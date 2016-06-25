# -*- coding: utf-8 -*-

import os
import estatistica        as est
from definicoes           import lista_objetos, get_componente
from ler_entrada          import ler_arquivo
from ets                  import gera_ETs
from estrutura            import Componente, Roteador
from roteador             import roteador
from infinitos_servidores import infinitos_servidores
from multiplos_servidores import multiplos_servidores

ler_arquivo('exemplo_6.in')


entrada = get_componente('E')
entrada.list_espera_entrada = gera_ETs(10, 3, 5)
#entrada.list_espera_entrada = [4, 8, 11, 16, 19, 23, 27, 30, 35, 40, 45, 50, 54]


#verificar objetos
print("Obejtos Criados:")
for i in lista_objetos:
	if i.__class__ is Componente and i.next:
		print(i.nome, i.next.nome)
	if i.__class__ is Roteador:
		print(i.nome, i.dict_saidas)
print("--------------------")


TS = 20
relogio = 1

def atualiza_lista_entrada(lista):
	lista.sort()
	for i in range(1, len(lista)):
		if lista[i] == lista[i-1]:
			lista[i] = (lista[i] + 1)


def entrada(componente):
	origem = componente
	destino = componente.next
	et = origem.list_espera_entrada[0]

	if destino.__class__ is Roteador:
		destino = roteador(origem.nome)

	destino.list_espera_entrada.append(et)
	atualiza_lista_entrada(destino.list_espera_entrada)
	origem.list_espera_entrada.pop(0)


def executa_componente(componente):
	etmp = multiplos_servidores(componente.nome)
	transporta_entidade(componente, etmp)


def executa_infinito(componente):
	etmp = infinitos_servidores(componente.nome)
	transporta_entidade(componente, etmp)


def transporta_entidade(componente, et):
	origem = componente
	destino = componente.next
	if destino.__class__ is Roteador:
		destino = roteador(origem.nome)

	destino.list_espera_entrada.append(et)
	atualiza_lista_entrada(destino.list_espera_entrada)
	origem.list_espera_entrada.pop(0)


print(get_componente('E').list_espera_entrada)

while relogio < TS:
	print("\n------------------------------\nTempo:", relogio)

	for componente in lista_objetos:

		print(componente.nome, componente.list_espera_entrada)
		#if 'S' in componente.nome:
		#	print(componente.nome, componente.list_espera_entrada)

		if 'E' in componente.nome and componente.list_espera_entrada and componente.list_espera_entrada[0] == relogio:
			entrada(componente)
			print("Origem/Destino:", componente.nome, componente.next.nome)

		if 'C' in componente.nome and componente.list_espera_entrada and componente.list_espera_entrada[0] == relogio:
			executa_componente(componente)
			print("Origem/Destino:", componente.nome, componente.next.nome)

		if 'I' in componente.nome and componente.list_espera_entrada and componente.list_espera_entrada[0] == relogio:
			executa_infinito(componente)
			print("Origem/Destino:", componente.nome, componente.next.nome)

			# executar proximo componente para verificar se precisa fazer alguma coisa
		est.atualiza_estatisticas(componente, relogio)
	relogio += 1

est.gera_resultados()

#print(get_componente('S').list_espera_entrada)
#print(len(get_componente('S').list_espera_entrada))
