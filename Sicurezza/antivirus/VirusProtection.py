# python3 VirusProtection.py

import time
import os
import argparse
import psutil
import threading

# def input_with_timeout(prompt, timeout):
#     def get_input():
#         nonlocal user_input
#         user_input = input(prompt)

#     user_input = None
#     input_thread = threading.Thread(target=get_input)
#     input_thread.start()
#     input_thread.join(timeout)

#     if input_thread.is_alive():
#         print("\nInput timed out.")
#         return None
#     return user_input

def check_new_processes():
    existing_pids = set(psutil.pids())
    while True:
        time.sleep(5)
        current_pids = set(psutil.pids())
        new_pids = current_pids - existing_pids
        for pid in new_pids:
            try:
                process = psutil.Process(pid)
                print(f"New process detected: {process.name()} (PID: {pid})")
                terminate = input(f"Do you want to terminate the process {process.name()} (PID: {pid})? (y/n): ")
                if terminate.lower() == 'y':
                    process.terminate()
                    print(f"Process {process.name()} (PID: {pid}) terminated.")
                else:
                    print(f"Process {process.name()} (PID: {pid}) not terminated.")
            except psutil.NoSuchProcess:
                print(f"Process with PID {pid} no longer exists.")
                continue
            except psutil.AccessDenied:
                print(f"Access denied to process with PID {pid}.")
                continue
            except psutil.ZombieProcess:
                print(f"Zombie process with PID {pid}.")
                continue
            except psutil.TimeoutExpired:
                print(f"Timeout expired for process with PID {pid}.")
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
        existing_pids = current_pids

if __name__ == "__main__":
    check_new_processes()
