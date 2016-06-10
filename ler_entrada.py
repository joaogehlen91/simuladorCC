from definicoes import *

def abrir_arquivo(nome_arq):
   return open(nome_arq, 'r')

# --------------------------------------------------
####################################################
#   Controle dos Componentes C -                   #
####################################################

# Servidores dos Componentes 'C'
def criar_servidores(info):
   l = []
   for i in info:
      i    = i.strip(' ')
      valr = i[2:-1].split('-')
      nome = i[0]

      serv = criar_objeto(SERVIDOR, [nome, int(valr[0]), int(valr[1]), 0, 0, False])    
      l.append(serv)

   return (l, len(l))

# Funcao para imprimir a lista de componentes, preciso tornar generico
def imprimeC(lista):
   for i in lista:
      print("\nNome: %s, qtd serv: %d" % (i.nome, i.qtd_serv))
      for j in i.list_serv:
         print(" --  nome %s, Inicio %d, Fim %d" % (j.nome, j.ini, j.fim))

# --------------------------------------------------
####################################################
#   Controle dos Componentes Infinito -            #
####################################################

def componente_infinito(saida):
   pass

# --------------------------------------------------
####################################################
#   Controle dos Roteadores   R       -            #
####################################################

def config_roteadores(info):
   a = {}
   for i in info:
      i    = i.strip(' ')
      porc = float(i[1 : i.index('-')])
      cmpo = (i[i.index('-') + 1:-1]).strip(' ')

      a[cmpo] = porc
   return a



def ler_arquivo():
   arq  = abrir_arquivo("exemplo_4.in")   
   conf = []
   
   # Parte do arquivo
   for i in arq:
      if '*' in i: 
         break

      a = i.split(';')[:-1]
      if a != []: b = a[0].split(':')

      try:
         conf.append((b[0], b[1].split(',')))
      except:
         pass

   for i,j in conf:
      objeto = None
      if 'C' in i:
         #nome, qtd_serv, list_serv, saida, entrada, COMPONENTE
         objeto = criar_objeto(COMPONENTE, [i, criar_servidores(j)[1], criar_servidores(j)[0], None, None])
         imprime_componente(objeto)

      #nome, qtd_serv, list_serv, saida, entrada, INFINITO
      elif 'I' in i:
         objeto = criar_objeto(COMPONENTE, [i, 0, [], None, None])
         imprime_componente(objeto)         

      #nome, list_saidas, ROTEADOR
      elif 'R' in i:
         objeto = criar_objeto(ROTEADOR, [i, config_roteadores(j)])
         imprime_roteador(objeto)
         
      #Inserir nas listas de objetos
      if objeto != None: add_dict_componentes(objeto.nome, len(lista_objetos) - 1, objeto)
      
   
   
if __name__ == "__main__":
   ler_arquivo()
