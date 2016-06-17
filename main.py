import os
from definicoes import lista_objetos, get_componente
from ler_entrada import ler_arquivo
from ets import gera_ETs
from estrutura import Componente, Roteador

ler_arquivo('exemplo_2.in')


entrada = get_componente('E')
#entrada.list_espera_entrada = gera_ETs(50, 3, 5)
entrada.list_espera_entrada = [4, 8, 11, 16, 19, 23, 27, 30, 35, 40, 45, 50, 54]


#verificar objetos
for i in lista_objetos:
	print i.nome, i.list_espera_entrada, i.next
	#if i.__class__ is Componente and i.next:
	#	print(i.nome), (i.next.nome)
	#elif i.__class__ is Roteador:
	#	print(i.dict_saidas)


TS = 50
relogio = 1

def atualiza_lista_entrada(lista):
	lista.sort()
	for i in range(1, len(lista)):
		if lista[i] == lista[i-1]:
			lista[i] = (lista[i] + 1)


def transporta_entidade(origem, destino, et):
	print origem.nome, destino.list_espera_entrada, et
	destino.list_espera_entrada.append(et)
	atualiza_lista_entrada(destino.list_espera_entrada)
	origem.list_espera_entrada.pop()







while relogio < TS:
	for componente in lista_objetos:
		if componente.list_espera_entrada and componente.list_espera_entrada[0] == relogio:
			print(componente.list_espera_entrada)
			print relogio
			# enviar entidade temporaria para a proxima lista
			transporta_entidade(componente, componente.next, componente.list_espera_entrada[0])


			# executar proximo componente para verificar se precisa fazer alguma coisa





	relogio += 1
		