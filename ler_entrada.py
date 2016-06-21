import definicoes as df

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

      #nome, ini, fim, ociosidade, ult_saida, atendimento, list_espera_entrada
      serv = df.criar_objeto(df.SERVIDOR, [nome, int(valr[0]), int(valr[1]), 0, 0, False, []])
      l.append(serv)

   return (l, len(l))


# --------------------------------------------------
####################################################
#   Controle dos Componentes Entrada\Saida         #
####################################################

def criar_entrada_saida():
   #nome, qtd_serv, list_serv, next, list_espera_entrada
   objeto = df.criar_objeto(df.ENTRADA, ['E', 0, [], None, []])
   df.add_objeto(objeto.nome, objeto)

   objeto = df.criar_objeto(df.SAIDA, ['S', 0, [], None, []])
   df.add_objeto(objeto.nome, objeto)


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
         #nome, qtd_serv, list_serv, next, list_espera_entrada
         objeto = df.criar_objeto(df.COMPONENTE, [i, criar_servidores(j)[1], criar_servidores(j)[0], None, []])

      #nome, qtd_serv, list_serv, next, list_espera_entrada
      elif 'I' in i:
         objeto = df.criar_objeto(df.COMPONENTE, [i, criar_servidores(j)[1], criar_servidores(j)[0], None, []])

      #nome, dict_saidas, list_espera_entrada
      elif 'R' in i:
         objeto = df.criar_objeto(df.ROTEADOR, [i, config_roteadores(j), []])

      #Inserir nas listas de objetos
      if objeto != None: df.add_objeto(objeto.nome, objeto)
   pass


def conf_objeto(info):
   obj_saida    = None
   obj_original = df.get_componente(info[0])

   for i in info[1:]:
      if ',' in i:
         i = i.split(',')
         for j in i:
            obj_original.next = df.get_componente(j)
      else:
         obj_original.next = df.get_componente(i)


def configura_objetos(conf):
   for i in conf:
      if 'TS' in i:
         df.TS = int(i.strip('\n').strip(';').split('=')[1])

      elif 'TC' in i:
         i = i[i.index(':') +1 :].strip('\n')
         df.TC = (int(i.split(',')[0]), int(i.split(',')[1]))

      elif '->' in i:
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

      if a != []:
         b = a[0].split(':')

         try:
            obj.append((b[0], b[1].split(',')))
         except:
            pass

   cria_todos_objetos(obj)
   configura_objetos(cnf)


if __name__ == "__main__":
   ler_arquivo("exemplo_4.in")
