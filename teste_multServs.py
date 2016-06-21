# Um componente com multiplos servidores

from estrutura import *
from definicoes import *
from ler_entrada import *

def zerarAtendimento(servs):
  for x in range(0, len(servs)):
    servs[x].atendimento = False

entrada = [6, 24, 26, 35, 41]
ler_arquivo("exemplo_1.in")

objetos = []
servidores = []

for i in lista_objetos:
  objetos.append(i)
  print(i.nome)

c1 = get_componente("C1")
for i in c1.list_serv:
  servidores.append(i)

som  =  0
aux = 0
inc =  0
x = 0

saida = []
espera = []
atend = []

full = False

for i in entrada:

  inc = i

  if x < len(servidores):
    if servidores[x].atendimento == False:
      servidores[x].atendimento = True
      aux  = servidores[x].atividade()
      atend.append(aux)
      som  = inc + aux
      saida.append(som)
      x+=1
  else:
    full = True

  if full == True:   #Todos servidores ocupados
    for x in range(0, len(servidores)):
      if servidores[x].atendimento == True:
        espera.append(i)
        break

zerarAtendimento(servidores)
tam = len(servidores)
print("\nNúmero de Servidores: %s" % tam)

for i in range(0, len(espera)):
  if x > tam-1:
    zerarAtendimento(servidores)
    x = 0

  if espera[i] < saida[i]:
    if inc < som:
      inc = som

    if servidores[x].atendimento == False:
      servidores[x].atendimento = True
      aux  = servidores[x].atividade()
      atend.append(aux)
      som  = saida[i] + aux
      saida.append(som)
      x+=1
    else:
      x = 0
  else:
    inc = espera[i]
    if servidores[x].atendimento == False:
      servidores[x].atendimento = True
      aux  = servidores[x].atividade()
      atend.append(aux)
      som  = inc + aux
      saida.append(som) 
      x+=1

print("Entrada -> %s" % entrada)
print("Tempo -> %s" % atend)
print("Saida -> %s \n"% saida)
#print("\nEspera -> %s\n" % espera)