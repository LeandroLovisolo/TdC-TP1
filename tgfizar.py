#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
	sys.exit("Usage: python2 tgfizar.py file_path ip_root")


ips_en_red = list()
f = open(sys.argv[1], 'r')
for line in f:
	#Sacar ips y ponerlas en list
	datos = line.split(", ")

	#Ip-Src esta en la posicion 3
	if not (datos[3] in ips_en_red):
		ips_en_red.append(datos[3])

	#Ip-Src esta en la posicion 4
	if not (datos[4] in ips_en_red):
		ips_en_red.append(datos[4])

for i in range(len(ips_en_red)):
	print str(i+1) + " " + ips_en_red[i]

print "#"

for i in range(len(ips_en_red)):
	print str(datos.index(sys.argv[2])+1) + " " + str(i+1)