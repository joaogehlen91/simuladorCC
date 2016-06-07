from estrutura import *

entrada = [6, 24, 26, 35]

# Parte da configuracao

e  = Componente("E", None, None, None, None)  			  #Componente Entrada
s  = Componente("S", None, None, None, None)  			  #Componente Saida
c1 = Componente("C1", 2, [serv1, serv2], None, None)	  #Componente 1 - Caixa

serv1 = Servidor(1, 10, 35, 0, 0, False) 				  			 #(id, ini, fim, ult_saida) Servidor
serv2 = Servidor(2, 10, 20, 0, 0, False) 				  			 #(id, ini, fim, ult_saida) Servidor

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
ent   = []
saida = []

for i in entrada:
  if i < som:
    i = som
  if servidor1.atendimento == False and servidor2.atendimento == False:
      servidor1.atendimento = True
	  aux  = servidor1.atividade()
	  som  = i + aux
	  ent.append(i)
	  saida.append(aux + i)
	  
  elif servidor1.atendimento == False and servidor2.atendimento == True:
  elif servidor1.atendimento == True and servidor2.atendimento == False:
  elif servidor1.atendimento == True and servidor2.atendimento == True:

  print(i, aux)

entrada = ent
  
print(entrada)
print(saida)

