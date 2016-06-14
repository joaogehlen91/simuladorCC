# --------------------------------------------------
# Arquivo com definicoes globais e funcoes uteis

# A dict_componentes eh um dicionario chave:valor
# onde a chave eh o nome do componente e o valor
# eh o indice do componente no vetor global de
# componentes.

# Ex: Para buscar componente 'C2', basta chamar
# a funcao get_componente('C2'), que ira
# retornar o objeto componente C2 se existir.

from estrutura  import *

global dict_componentes, lista_objetos
global ROTEADOR, COMPONENTE, SERVIDOR, ENTRADA, SAIDA

dict_componentes , lista_objetos           = {}, []
ROTEADOR, COMPONENTE, SERVIDOR, ENTRADA, SAIDA = 0, 1, 2, 3, 4

def criar_objeto(opcao, param):
   c = None

   #nome, qtd_serv, list_serv, saida, entrada
   if opcao == ENTRADA or opcao == SAIDA:
      c = Componente(param[0], param[1], param[2], param[3])

   #nome, qtd_serv, list_serv, saida, entrada
   if opcao == COMPONENTE:
      c = Componente(param[0], param[1], param[2], param[3])

   #nome, ini, fim, ociosidade, ult_saida, atendimento
   if opcao == SERVIDOR:
      c = Servidor(param[0], param[1], param[2], param[3], param[4], param[5])

   #nome, list_saidas
   if opcao == ROTEADOR:
      c = Roteador(param[0], param[1])


   return c

def add_objeto(nome, objeto):
   lista_objetos.append(objeto)
   indice = len(lista_objetos) - 1 if lista_objetos != [] else 0
   dict_componentes[nome] = indice
   #print(dict_componentes)


def imprime_componente(comp):
   if comp.next != None:
      a = comp.next.nome
   else:
      a = ''

   print("\n --------------- COMPONENTE ---------------")
   print("   | Nome     -> %s" % (comp.nome))
   print("   | Qtd_Serv -> %d" % (comp.qtd_serv))
   print("   | Lst_Serv -> %s" % ([i.nome for i in comp.list_serv]))
   print("   | Saida    -> %s" % (a))

def imprime_roteador(rot):
   print("\n --------------- ROTEADOR ---------------")
   print("   | Nome       -> %s" % (rot.nome))
   print("   | Lst_Saidas -> %s" % (rot.dict_saidas))

def get_componente(nome):
   try:
      a = lista_objetos[dict_componentes[nome]]
   except:
      return None

   return a