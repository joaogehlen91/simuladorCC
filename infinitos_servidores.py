import ler_entrada as le
import definicoes  as df

def infinitos_servidores(nomeC):
   comp = df.get_componente(nomeC)
   serv = comp.list_serv[0] #Componente de infinitos servidores tem apenas 1 servidor.
   df.imprime_objetos()


if __name__ == '__main__':
   le.ler_arquivo("exemplo_4.in")
   infinitos_servidores('I1')
