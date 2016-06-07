from estrutura import *

def abrir_arquivo(nome_arq):
   return open(nome_arq, 'r')

# Componentes 'C'
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
   return l

# Funcao para imprimir a lista de componentes, preciso tornar generico
def imprimeC(lista):
   for i in lista:
      print("Nome %s" % (i.nome))
      for j in i.list_serv:
         print(" --  Id_Serv %s, Inicio %d, Fim %d" % (j.id_serv, j.ini, j.fim))
   
   
def ler_arquivo():
   arq  = abrir_arquivo("exemplo_4.in")   
   conf = []
   comp = []
   
   # Parte do arquivo
   for i in arq:
      if '*' in i: break

      a = i.split(';')[:-1]
      if a != []: 
         b = a[0].split(':')

      try:
         conf.append((b[0], b[1].split(',')))
      except:
         pass
        	
   # Cria componentes 'C'
   for i,j in conf:
      if 'C' in i:
         componente = criar_componente(i)
         componente.list_serv = criar_servidores(j)
         comp.append(componente)
         
   # Imprime componentes 'C'
   imprimeC(comp)
         
   
if __name__ == "__main__":
   ler_arquivo()
