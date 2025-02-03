# GeoCraft

GeoCraft is a Python-based system task management tool designed to assist in managing and prioritizing system tasks to optimize performance on Windows systems. This tool allows users to view running processes, change their priorities, and terminate them if necessary.

## Features

- List all running processes with their Process ID (PID) and name.
- Set the priority of a process to optimize system performance.
- Terminate unwanted or unresponsive processes.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the `psutil` library using pip:

   ```bash
   pip install psutil
   ```

3. Download or clone the GeoCraft repository.

## Usage

1. Run the `geocraft.py` script:

   ```bash
   python geocraft.py
   ```

2. Follow the on-screen instructions to:
   - List all processes.
   - Set the priority of a process by entering its PID and desired priority level.
   - Terminate a process by entering its PID.

## Priority Levels

- `low`
- `below_normal`
- `normal`
- `above_normal`
- `high`
- `realtime`

**Note:** Changing process priorities and terminating processes may require administrative privileges.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you'd like to help improve GeoCraft, please fork the repository and submit a pull request.

## Disclaimer

Use this tool at your own risk. Terminating or changing the priority of system-critical processes can affect system stability.