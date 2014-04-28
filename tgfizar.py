#!/usr/bin/env python
import sys

if len(sys.argv) < 1:
	sys.exit("Usage: python2 tgfizar.py file_path")


ips_en_red = list()
#Lista de tuplas (Ip-Src, Ip-Dst)
messages = list()
f = open(sys.argv[1], 'r')
#Conisgo todas las IP's
for line in f:
	#Sacar ips y ponerlas en list
	datos = line.split(", ")

	if datos[0] == "ARP-Operacion":
		continue

	#Ip-Src esta en la posicion 3
	if not (datos[3] in ips_en_red):
		ips_en_red.append(datos[3])

	#Ip-Src esta en la posicion 4
	if not (datos[4] in ips_en_red):
		ips_en_red.append(datos[4])

	#Guardo mensaje
	messages.append((ips_en_red.index(datos[3]),ips_en_red.index(datos[4])))

for i in range(len(ips_en_red)):
	print str(i+1) + " " + ips_en_red[i]

print "#"

writen_messages = list()
for msg in messages:
	if not (msg in writen_messages):
		print str(msg[0]+1) + " " + str(msg[1]+1)
		writen_messages.append(msg)

f.close()