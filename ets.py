# -*- coding: utf-8 -*-

from random import randint


def gera_ETs(max, ini, fim, ant=0, et=0):
	ETs = []
	while et <= max:
		et = randint(ini, fim)
		et = et + ant
		ETs.append(et)
		ant = et

	return ETs

if __name__ == "__main__":
	ETs = gera_ETs(1000, 3, 5)
	print(ETs)
	print(len(ETs))
