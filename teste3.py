from estrutura import *

entrada = [6, 24, 26, 35]

# Parte da configuracao

serv1 = Servidor(1, 10, 35, 0, 0, False)                 #(id, ini, fim, ult_saida) Servidor
serv2 = Servidor(2, 10, 20, 0, 0, False)                 #(id, ini, fim, ult_saida) Servidor

e  = Componente("E", None, None, None, None)  			  #Componente Entrada
s  = Componente("S", None, None, None, None)  			  #Componente Saida
c1 = Componente("C1", 2, [serv1, serv2], None, None)	#Componente 1 - Caixa com 2 servidores

c1.list_serv.append(serv1)

e.saida    = c1  #E->C1
c1.entrada = e	 #E<-C1

s.entrada  = c1  #C1->S
c1.saida   = s   #C1<-S

# Fim da parte da configuracao

servidor1 = c1.list_serv[0]
servidor2 = c1.list_serv[1]


# Um componente com dois servidor
som   = 0
aux   = 0
inc   = 0
saida = []
espera = []
atend = []

for i in entrada:
  if inc < som and servidor1.atendimento == False and servidor2.atendimento == False: 
    inc = som
  else:
   inc = i

  if servidor1.atendimento == False and servidor2.atendimento == False or servidor1.atendimento == False and servidor2.atendimento == True:
    servidor1.atendimento = True

    aux  = servidor1.atividade()
    atend.append(aux)
    som  = inc + aux
    saida.append(aux + inc) 

  elif servidor1.atendimento == True and servidor2.atendimento == False:
    servidor2.atendimento = True

    aux  = servidor2.atividade()
    atend.append(aux)
    som  = inc + aux
    saida.append(aux + inc)
    
  elif servidor1.atendimento == True and servidor2.atendimento == True:
    espera.append(i)


servidor1.atendimento = False
servidor2.atendimento = False

for i in range(0, len(espera)):
  if espera[i] < saida[i]:
    if servidor1.atendimento == False and servidor2.atendimento == False or servidor1.atendimento == False and servidor2.atendimento == True:
      servidor1.atendimento = True
      aux  = servidor1.atividade()
      atend.append(aux)
      som  = saida[i] + aux
      saida.append(som)

    elif servidor1.atendimento == True and servidor2.atendimento == False:
      servidor2.atendimento = True
      aux  = servidor2.atividade()
      atend.append(aux)
      som  = saida[i] + aux
      saida.append(som)
  else:
    if inc < som and servidor1.atendimento == False and servidor2.atendimento == False: 
      inc = som

    if servidor1.atendimento == False and servidor2.atendimento == False or servidor1.atendimento == False and servidor2.atendimento == True:
      servidor1.atendimento = True

      aux  = servidor1.atividade()
      atend.append(aux)
      som  = inc + aux
      saida.append(aux + inc) 

    elif servidor1.atendimento == True and servidor2.atendimento == False:
      servidor2.atendimento = True

      aux  = servidor2.atividade()
      atend.append(aux)
      som  = inc + aux
      saida.append(aux + inc)


servidor1.atendimento = False
servidor2.atendimento = False

#entrada = ent
  
print("\nEntrada -> %s" % entrada)
print("Tempo -> %s" % atend)
print("Saida -> %s "% saida)
print("\nEspera -> %s\n" % espera)

