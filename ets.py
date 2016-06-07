from random import randint

ETs = []

max = 50000
ini = 3
fim = 5
ant = 0
et = 0

while et <= max:
	et = randint(ini, fim)
	et = et + ant
	ETs.append(et)
	ant = et

print(ETs)
