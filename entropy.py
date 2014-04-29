#!/usr/bin/env python

#Calcula la entropia de las fuentes, tomando como fuente IPS

import sys
import math

# Descartar ips con entropia 0
descartar = True
#

if len(sys.argv) < 2:
	sys.exit("Uso (type puede ser: sender, receiver) : python2 entropy.py file_path type")

ips_en_red = list()
f = open(sys.argv[1], 'r')

#Consigo las diferentes IP's
for line in f:
	#Sacar ips y ponerlas en list
	datos = line.split(", ")

	if datos[0] == "ARP-Operacion":
		continue

	#Ip-Src esta en la posicion 3
	if not (datos[3] in ips_en_red):
		ips_en_red.append(datos[3])

	#Ip-Dst esta en la posicion 4
	if not (datos[4] in ips_en_red):
		ips_en_red.append(datos[4])

#Calculo la entropia de cada IP
for ip in ips_en_red:
	f.seek(0)
	ips_receptoras = [0] * len(ips_en_red)
	ips_emisoras = [0] * len(ips_en_red)
	#Paquetes como receptor
	total_receptor = 0
	#Paquetes como emisor
	total_emisor = 0
	for line in f:
		datos = line.split(", ")

		if datos[0] == "ARP-Operacion":
			continue

		#Si la fuente es la IP
		if sys.argv[2] == "sender":
			if datos[3] == ip:
				total_emisor = total_emisor + 1
				#Aumento la probabilidad de mandarle desde IP
				index = ips_en_red.index(datos[4])
				ips_receptoras[index] = ips_receptoras[index] + 1

		#Si el receptor es la IP
		if sys.argv[2] == "receiver":
			if datos[4] == ip:
				total_receptor = total_receptor + 1
				#Aumento la probabilidad de recibir un paquete a IP desde un emisor
				index = ips_en_red.index(datos[3])
				ips_emisoras[index] = ips_emisoras[index] + 1

	entropy = 0
	if sys.argv[2] == "sender":
		for muestra in ips_receptoras:
			if muestra != 0:
				entropy = entropy + (float(muestra)/total_emisor)*(-math.log((float(muestra)/total_emisor), 2))
		print ip + " " + str(entropy)

	if sys.argv[2] == "receiver":
		for muestra in ips_emisoras:
			if muestra != 0:
				entropy = entropy + (float(muestra)/total_receptor)*(-math.log((float(muestra)/total_receptor), 2))
		print ip + " " + str(entropy)

f.close()