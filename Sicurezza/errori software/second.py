import os
import time

def file_access(filename):
    # Check if file exists
    if os.path.exists(filename):
        print("[Main] File exists. Preparing to read...")
        with open(filename, "r") as f:
            content = f.read()
        print("[Main] File content:", content)
    else:
        print("[Main] File does not exist.")

       
file_access("prova.txt")

