#!/usr/bin/env python

#Calcula la entropia de las fuentes, tomando como fuente IPS

import sys

# Descartar ips con entropia 0
descartar = True
#

if len(sys.argv) < 2:
	sys.exit("Uso (type puede ser: sender, reciever, both) : python2 entropy.py file_path type")

ips_en_red = list()

f = open(sys.argv[1], 'r')

#Consigo las diferentes IP's
for line in f:
	#Sacar ips y ponerlas en list
	datos = line.split(", ")

	#Ip-Src esta en la posicion 3
	if not (datos[3] in ips_en_red):
		ips_en_red.append(datos[3])

	#Ip-Dst esta en la posicion 4
	if not (datos[4] in ips_en_red):
		ips_en_red.append(datos[4])

ips_reciben = [0] * len(ips_en_red)
ips_mandan = [0] * len(ips_en_red)

#Calcular la cantidad de veces que aparece cada IP
f.seek(0)
total = 0
for line in f:
	#Sacar ips y ponerlas en list
	datos = line.split(", ")

	total = total + 1

	index = ips_en_red.index(datos[3])
	ips_reciben[index] = ips_reciben[index] + 1

	index = ips_en_red.index(datos[4])
	ips_mandan[index] = ips_mandan[index] + 1

print "Total de paquetes: " + str(total)

if sys.argv[2] == "sender":
	print "Entropia por emisor"

	for i in range(len(ips_en_red)):
		if ips_mandan[i] == 0:
			entropy = 0
		else :
			entropy = float(ips_mandan[i]) / total
		if descartar and entropy != 0:
			print ips_en_red[i] + ", " + str(entropy)

if sys.argv[2] == "reciever":
	print "Entropia por receptor"

	for i in range(len(ips_en_red)):
		if ips_reciben[i] == 0:
			entropy = 0
		else :
			entropy = float(ips_reciben[i]) / total
		if descartar and entropy != 0:
			print ips_en_red[i] + ", " + str(entropy)

if sys.argv[2] == "both":
	print "Entropia por receptor y emisor"

	for i in range(len(ips_en_red)):
		if (ips_reciben[i] + ips_mandan[i]) == 0:
			entropy = 0
		else :
			entropy = float(ips_reciben[i] + ips_mandan[i]) / total
		if descartar and entropy != 0:
			print ips_en_red[i] + ", " + str(entropy)

f.close()