import ler_entrada as le
import definicoes  as df

def zerarAtendimento(servs, num):
   servs[num].atendimento = False

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

   for x in range(0, tam):
     if servidores[x].atendimento == False:
       servidores[x].atendimento = True
       aux  = servidores[x].atividade()
       som  = etmp + aux
       comp.list_espera_entrada.pop(0)
       break
     else:
       cont+=1

   if cont == tam:   #Todos servidores ocupados
     for x in range(0, tam):
       if servidores[x].atendimento == True:
         servidores[x].list_espera_entrada.append(etmp)
         comp.list_espera_entrada.pop(0)
         break

   #zerarAtendimento(servidores, 0)

   print("Entrada -> %s" % etmp)
   print("Tempo -> %s" % aux)
   print("Saida -> %s \n"% som)
   return som


# A main ira fazer isso.
if __name__ == '__main__':
   le.ler_arquivo("exemplo_1.in")

   c = df.get_componente('C1')
   c.list_espera_entrada = [2,5,20,30]

   while(c.list_espera_entrada):
      multiplos_servidores('C1')
# A main ira fazer isso.
