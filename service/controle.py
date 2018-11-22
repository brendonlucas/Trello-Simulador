from modelo.modelos import *


class Controle:
    def __init__(self):
        self.quadro = Quadro()

    def criar_quadro(self, titulo):
        self.quadro.criar_quadro(titulo)

    def seleciona_quadro(self, quadro_solicitado):
        return self.quadro.seleciona_quadro(quadro_solicitado)

    def criar_lista(self, titulo):
        self.quadro.criar_lista(titulo)

    def adicionar_cartao(self, lista_selecionada, titulo, descricao):
        self.quadro.adicionar_cartao(lista_selecionada, titulo, descricao)

    def adicionar_etiqueta(self, lista, cartao, etiqueta):
        self.quadro.adicionar_etiqueta(lista, cartao, etiqueta)

    def remove_quadro(self, quadro_selecionado):
        self.quadro.remove_quadro(quadro_selecionado)

    def mover_cartao_de_lista(self, lista_primaria, nome_cartao, lista_destino):
        self.quadro.mover_cartao_de_lista(lista_primaria, nome_cartao, lista_destino)

    def remover_cartao(self, lista, nome_quadro):
        self.quadro.remover_cartao(lista, nome_quadro)

    def exibir_listas(self):
        return self.quadro.exibir_listas()

    def exibir_quadros(self):
        return self.quadro.exibir_quadros()

    def registros(self):
        return self.quadro.exibir_log()
