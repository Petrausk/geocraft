import psutil
import os
import ctypes

class GeoCraft:
    def __init__(self):
        self.processes = []

    def list_processes(self):
        """List all running processes."""
        self.processes = [(proc.info['pid'], proc.info['name']) for proc in psutil.process_iter(['pid', 'name'])]
        return self.processes

    def prioritize_process(self, pid, priority_level):
        """Set the priority of a process given its PID."""
        try:
            process = psutil.Process(pid)
            priority = self._get_priority_value(priority_level)
            process.nice(priority)
            print(f"Process {process.name()} ({pid}) set to {priority_level} priority.")
        except psutil.NoSuchProcess:
            print(f"No such process with PID: {pid}")
        except psutil.AccessDenied:
            print("Access denied. Run as administrator to change process priorities.")
        except Exception as e:
            print(f"Error setting priority: {e}")

    def terminate_process(self, pid):
        """Terminate a process given its PID."""
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait()
            print(f"Process {process.name()} ({pid}) has been terminated.")
        except psutil.NoSuchProcess:
            print(f"No such process with PID: {pid}")
        except psutil.AccessDenied:
            print("Access denied. Run as administrator to terminate processes.")
        except Exception as e:
            print(f"Error terminating process: {e}")

    def _get_priority_value(self, priority_level):
        """Translate priority level to system value."""
        priorities = {
            "low": psutil.IDLE_PRIORITY_CLASS,
            "below_normal": psutil.BELOW_NORMAL_PRIORITY_CLASS,
            "normal": psutil.NORMAL_PRIORITY_CLASS,
            "above_normal": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
            "high": psutil.HIGH_PRIORITY_CLASS,
            "realtime": psutil.REALTIME_PRIORITY_CLASS
        }
        return priorities.get(priority_level.lower(), psutil.NORMAL_PRIORITY_CLASS)

def main():
    geocraft = GeoCraft()
    while True:
        print("\nGeoCraft System Task Manager")
        print("1. List all processes")
        print("2. Set process priority")
        print("3. Terminate process")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            processes = geocraft.list_processes()
            for pid, name in processes:
                print(f"PID: {pid}, Name: {name}")
        elif choice == '2':
            pid = int(input("Enter the PID of the process: "))
            priority = input("Enter priority (low, below_normal, normal, above_normal, high, realtime): ")
            geocraft.prioritize_process(pid, priority)
        elif choice == '3':
            pid = int(input("Enter the PID of the process to terminate: "))
            geocraft.terminate_process(pid)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()