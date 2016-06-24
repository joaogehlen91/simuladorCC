from os            import system
import ler_entrada as le
import definicoes  as df

'''
   (1) Ociosidade das entidades permanentes, individualmente por servidor (exceto para centros de serviço com infinitos servidores). 
   (2) Ociosidade média por componente.
   (3) Ociosidade média geral de todos os componentes com servidores.
   (4) Tempo médio de espera das ETs na fila de cada componente;
   (5) Tempo médio de atendimento das entidades temporárias em cada componente;
   (6) Tempo médio de permanência, no modelo, das Ets.
   (7) Número médio de ETs na fila de cada componente que possui contenção.
'''

dict_estatisticas = {}

def calcula_1():
   lst = df.get_todos_componentes()

   

   
   pass


def calcula_2():
   print("\n------------------------------------\n")
   for x in lst:
      print(x.nome)
      print(sum([serv.ociosidade for serv in x.list_serv]))
      print(sum([serv.ociosidade for serv in x.list_serv]) / len(x.list_serv))   
   print("\n------------------------------------\n")
   pass



def calcula_3():
   pass



def gera_resultados():
   #system("clear")
   
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
      
