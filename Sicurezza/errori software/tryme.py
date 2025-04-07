import threading
import time
import random

# Shared bank account balance
balance = 1000

def deposit(amount):
    global balance
    # Read the balance
    local_copy = balance
    # Random delay to simulate context switching
    time.sleep(random.uniform(0.001, 0.005))
    # Modify the local copy and write it back
    local_copy += amount
    balance = local_copy

def withdraw(amount):
    global balance
    # Read the balance
    local_copy = balance
    # Random delay to simulate context switching
    time.sleep(random.uniform(0.001, 0.005))
    # Modify the local copy and write it back
    local_copy -= amount
    balance = local_copy

def perform_deposit():
    for _ in range(100):
        deposit(5)

def perform_withdraw():
    for _ in range(100):
        withdraw(5)

# Create and start 10 threads
threads = []
for _ in range(10):
    t = threading.Thread(target=perform_deposit)
    threads.append(t)
    t.start()
    t1 = threading.Thread(target=perform_withdraw)
    threads.append(t1)
    t1.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Final balance:", balance)
