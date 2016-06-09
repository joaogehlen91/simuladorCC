# --------------------------------------------------
# Arquivo com definicoes globais e funcoes uteis

# A dict_componentes eh um dicionario chave:valor
# onde a chave eh o nome do componente e o valor
# eh o indice do componente no vetor global de
# componentes.

# Ex: Para buscar componente 'C2', basta chamar
# a funcao get_componente('C2'), que ira
# retornar o objeto componente C2 se existir.

global dict_componentes, lista_componentes
dict_componentes  = {}
lista_componentes = []

def add_dict_componentes(nome, indice):
   dict_componentes[nome] = indice
   print(dict_componentes)
   pass

# TODO: Verificar se nao existe
def get_componente(nome):
   return lista_componentes[dict_componentes[nome]]   