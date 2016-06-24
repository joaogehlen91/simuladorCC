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
global ROTEADOR, COMPONENTE, SERVIDOR, ENTRADA, SAIDA, TS, TC

TS, TC, dict_componentes , lista_objetos       = 0, (1,1), {}, []
ROTEADOR, COMPONENTE, SERVIDOR, ENTRADA, SAIDA = 0, 1, 2, 3, 4

def criar_objeto(opcao, param):
   c = None

   #nome, qtd_serv, list_serv, next, list_espera_entrada
   if opcao == ENTRADA or opcao == SAIDA:
      c = Componente(param[0], param[1], param[2], param[3], param[4])

   #nome, qtd_serv, list_serv, next, list_espera_entrada
   if opcao == COMPONENTE:
      c = Componente(param[0], param[1], param[2], param[3], param[4])

   #nome, ini, fim, ociosidade, ult_saida, atendimento, list_espera_entrada
   if opcao == SERVIDOR:
      c = Servidor(param[0], param[1], param[2], param[3], param[4], param[5], param[6])

   #nome, dict_saidas, list_espera_entrada
   if opcao == ROTEADOR:
      c = Roteador(param[0], param[1], param[2])

   return c

def add_objeto(nome, objeto):
   lista_objetos.append(objeto)
   indice = len(lista_objetos) - 1 if lista_objetos != [] else 0
   dict_componentes[nome] = indice


def imprime_objetos():
   print("\n     --------------- TS \ TC ---------------")
   print('   | TS -> %d' % TS)
   print('   | TC -> %s' % str(TC))

   for i in lista_objetos:
      if i.__class__ is Roteador:
         imprime_roteador(i)

      if i.__class__ is Componente:
         imprime_componente(i)
         for j in i.list_serv:
            if j.__class__ is Servidor:
               imprime_servidor(j, i.nome)
   pass


def imprime_servidor(serv, nome_componente):
   print("\n --------------- SERVIDOR - Componente %s ---------------" % nome_componente)
   print("   | Nome        -> %s" % (serv.nome))
   print("   | Serv Ini    -> %d" % (serv.ini))
   print("   | Serv Fim    -> %d" % (serv.fim))
   print("   | Atendimento -> %d" % (serv.atendimento))
   print("   | Ult Saida   -> %d" % (serv.ult_saida))
   print("   | Ociosidade  -> %d" % (serv.ociosidade))
   print("   | Espera      -> %s" % (serv.list_espera_entrada))


def imprime_componente(comp):
   print("\n --------------- COMPONENTE ---------------")
   print("   | Nome     -> %s" % (comp.nome))
   print("   | Qtd_Serv -> %d" % (comp.qtd_serv))
   print("   | Lst_Serv -> %s" % ([i.nome for i in comp.list_serv]))
   print("   | Next     -> %s" % ('' if comp.next == None else comp.next.nome))
   print("   | Espera   -> %s" % comp.list_espera_entrada)

def imprime_roteador(rot):
   print("\n --------------- ROTEADOR ---------------")
   print("   | Nome        -> %s" % (rot.nome))
   print("   | dict_saidas -> %s" % (rot.dict_saidas))
   print("   | Espera      -> %s" % rot.list_espera_entrada)


def get_todos_componentes():
   l = []
   for i in lista_objetos:
      if 'C' in i.nome:
         l.append(i)
   return l


def get_componente(nome):
   try:
      a = lista_objetos[dict_componentes[nome]]
   except:
      return None
   return a

