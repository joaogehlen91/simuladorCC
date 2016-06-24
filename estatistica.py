import ler_entrada as le
import definicoes  as df

'''
   • Ociosidade das entidades permanentes, individualmente por servidor (exceto para centros de serviço com infinitos servidores). 
   • Ociosidade média por componente.
   • Ociosidade média geral de todos os componentes com servidores.
   • Tempo médio de espera das ETs na fila de cada componente;
   • Tempo médio de atendimento das entidades temporárias em cada componente;
   • Tempo médio de permanência, no modelo, das Ets.
   • Número médio de ETs na fila de cada componente que possui contenção.
'''

def atualiza_servidores(list_serv, relogio):
   for serv in list_serv:
      ocio = relogio - serv.ult_saida

      if ocio >= 0: 
         serv.ociosidade += 1
         print("Ult_Saida / Ociosidade    -> %d / %d" % (serv.ult_saida, serv.ociosidade))

def atualiza_estatisticas(componente, relogio):
   if 'C' in componente.nome:
      print("Componente -> %s" % componente.nome)
      atualiza_servidores(componente.list_serv, relogio)
      
         

         



if __name__ == '__main__':
   le.ler_arquivo("exemplo_4.in")
   df.imprime_objetos()
   atualiza_estatisticas()