import ler_entrada as le
import definicoes  as df

def infinitos_servidores(nomeC):
   comp = df.get_componente(nomeC)
   etmp = comp.list_espera_entrada[0]
   serv = comp.list_serv[0] #Componente de infinitos servidores tem apenas 1 servidor.

   aux   = serv.atividade()
   som   = aux + etmp

   print("Entrada -> %s" % etmp)
   print("Tempo -> %s" % aux)
   print("Saida -> %s "% som)
   return som


# A main ira fazer isso.
if __name__ == '__main__':
   le.ler_arquivo("exemplo_4.in")

   c = df.get_componente('I1')
   c.list_espera_entrada = [2]

   infinitos_servidores('I1')
# A main ira fazer isso.
