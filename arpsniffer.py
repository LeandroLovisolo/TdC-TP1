#!/usr/bin/env python

#Script comentado es script dado en el taller (transcripto por si es necesario)
# arping2tex : arpings a network and outputs a LaTeX table as a r e s u l t
# import sys
# if len(sys.argv) != 2 :
# 	print "Usage : arping2tex <net> eg: arping2tex 192.168.1.0/24"
# 	sys.exit(1)

# from scapy.all import *
# conf.verb = 0
# ans, unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),timeout=2)
# print r "\begin{tabular}{|l|l|}"
# print r "\hline"
# print r "\MAC & IP \\"
# print r "\hline
# for snd, rcv in ans:
# 	print rcv.sprintf(r" %Ether.src&& ARP.prsc & \\")
# printr r"\hline"
# printf r"\end{tabular}"


#Script captura paquetes ARP correr con sudo y tener tcpdump instalado
from scapy.all import *
import time
def monitor_callback(pkt):
	#print pkt.show() Solo para debugging
	if ARP in pkt:
		#Usuo sprintf para ARP para que me nombre la operacion, no el numero
		op = pkt.sprintf("%ARP.op%")
		#Imprimo solo los who-has
		if pkt[ARP].op == 1:
			#Alternativa 1
			print op+", "+str(pkt[ARP].hwsrc)+", "+str(pkt[ARP].hwdst)+", "+str(pkt[ARP].psrc)+", "+str(pkt[ARP].pdst) + ", " + str(pkt[Ether].dst) + ", " + str(pkt[Ether].src + ", " + str(int(time.time())))
			#Alternativa 2
			#print pkt.sprintf("%ARP.op%, %ARP.hwsrc%, %ARP.hwdst%, %ARP.psrc%, %ARP.pdst%, %Ether.dst%, %Ether.src%")


if __name__ == '__main__':
	#Operacion 1: who-has
	print "ARP-Operacion, ARP-MAC-Src, ARP-MAC-Dst, ARP-IP-Src, ARP-IP-Dst, Ether-MAC-Dst, Ether-MAC-Src, Tiempo"
	sniff(prn=monitor_callback, filter = "arp", store = 0)