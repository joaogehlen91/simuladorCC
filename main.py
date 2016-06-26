# -*- coding: utf-8 -*-
import estatistica        as est
import definicoes 	 	  as df
from sys				  import argv
from ler_entrada          import ler_arquivo
from ets                  import gera_ETs
from estrutura            import Componente, Roteador
from roteador             import roteador
from infinitos_servidores import infinitos_servidores
from multiplos_servidores import multiplos_servidores


def atualiza_lista_entrada(lista):
	lista.sort()
	for i in range(1, len(lista)):
		if lista[i] == lista[i-1]:
			lista[i] = (lista[i] + 1)


def executa_entrada(componente):
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


#Argumento da linha de comando
ler_arquivo(argv[1])

entrada = df.get_componente('E')

#entrada.list_espera_entrada = gera_ETs(10, 3, 5)
entrada.list_espera_entrada = gera_ETs(df.TS, df.TC[0], df.TC[1])
#entrada.list_espera_entrada = [4, 8, 11, 16, 19, 23, 27, 30, 35, 40, 45, 50, 54]
entradaC = [x for x in entrada.list_espera_entrada]




#verificar objetos
print("Obejtos Criados:")
for i in df.lista_objetos:
	if i.__class__ is Componente and i.next:
		print(i.nome, i.next.nome)
	if i.__class__ is Roteador:
		print(i.nome, i.dict_saidas)
print("--------------------")


print(df.get_componente('E').list_espera_entrada)

relogio = 1
while relogio <= df.TS:
	print("\n------------------------------\nTempo:", relogio)

	for componente in df.lista_objetos:
		#print(componente.nome, componente.list_espera_entrada)
		#if 'S' in componente.nome:
		#	print(componente.nome, componente.list_espera_entrada)

		if 'E' in componente.nome and componente.list_espera_entrada and componente.list_espera_entrada[0] == relogio:
			executa_entrada(componente)
			#print("Origem/Destino:", componente.nome, componente.next.nome)

		if 'C' in componente.nome and componente.list_espera_entrada and componente.list_espera_entrada[0] == relogio:
			executa_componente(componente)
			#print("Origem/Destino:", componente.nome, componente.next.nome)

		if 'I' in componente.nome and componente.list_espera_entrada and componente.list_espera_entrada[0] == relogio:
			executa_infinito(componente)
			#print("Origem/Destino:", componente.nome, componente.next.nome)

			# executar proximo componente para verificar se precisa fazer alguma coisa
		est.atualiza_estatisticas(componente, relogio)
	relogio += 1

est.gera_resultados(entradaC)

#print(get_componente('S').list_espera_entrada)
#print(len(get_componente('S').list_espera_entrada))
