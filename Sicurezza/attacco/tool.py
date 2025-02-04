import os

ips=["22", "30", "86", "90", "82"]

packet_number = 1*10**5

for ip in ips:
    os.system(f"ab -n {packet_number} -c 256 http://10.8.0.{ip}:8888/")