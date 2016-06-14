import os
import definicoes
import ler_entrada
from estrutura import Componente, Roteador

ler_entrada.ler_arquivo('exemplo_4.in')

objetos = []

for i in definicoes.lista_objetos:
	objetos.append(i)

#							   0  1  2   3   4   5   6
#lista de objetos exemplo 4 = [E, S, C1, C2, I1, R1, R2]

#faz as ligacoes entre os objetos
objetos[0].next = objetos[2]
objetos[2].next = objetos[5]
objetos[4].next = objetos[3]
objetos[3].next = objetos[6]

for i in objetos:
	if i.__class__ is Componente and i.next:
		print(i.nome), (i.next.nome)
	elif i.__class__ is Roteador:
		print(i.dict_saidas)


TS = 50000

true = True
relogio = 0

while true:
	relogio += 1

	
	
	

	if relogio == TS:
		true = False
