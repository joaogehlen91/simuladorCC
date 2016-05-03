from estrutura import *

arq = open("exemplo_1.in", "r")

texto = arq.read()

lista = texto.replace("\n", "").split(";")

print (lista)
