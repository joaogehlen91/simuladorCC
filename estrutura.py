# -*- coding: utf-8 -*-

from random import randint

class Componente:
  def __init__(self, nome, qtd_serv, list_serv, next, list_espera_entrada):
    self.nome                = nome
    self.qtd_serv            = qtd_serv
    self.list_serv           = list_serv
    self.next                = next
    self.list_espera_entrada = list_espera_entrada

class Servidor:
  def __init__(self, nome, ini, fim, ociosidade = 0, ult_saida = 0, atendimento = False, list_espera_entrada=[]):
    self.nome                = nome
    self.ini                 = ini
    self.fim                 = fim
    self.atendimento         = atendimento
    self.ult_saida           = ult_saida
    self.ociosidade          = ociosidade
    self.list_espera_entrada = list_espera_entrada

  def atividade(self):
    return randint(self.ini, self.fim)


class Roteador:
  def __init__(self, nome, dict_saidas, list_espera_entrada):
    self.nome                = nome
    self.dict_saidas         = dict_saidas
    self.list_espera_entrada = list_espera_entrada
