from estrutura import *

entrada = [6, 24, 26, 35]

e1 = Componente('E1', None, None, None, None)
c1 = Componente('C1', 0, [], None, None)
serv1 = Servidor(1, 4, 8)
s1 = Componente('S1', None, None, None, None)

#print c1.nome, c1.qtd_serv, c1.list_serv

e1.saida = c1
c1.entrada = e1
c1.list_serv = [serv1]
s1.entrada = c1
c1.saida = s1

#print e1.saida.nome
#print c1.entrada.nome


teste = 10 + e1.saida.list_serv[0].atividade()
teste2 = 0 + e1.saida.list_serv[0].atividade()

#print teste
#print teste2

print c1.entrada.nome,
print "<->",
print e1.saida.nome,
print "<->",
print c1.saida.nome,


