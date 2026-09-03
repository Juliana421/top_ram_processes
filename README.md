# Top RAM Processes

A Python command-line tool that monitors system processes and displays the processes consuming the most physical RAM.

The tool uses the `psutil` library to collect process information and sort processes according to their Resident Set Size (RSS) memory usage.

## Features

* Displays processes using the most RAM.
* Shows the process ID (PID).
* Displays the process name.
* Reports RAM usage in megabytes (MB).
* Allows the user to specify how many processes to display.
* Handles processes that terminate during execution.
* Handles access restrictions and zombie processes.
* Uses RSS memory to measure actual physical RAM usage.

## Technologies

* Python 3
* `psutil`
* `argparse`

## Requirements

Python 3.x is required.

Install the `psutil` library:

```bash
pip install psutil
```

On some Linux environments, you may need:

```bash
pip install psutil --break-system-packages
```

## Usage

### Display the Top 3 Processes

By default, the program displays the three processes consuming the most RAM:

```bash
python3 top_ram_processes.py
```

### Display a Custom Number of Processes

Use the `--top` argument to specify how many processes you want to display:

```bash
python3 top_ram_processes.py --top 5
```

For example:

```bash
python3 top_ram_processes.py --top 10
```

## Output

The program displays the following information:

| Field          | Description                      |
| -------------- | -------------------------------- |
| PID            | Process identification number    |
| PROCESS NAME   | Name of the running process      |
| RAM USAGE (MB) | Physical RAM used by the process |

Example:

```text
PID     PROCESS NAME                  RAM USAGE (MB)
-------------------------------------------------------
1234    chrome                        842.31
5678    python3                       421.76
9012    code                          315.44
```

## How It Works

The script uses `psutil.process_iter()` to obtain information about running processes.

For each process, it retrieves:

* Process ID
* Process name
* Memory information

The script then obtains the Resident Set Size (RSS) value and converts it from bytes to megabytes.

The processes are sorted in descending order based on RAM usage, and only the requested number of processes is displayed.

```text
Running Processes
       |
       v
Collect Process Information
       |
       v
Get RSS Memory Usage
       |
       v
Convert Bytes → MB
       |
       v
Sort by RAM Usage
       |
       v
Display Top N Processes
```

## Security and System Administration Use

Monitoring resource usage can provide useful information during system administration and basic security investigations.

This tool can help identify:

* Unexpected resource-intensive processes.
* Applications consuming excessive memory.
* Processes that may require further investigation.
* Potentially abnormal system behavior.
* Resource consumption during troubleshooting.

High memory consumption does not necessarily indicate malicious activity. Any suspicious process should be investigated using additional system and security analysis techniques.

## Error Handling

Processes can terminate or change while the script is collecting information.

The application handles:

* `NoSuchProcess`
* `AccessDenied`
* `ZombieProcess`

When one of these conditions occurs, the affected process is skipped instead of terminating the entire program.

## Project Purpose

This project was developed as a cybersecurity and system administration learning exercise to demonstrate:

* Process monitoring
* System resource monitoring
* RAM analysis
* Python automation
* Exception handling
* Command-line interfaces
* Practical use of the `psutil` library

## Limitations

The tool provides a snapshot of RAM usage at the moment it is executed. It does not continuously monitor processes or perform historical resource tracking.

It also does not determine whether a process is malicious based solely on its memory consumption.

## Disclaimer

This project is intended for educational and authorized system administration purposes only.

Do not use the information produced by this tool to interfere with systems or processes that you are not authorized to manage.

## License

This project is provided for educational and cybersecurity learning purposes.
