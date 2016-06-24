from os            import system
import ler_entrada as le
import definicoes  as df

'''
   (1) x Ociosidade das entidades permanentes, individualmente por servidor (exceto para centros de serviço com infinitos servidores). 
   (2) x Ociosidade média por componente.
   (3) x Ociosidade média geral de todos os componentes com servidores.
   (4) Tempo médio de espera das ETs na fila de cada componente;
   (5) Tempo médio de atendimento das entidades temporárias em cada componente;
   (6) Tempo médio de permanência, no modelo, das Ets.
   (7) Número médio de ETs na fila de cada componente que possui contenção.
'''

arq = open("estatisticas.out", "w")

#Ociosidade das entidades permanentes, individualmente por servidor
def calcula_1():
   lst = df.get_todos_componentes_por_nome('C')
   arq.write("*** 1) Ociosidade das entidades permanentes, individualmente por servidor ***\n")

   for x in lst:
      arq.write("\n             ---------------- COMPONENTE %s ----------------\n" % x.nome)

      for serv in x.list_serv:
         arq.write("                     Ociosidade Servidor %s ---> %0.2f\n" % (serv.nome, serv.ociosidade))
   return


#Ociosidade média por componente.
def calcula_2():
   lst = df.get_todos_componentes_por_nome('C')
   arq.write("\n\n*** 2) Ociosidade média por componente. ***\n")

   for x in lst:
      arq.write("\n             ---------------- COMPONENTE %s ----------------\n" % x.nome)
      arq.write("                     Ociosidade Média  ---> %0.2f\n" % (sum([serv.ociosidade for serv in x.list_serv]) / len(x.list_serv)))
   return


#Ociosidade média geral de todos os componentes com servidores.
def calcula_3():
   lst = df.get_todos_componentes_por_nome('C')
   arq.write("\n\n*** 3) Ociosidade média geral de todos os componentes com servidores. ***\n")
   soma = 0

   for comp in lst:      
      soma += sum([x.ociosidade for x in comp.list_serv])

   arq.write("                     Ociosidade Média Geral ---> %0.2f\n" % (0 if len(lst) <= 0 else (soma / len(lst))))
   pass



def gera_resultados():
   system("clear")
   calcula_1()
   calcula_2()
   calcula_3()

   arq.close()
   pass

def atualiza_servidores(list_serv, relogio):
   for serv in list_serv:
      if (relogio - serv.ult_saida) > 0: 
         serv.ociosidade += 1

      print("Ult_Saida / Ociosidade    -> %d / %d" % (serv.ult_saida, serv.ociosidade))

def atualiza_estatisticas(componente, relogio):
   if 'C' in componente.nome:
      print("Componente -> %s" % componente.nome)
      atualiza_servidores(componente.list_serv, relogio)
      
