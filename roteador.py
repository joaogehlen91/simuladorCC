# -*- coding: utf-8 -*-

from estrutura import *
from random    import choice
import ler_entrada as le
import definicoes  as df

def calcula_porcentagem(dict):
   lista = ''
   itens = list(dict.items())

   for a in itens: lista += (a[0] + ' ') * int(a[1])

   lista = lista.split()
   return df.get_componente(choice(lista))


def roteador(origem):
   origem   = df.get_componente(origem)
   roteador = origem.next

   if roteador.__class__ is not Roteador: return

   destino = calcula_porcentagem(roteador.dict_saidas)
   print("Destino Roteador: %s\n" % destino.nome)
   return destino