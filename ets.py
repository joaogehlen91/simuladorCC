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
