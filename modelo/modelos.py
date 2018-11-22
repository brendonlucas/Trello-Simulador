class Quadro:
    def __init__(self):
        self.quadro_atual = []
        self.cartao_atual = []
        self.quadros = []
        self.quadros_disponiveis = []
        self.logs = []

    def criar_quadro(self, titulo):  # cria um novo quadro
        self.quadros.append([titulo])
        acao = "Adicionou um novo quadro de titulo " + titulo
        self.logs.append(acao)
        return True

    def criar_lista(self, titulo):  # cria uma nova lista em um quadro
        self.quadro_atual.append([titulo])
        acao = "Adicionou uma nova lista com o titulo " + titulo
        self.logs.append(acao)
        return True

    def adicionar_cartao(self, lista_selecionada, titulo, descricao):  # adiciona um novo cartão a uma lista
        for i in range(1, len(self.quadro_atual)):
            lista_atual = self.quadro_atual[i][0]
            if lista_atual == lista_selecionada:
                self.quadro_atual[i].append([titulo, descricao])
                acao = "Adicionou um cartão com titulo " + titulo
                self.logs.append(acao)
                return True

    def seleciona_quadro(self, quadro_solicitado):  # Faz a selecão do quadroatual para fazer mudanças
        for i in range(len(self.quadros)):
            quadro_atual = self.quadros[i][0]
            if quadro_atual == quadro_solicitado:
                self.quadro_atual = self.quadros[i]
                return True
        return False

    def adicionar_etiqueta(self, lista, cartao, etiqueta):  # adicona uma etiqueta a um cartão
        self.retorna_cartao_atual(lista, cartao)
        if self.cartao_atual[0] == cartao:
            self.cartao_atual.append(etiqueta)
            acao = "Adicionou uma etiqueta ao cartão " + cartao + " da lista " + lista
            self.logs.append(acao)
            return True

    def exibir_quadros(self):  # Exibe os quadros criados
        self.quadros_disponiveis = []
        for i in range(len(self.quadros)):
            quadro_atual = self.quadros[i][0]
            self.quadros_disponiveis.append(quadro_atual)
        return self.quadros_disponiveis

    def exibir_listas(self):  # Exibe as listas
        return self.quadro_atual

    def remove_quadro(self, quadro_selecionado):  # Remove um quadro
        for i in range(len(self.quadros)):
            quadro_atual = self.quadros[i]
            if quadro_atual[0] == quadro_selecionado:
                del self.quadros[i]
                acao = "removeu o quadro " + quadro_selecionado
                self.logs.append(acao)
                return True

    def remover_cartao(self, lista, nome_cartao):  # Remove um cartão
        local = self.retorna_cartao_atual(lista, nome_cartao)
        del self.quadro_atual[local[0]][local[1]]
        acao = "removeu o cartão " + nome_cartao
        self.logs.append(acao)

    def retorna_cartao_atual(self, lista, nome_cartao):  # Faz adefinicao de um cartao atual para auxilio
        for i in range(1, len(self.quadro_atual)):
            lista_atual = self.quadro_atual[i]
            if lista_atual[0] == lista:
                for k in range(1, len(lista_atual)):
                    self.cartao_atual = lista_atual[k]
                    if self.cartao_atual[0] == nome_cartao:
                        return i, k

    def mover_cartao_de_lista(self, lista_primaria, nome_cartao, lista_destino):  # Move cartão de uma lista para outra
        for i in range(1, len(self.quadro_atual)):
            lista_atual = self.quadro_atual[i]
            if lista_atual[0] == lista_primaria:
                for k in range(1, len(lista_atual)):
                    self.cartao_atual = lista_atual[k]
                    if self.cartao_atual[0] == nome_cartao:
                        copia_cartao = [] + self.cartao_atual
                        del self.quadro_atual[i][k]
                        for l in range(1, len(self.quadro_atual)):
                            lista_atual = self.quadro_atual[l][0]
                            if lista_atual == lista_destino:
                                self.quadro_atual[l].append(copia_cartao)
                                acao = "Moveu " + nome_cartao + " da lista " + lista_primaria + " para a lista " + \
                                       lista_destino
                                self.logs.append(acao)

    def exibir_log(self):  # Exibe os logs
        return self.logs
