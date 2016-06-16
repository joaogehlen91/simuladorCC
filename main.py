import os
import definicoes
import ler_entrada
from estrutura import Componente, Roteador

ler_entrada.ler_arquivo('exemplo_4.in')



for i in definicoes.lista_objetos:
	if i.__class__ is Componente and i.next:
		print(i.nome), (i.next.nome), (i.list_espera_entrada)
	elif i.__class__ is Roteador:
		print(i.dict_saidas)


TS = 50000

relogio = 0

while relogio < TS:
	relogio += 1

	
	
	

	
