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
#   Controle dos Componentes Entrada\Saida         #
####################################################

def criar_entrada_saida():
   #nome, qtd_serv, list_serv, saida, entrada
   objeto = criar_objeto(ENTRADA, ['E', 0, [], None, None])
   add_objeto(objeto.nome, objeto)

   objeto = criar_objeto(SAIDA, ['S', 0, [], None, None])
   add_objeto(objeto.nome, objeto)


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


def cria_todos_objetos(conf):
   criar_entrada_saida()

   for i,j in conf:
      objeto = None

      if 'C' in i:
         #nome, qtd_serv, list_serv, saida, entrada, COMPONENTE
         objeto = criar_objeto(COMPONENTE, [i, criar_servidores(j)[1], criar_servidores(j)[0], None, None])
         #imprime_componente(objeto)

      #nome, qtd_serv, list_serv, saida, entrada, INFINITO
      elif 'I' in i:
         objeto = criar_objeto(COMPONENTE, [i, 0, [], None, None])
         #imprime_componente(objeto)         

      #nome, list_saidas, ROTEADOR
      elif 'R' in i:
         objeto = criar_objeto(ROTEADOR, [i, config_roteadores(j)])
         #imprime_roteador(objeto)
         
      #Inserir nas listas de objetos
      if objeto != None: add_objeto(objeto.nome, objeto)
   pass


def conf_objeto(info):
   obj_saida = get_componente(info[0])
   outro_obj = []

   for i in info[1:]:
      if ',' in i:
         i = i.split(',')
         for j in i:
            print("%s -> %s" % (info[0], j))
      else:
         print("%s -> %s" % (info[0], i))
      #outro_obj.append(i)


      #print("I -> %s" % i)
   

   #print(obj_saida.nome, outro_obj)
   




def configura_objetos(conf):
   for i in conf:
      if '->' in i:
         i = ((i.strip('\n')).strip(';')).split('->')
         conf_objeto(i)      
   pass



def ler_arquivo(arquivo):
   arq  = abrir_arquivo(arquivo)   
   lit  = arq.readlines()
   cnf  = []
   obj  = []
   
   # Parte do arquivo
   for i in lit:
      if '*' in i:
         cnf = lit[lit.index(i) + 2:]
         break

      a = i.split(';')[:-1]
      if a != []: b = a[0].split(':')

      try:
         obj.append((b[0], b[1].split(',')))
      except:
         pass

   cria_todos_objetos(obj)
   configura_objetos(cnf)

   
if __name__ == "__main__":
   ler_arquivo("exemplo_4.in")
