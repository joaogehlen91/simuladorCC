from estrutura  import *
from definicoes import *

def abrir_arquivo(nome_arq):
   return open(nome_arq, 'r')

# --------------------------------------------------
####################################################
#   Controle dos Componentes C - Inicio            #
####################################################

def criar_componente(nome):
   c = Componente(nome, 0, [], None, None)
   return c

# Servidores dos Componentes 'C'
def criar_servidores(info):
   l = []
   for i in info:
      i    = i.strip(' ')
      valr = i[2:-1].split('-')
      nome = i[0]
      
      l.append(Servidor(nome, int(valr[0]), int(valr[1]), 0, 0))
   return (l, len(l))

# Funcao para imprimir a lista de componentes, preciso tornar generico
def imprimeC(lista):
   for i in lista:
      print("\nNome: %s, qtd serv: %d" % (i.nome, i.qtd_serv))
      for j in i.list_serv:
         print(" --  Id_Serv %s, Inicio %d, Fim %d" % (j.id_serv, j.ini, j.fim))

# --------------------------------------------------
####################################################
#   Controle dos Componentes Infinito - Inicio     #
####################################################

def componente_infinito():
   pass


def ler_arquivo():
   arq  = abrir_arquivo("exemplo_4.in")   
   conf = []
   
   # Parte do arquivo
   for i in arq:
      if '*' in i: break

      a = i.split(';')[:-1]
      if a != []: b = a[0].split(':')

      try:
         conf.append((b[0], b[1].split(',')))
      except:
         pass
        	
   # Cria componentes 'C'
   for i,j in conf:
      if 'C' in i:
         componente = criar_componente(i)
         componente.list_serv, componente.qtd_serv = criar_servidores(j)
         lista_componentes.append(componente)
         add_dict_componentes(componente.nome, len(lista_componentes) - 1)
      elif 'I' in i:
         componente = criar_componente(i)
         componente_infinito()
         lista_componentes.append(componente)
         add_dict_componentes(componente.nome, len(lista_componentes) - 1)
         print(i)


   # Imprime componentes 'C'
   imprimeC(lista_componentes) 
   
if __name__ == "__main__":
   ler_arquivo()
