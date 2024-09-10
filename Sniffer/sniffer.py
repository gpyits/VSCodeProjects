from scapy.all import *
from scapy.layers.http import *

iPkt=0

def process_packet(pkt):
    global iPkt
    iPkt+=1
    print(f'\npkt received no. {iPkt}')

    if not pkt.haslayer(IP):
        return

    if pkt[IP].proto==6:
        if pkt[TCP].sport==80 or pkt[TCP].dport==80:
            print('riconosciuto pacchetto HTTP')
            if pkt[TCP].dport==80:
                print('-> richiesta')
                print('HttpRequest')
            else:
                print('-> risposta')
                print('HttpResponse')
                if pkt.haslayer(HTTPResponse):
                    print(pkt[HTTPResponse].show())
        elif pkt[TCP].sport==443 or pkt[TCP].dport==443:
            print('riconosciuto pacchetto TLS')
        print("SOURCE_PORT: " + str(pkt[TCP].sport) + " | DEST_PORT: " + str(pkt[TCP].dport))

    #stampa i dati del layer ip
    ip_layer='PKT_SRC: '+pkt[IP].src+' PKT_DEST: '+pkt[IP].dst+' PKT_PROTO: '+str(pkt[IP].proto)+' PKT_LEN: '+str(pkt[IP].len)
    #print(ip_layer)

ip_layer=0

sniff(iface='enp4s0', filter='tcp', prn=process_packet)