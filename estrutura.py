class Componente:
	def __init__(self, nome, qtd_serv, list_serv, saida, entrada):
		self.nome = nome
		self.qtd_serv = qtd_serv
		self.list_serv = list_serv
		self.saida = saida
		self.entrada = entrada


class Servidor:
	def __init__(self, id_serv, ini, fim, ociosidade=0):
		self.id_serv = id_serv
		self.ini = ini
		self.fim = fim
		self.ociosidade = ociosidade
	def atividade(self):
		return 10
		# tempo = random(ini, fim)
		
		


class Roteador:
	def __init__(self, nome, list_saidas):
		self.nome = nome
		self.list_saidas = list_saidas
