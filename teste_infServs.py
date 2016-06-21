# Um componente com infinitos servidores

from estrutura import *
from definicoes import *
from ler_entrada import *

entrada = [6, 24, 26, 35, 41, 52]
ler_arquivo("exemplo_2.in")

objetos = []
servidor = []

for i in lista_objetos:
  objetos.append(i)
  print(i.nome)

i1 = get_componente("I1")
for i in i1.list_serv:
  servidor.append(i)

som  =  0
aux = 0

saida = []
atend = []

for i in entrada:
  aux  = servidor[0].atividade()
  atend.append(aux)
  som  = i + aux
  saida.append(som)

print("\nEntrada -> %s" % entrada)
print("Tempo -> %s" % atend)
print("Saida -> %s "% saida)
