import os
from definicoes import lista_objetos, get_componente
from ler_entrada import ler_arquivo
from ets import gera_ETs
from estrutura import Componente, Roteador

ler_arquivo('exemplo_2.in')


entrada = get_componente('E')
entrada.list_espera_entrada = gera_ETs(50000, 3, 5)


#verificar objetos
for i in lista_objetos:
	print i.nome
	#if i.__class__ is Componente and i.next:
	#	print(i.nome), (i.next.nome)
	#elif i.__class__ is Roteador:
	#	print(i.dict_saidas)


TS = 50000
relogio = 0


while relogio < TS:
	relogio += 1

	for i in lista_objetos:
		if i.list_espera_entrada and i.list_espera_entrada[0] == relogio:
			pass
			# enviar entidade temporaria para a proxima lista
			# executar proximo componente para verificar se precisa fazer alguma coisa
			

		