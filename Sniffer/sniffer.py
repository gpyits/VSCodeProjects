from scapy.all import *

iPkt=0

def process_packet(pkt):
    global iPkt
    iPkt+=1
    print(f'Ho ricevuto un pkt {iPkt}')

ip_layer=0

sniff(iface='enp4s0', filter='tcp', prn=process_packet)