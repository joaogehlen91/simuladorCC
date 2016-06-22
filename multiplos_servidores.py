import ler_entrada as le
import definicoes  as df

def multiplos_servidores(nomeC):
   comp = df.get_componente(nomeC)
   etmp = comp.list_espera_entrada[0]

   servidores = []
   for i in comp.list_serv:
     servidores.append(i)

   cont = 0
   aux = 0
   som = 0
   tam = len(servidores)
   ult_saida_menor = 9999999999999

   for x in range(0, tam):
     if servidores[x].ult_saida < etmp or servidores[x].atendimento == False: # Nao esta em atendimento (Algum servidor Livre Servidor)
       servidores[x].atendimento = True
       aux  = servidores[x].atividade()
       som  = etmp + aux
       comp.list_espera_entrada.pop(0)
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

       servidores[serv].list_espera_entrada.append(etmp)
       comp.list_espera_entrada.pop(0)

   print("Servidor -> %s "% serv)
   print("Entrada -> %s" % etmp)
   print("Tempo -> %s" % aux)
   print("Saida -> %s \n"% som)

   return som

# A main ira fazer isso.
if __name__ == '__main__':
   le.ler_arquivo("exemplo_1.in")

   relogio = 0
   c = df.get_componente('C1')
   c.list_espera_entrada = []

   while relogio < 500:
      if relogio == 2:
         c.list_espera_entrada.append(2)
         multiplos_servidores('C1')

      if relogio == 5:
         c.list_espera_entrada.append(5)
         multiplos_servidores('C1')

      if relogio == 20:
         c.list_espera_entrada.append(20)
         multiplos_servidores('C1')

      if relogio == 35:
         c.list_espera_entrada.append(35)
         multiplos_servidores('C1')

      if relogio == 40:
         c.list_espera_entrada.append(40)
         multiplos_servidores('C1')

      relogio += 1

# A main ira fazer isso.
