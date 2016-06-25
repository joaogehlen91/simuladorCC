# -*- coding: utf-8 -*-

from random import randint

class Componente:
  def __init__(self, nome, qtd_serv, list_serv, next, list_espera_entrada, estat_componente = None):
    self.nome                   = nome
    self.qtd_serv               = qtd_serv
    self.list_serv              = list_serv
    self.next                   = next
    self.list_espera_entrada    = list_espera_entrada
    self.estatistica_componente = estat_componente

class Servidor:
  def __init__(self, nome, ini, fim, ociosidade = 0, ult_saida = 0, atendimento = False, list_espera_entrada = [], estat_serv = None):
    self.nome                   = nome
    self.ini                    = ini
    self.fim                    = fim
    self.atendimento            = atendimento
    self.ult_saida              = ult_saida
    self.ociosidade             = ociosidade
    self.list_espera_entrada    = list_espera_entrada
    self.estatistica_servidor   = estat_serv

  def atividade(self):
    return randint(self.ini, self.fim)

class Roteador:
  def __init__(self, nome, dict_saidas, list_espera_entrada):
    self.nome                = nome
    self.dict_saidas         = dict_saidas
    self.list_espera_entrada = list_espera_entrada


#Classes com outras estatistícas além da ociosidade. Uteis para itens (4), (5), (6) e (7)
class Estatistica_Componente:
  def __init__(self, nome_componente):
    self.nome_componente            = nome_componente

class Estatistica_Servidor:
  def __init__(self, nome_servidor, total_espera = 0, total_atendimento = 0):
    self.nome_servidor      = nome_servidor
    self.total_espera       = total_espera
    self.total_atendimento  = total_atendimento

  def incrementa_espera(self, espera):
    self.total_espera += espera

  def incrementa_atendimento(self, atendimento):
    self.total_atendimento += atendimento