"""
top_ram_processes.py

Shows the top N processes consuming the most RAM (default: 3).

Requires: psutil
    pip install psutil --break-system-packages

Usage:
    python3 top_ram_processes.py
    python3 top_ram_processes.py --top 5
"""

import argparse

import psutil # type: ignore


def get_top_ram_processes(top_n: int = 3) -> list:
    """
    Return a list of the top_n processes sorted by RSS memory usage
    (Resident Set Size, i.e. actual physical RAM used), descending.

    Each item is a dict with: pid, name, memory_mb
    """
    processes = []

    for proc in psutil.process_iter(attrs=["pid", "name", "memory_info"]):
        try:
            mem_info = proc.info["memory_info"]
            if mem_info is None:
                continue
            memory_mb = mem_info.rss / (1024 * 1024)  # bytes -> MB
            processes.append(
                {"pid": proc.info["pid"], "name": proc.info["name"], "memory_mb": memory_mb}
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Process may have ended or we lack permission; skip it.
            continue

    processes.sort(key=lambda p: p["memory_mb"], reverse=True)
    return processes[:top_n]


def main() -> None:
    parser = argparse.ArgumentParser(description="Show the top N processes by RAM usage.")
    parser.add_argument("--top", type=int, default=3, help="Number of top processes to show (default: 3).")
    args = parser.parse_args()

    top_processes = get_top_ram_processes(args.top)

    print(f"{'PID':<8}{'PROCESS NAME':<30}{'RAM USAGE (MB)'}")
    print("-" * 55)
    for proc in top_processes:
        print(f"{proc['pid']:<8}{proc['name']:<30}{proc['memory_mb']:.2f}")


if __name__ == "__main__":
    main()
