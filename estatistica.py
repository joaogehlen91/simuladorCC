# -*- coding: utf-8 -*-

import ler_entrada as le
import definicoes  as df

'''
   (1) x Ociosidade das entidades permanentes, individualmente por servidor (exceto para centros de serviço com infinitos servidores).
   (2) x Ociosidade média por componente.
   (3) x Ociosidade média geral de todos os componentes com servidores.
   (4) x Tempo médio de espera das ETs na fila de cada componente;
   (5) x Tempo médio de atendimento das entidades temporárias em cada componente;
   (6) x Tempo médio de permanência, no modelo, das Ets.
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

      if len(x.list_serv) > 0:
        arq.write("                     Ociosidade Média  ---> %0.2f\n" % float(sum([serv.ociosidade for serv in x.list_serv]) / len(x.list_serv)))
   return


#Ociosidade média geral de todos os componentes com servidores.
def calcula_3():
   lst = df.get_todos_componentes_por_nome('C')
   arq.write("\n\n*** 3) Ociosidade média geral de todos os componentes com servidores. ***\n")
   soma = 0

   for comp in lst:
      soma += sum([x.ociosidade for x in comp.list_serv])

   arq.write("                     Ociosidade Média Geral ---> %0.2f\n" % (0 if len(lst) <= 0 else float(soma / len(lst))))
   return


#Tempo médio de espera das ETs na fila de cada componente;
def calcula_4():
    lst = df.get_todos_componentes_por_nome('C')

    arq.write("\n\n*** 4) Tempo médio de espera das ETs na fila de cada componente. ***\n")

    for cmp in lst:
       arq.write("\n             ---------------- COMPONENTE %s ----------------\n" % cmp.nome)
       soma = sum([x.estatistica_servidor.total_espera for x in cmp.list_serv])

       if len(cmp.list_serv) > 0:
         arq.write("                     Media do tempo de espera  ---> %0.2f\n" % float(soma / len(cmp.list_serv)))
    return


#Tempo médio de atendimento das entidades temporárias em cada componente;
def calcula_5():
  lst = df.get_todos_componentes_por_nome('C') + df.get_todos_componentes_por_nome('I')
  arq.write("\n\n*** 5) Tempo médio de atendimento das entidades temporárias em cada componente. ***\n")

  for cmp in lst:
      arq.write("\n             ---------------- COMPONENTE %s ----------------\n" % cmp.nome)
      soma = sum([x.estatistica_servidor.total_atendimento for x in cmp.list_serv])
      arq.write("                   Qtd de ET que passou pelo componente ---> %d\n" % (cmp.estatistica_componente.qtd_et_passou))

      if cmp.estatistica_componente.qtd_et_passou > 0:
        arq.write("                   Media do tempo de atendimento        ---> %0.2f\n" % float(soma / cmp.estatistica_componente.qtd_et_passou))
  return


#Tempo médio de permanência, no modelo, das Ets.
def calcula_6(entradaC):
  s = df.get_componente('S')
  arq.write("\n\n*** 6) Tempo médio de permanência, no modelo, das Ets.. ***\n")
  print("Entrada -> %s" % entradaC)
  print("Saida   -> %s" % s.list_espera_entrada)
  print("Media Total      %d" % (s.list_espera_entrada[-1:][0] - entradaC[0]))

  arq.write("                   Media de permanência        ---> %0.2f\n" % (s.list_espera_entrada[-1:][0] - entradaC[0]))
  return


#Número médio de ETs na fila de cada componente que possui contenção.
def calcula_7():
  lst = df.get_todos_componentes_por_nome('C')
  arq.write("\n\n*** 7) Número médio de ETs na fila de cada componente que possui contenção.. ***\n")

  for cmp in lst:
      arq.write("\n             ---------------- COMPONENTE %s ----------------\n" % cmp.nome)
      media_das_somas = 0
      soma_ocorrencia = sum([x.estatistica_servidor.total_ocorreu_fila for x in cmp.list_serv])
      soma_total_fila = sum([x.estatistica_servidor.total_tamanho_fila for x in cmp.list_serv])

      if soma_ocorrencia > 0:
        media_das_somas = float(soma_total_fila / soma_ocorrencia)

      arq.write("                   Total de vezes que ocorreu fila        ---> %0.2f\n" % soma_ocorrencia)
      arq.write("                   Média de ETs nas filas                 ---> %0.2f\n" % media_das_somas)
  return


def gera_resultados(entradaC):
   calcula_1()
   calcula_2()
   calcula_3()
   calcula_4()
   calcula_5()
   calcula_6(entradaC)
   calcula_7()

   arq.close()
   return


def atualiza_servidores(list_serv, relogio):
  for serv in list_serv:
    if (relogio - serv.ult_saida) > 0:
      serv.ociosidade += 1

      print("Ult_Saida / Ociosidade    -> %d / %d" % (serv.ult_saida, serv.ociosidade))
  print("\n")


def atualiza_estatisticas(componente, relogio):
   if 'C' in componente.nome:
      print("Componente -> %s" % componente.nome)
      atualiza_servidores(componente.list_serv, relogio)
