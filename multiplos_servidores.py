# -*- coding: utf-8 -*-

import ler_entrada as le
import definicoes  as df

def multiplos_servidores(nomeC):
   comp = df.get_componente(nomeC)
   etmp = comp.list_espera_entrada[0]

   servidores = []
   for i in comp.list_serv:
     servidores.append(i)

   cont, aux, som = 0, 0, 0
   tam = len(servidores)
   ult_saida_menor = 9999999999999

   for x in range(0, tam):
     if servidores[x].ult_saida < etmp or servidores[x].atendimento == False: # Nao esta em atendimento (Algum servidor Livre Servidor)
       servidores[x].atendimento = True
       aux  = servidores[x].atividade()

       #Estatistica - Tempo de atendimento
       serv_atualizado = comp.list_serv[x]
       comp.estatistica_componente.qtd_et_passou += 1
       serv_atualizado.estatistica_servidor.incrementa_atendimento(aux)

       som  = etmp + aux
       servidores[x].ult_saida = som
       serv = x
       break
     else:
       cont+=1

   if cont == tam: # Servidores ocupados
     for x in range(0, tam): # Procurar o menor tempo de saida
       if servidores[x].ult_saida < ult_saida_menor:
         ult_saida_menor = servidores[x].ult_saida
         serv = x

     if ult_saida_menor >= etmp and servidores[serv].atendimento == True: # Esta em atendimento (Todos servidores ocupados no momento)
       aux = servidores[serv].atividade()
       som = ult_saida_menor + aux
       servidores[serv].ult_saida = som

       serv_atualizado = comp.list_serv[serv]

       #Estatistica - Tempo de atendimento do servidor
       serv_atualizado.estatistica_servidor.incrementa_atendimento(aux)
       
       if ult_saida_menor - etmp > 0:
         #Estatisticas - Tempo de espera das ET do servidor
         serv_atualizado.estatistica_servidor.incrementa_espera(ult_saida_menor - etmp)

       #Estatisticas - Total de ETs na fila do servidor
       serv_atualizado.estatistica_servidor.total_ocorreu_fila += 1

       #Estatistica - Qtd de ETs no componente
       comp.estatistica_componente.qtd_et_passou += 1

       #Estatistica - Total de vezes que ocorreu fila
       servidores[serv].list_espera_entrada.append(etmp)

       #Estatistica - Total de ET nas vezes que ocorreram fila
       servidores[serv].estatistica_servidor.incrementa_tamanho_fila(len(servidores[serv].list_espera_entrada))


   print("\nComponente -> %s" % nomeC)
   print("Servidor -> %s "% serv)
   print("Entrada -> %s" % etmp)
   print("Tempo -> %s" % aux)
   print("Saida -> %s \n"% som)

   return som