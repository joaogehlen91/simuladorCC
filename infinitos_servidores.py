import ler_entrada as le
import definicoes  as df

def infinitos_servidores(nomeC):
   comp = df.get_componente(nomeC)
   etmp = comp.list_espera_entrada[0]
   serv = comp.list_serv[0] #Componente de infinitos servidores tem apenas 1 servidor.

   aux   = serv.atividade()
   som   = aux + etmp

   #Estatisticas - Tempo de atendimento e Qtd de ETS que passaram pelo componente
   serv.estatistica_servidor.incrementa_atendimento(aux)
   comp.estatistica_componente.qtd_et_passou += 1

   print("\n(INFINITOS SERVIDORES)\nEntrada -> %s" % etmp)
   print("Tempo -> %s" % aux)
   print("Saida -> %s "% som)
   return som