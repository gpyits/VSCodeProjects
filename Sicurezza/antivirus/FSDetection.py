# installare watchdog con apt install python3-watchdog
# python3 VirusProtection.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import argparse
import psutil
import threading

def get_process_that_created_file(file_path):
    """
    Scans active processes and checks which one created the given file.
    """
    file_path = os.path.abspath(file_path)

    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            # Get list of open files for the process
            open_files = proc.info['open_files']
            if open_files:
                for f in open_files:
                    if f.path == file_path:
                        return f"{proc.info['name']} (PID: {proc.info['pid']})"
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return None  # No matching process found

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Get the process that created the file
        print(f"Created: {event.src_path}")
        process_name = get_process_that_created_file(event.src_path)
        if process_name:
            print(f"Created by: {process_name}")
        else:
            print("Process not found")

    def on_modified(self, event):
        print(f"Modified: {event.src_path}")
        process_name = get_process_that_created_file(event.src_path)
        if process_name:
            print(f"Modified by: {process_name}")
        else:
            print("Process not found")

    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")
        process_name = get_process_that_created_file(event.src_path)
        if process_name:
            print(f"Deleted by: {process_name}")
        else:
            print("Process not found")

def watch_directory(directory):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)  # `recursive=True` watches subdirectories
    observer.start()

    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watch a directory for changes.")
    parser.add_argument("-d", "--directory", nargs="?", default=os.path.expanduser("~"), help="Directory to watch. Defaults to the home directory.")
    args = parser.parse_args()
    directory_to_watch = args.directory
    watch_directory(directory_to_watch)
 