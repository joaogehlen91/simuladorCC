from estrutura import *

entrada = [6, 24, 26, 35]

# Parte da configuracao

e  = Componente("E", None, None, None, None)  #Componente Entrada
s  = Componente("S", None, None, None, None)  #Componente Saida
c1 = Componente("C1", 0, [], None, None)	  #Componente 1 - Caixa

serv1 = Servidor(1, 1, 4, 0) 				  #(id, ini, fim, ult_saida) Servidor

c1.list_serv.append(serv1)

e.saida    = c1  #E->C1
c1.entrada = e	 #E<-C1

s.entrada  = c1  #C1->S
c1.saida   = s   #C1<-S

# Fim da parte da configuracao ou inicio de outra coisa 

servidor = c1.list_serv[0]

for i in entrada:
	joao     = i + servidor.atividade()
	
	if i < joao:
		i = joao
		
	servidor.ult_saida = i
	print(servidor.ult_saida)





