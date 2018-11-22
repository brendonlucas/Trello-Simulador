from service.controle import *


def main():
    opcao = -1
    contole_trello = Controle()
    logo = " _____   _____    _____   _       _       _____   _       _____   _       _____\n" \
           "|_   _| |  _  \  | ____| | |     | |     /  _  \ | |     | ____| | |     /  _  \ \n" \
           "  | |   | |_| |  | |__   | |     | |     | | | | | |     | |__   | |     | | | | \n" \
           "  | |   |  _  /  |  __|  | |     | |     | | | | | |     |  __|  | |     | | | | \n" \
           "  | |   | | \ \  | |___  | |___  | |___  | |_| | | |___  | |___  | |___  | |_| | \n" \
           "  |_|   |_|  \_\ |_____| |_____| |_____| \_____/ |_____| |_____| |_____| \_____/ \n"
    menu_painel = "1 - Criar quadro: \n" \
                  "2 - Selecionar quadro:\n" \
                  "3 - listar quadros:\n" \
                  "4 - apagar quadro:\n" \
                  "5 - exibir logs:\n" \
                  "0 - sair:\n" \
                  "-> "
    while opcao != 0:
        print(logo)
        opcao = int(input(menu_painel))

        if opcao == 1:
            titulo_quadro = input("Digite o titulo do quadro: ")
            contole_trello.criar_quadro(titulo_quadro)
            print()

        if opcao == 2:
            seleciona_quadro = input("Digite o nome do quadro para entrar: ")
            escolhe = contole_trello.seleciona_quadro(seleciona_quadro)
            if escolhe:
                escolha = -1
                print("Quadro selecionado :) \n")
                while escolha != 0:
                    menu_quadro = "1 - Add lista:\n" \
                                  "2 - Adicionar cartão a uma lista:\n" \
                                  "3 - Adicionar etiqueta a um cartão:\n" \
                                  "4 - Listar listas com seus cartões:\n" \
                                  "5 - Mover cartao de uma lista para outra:\n" \
                                  "6 - Remover um cartão:\n" \
                                  "7 - Exibir logs:\n" \
                                  "0 - Voltar:\n" \
                                  "-> "
                    escolha = int(input(menu_quadro))

                    if escolha == 1:
                        titulo_lista = input("Digite o titulo da lista: ")
                        contole_trello.criar_lista(titulo_lista)
                        print()

                    if escolha == 2:
                        select_lista = input("Digite a lista que queira adicionar um cartao: ")
                        nome_cartao = input("Digite o titulo do cartao: ")
                        descricao = input("Digite a descriçao: ")
                        contole_trello.adicionar_cartao(select_lista, nome_cartao, descricao)
                        print()

                    if escolha == 3:
                        lista = input("Digite em qual lista esta o cartao: ")
                        cartao_selecionado = input("Digite o titulo do cartao: ")
                        etiqueta = input("Digite a etiqueta: ")
                        contole_trello.adicionar_etiqueta(lista, cartao_selecionado, etiqueta)
                        print()

                    if escolha == 4:
                        listas = contole_trello.exibir_listas()
                        for i in range(1, len(listas)):
                            lista_atual = listas[i]
                            print(">> " + lista_atual[0])
                            if len(lista_atual) > 1:
                                for k in range(1, len(lista_atual)):
                                    cartao = lista_atual[k]
                                    print("   > " + cartao[0])
                                    print("    Descrição: " + cartao[1])
                                    if len(cartao) > 2:
                                        for j in range(2, len(cartao)):
                                            print("      Etiqueta > " + cartao[j])
                                print("")
                        print()

                    if escolha == 5:
                        lista_primaria = input("Digite a lista em que esta o quadro: ")
                        nome_cartao = input("Digite o nome do cartão: ")
                        lista_destino = input("Digite para onde que mover o cartão: ")
                        contole_trello.mover_cartao_de_lista(lista_primaria, nome_cartao, lista_destino)
                        print()

                    if escolha == 6:
                        lista = input("Digite a lista em que esta o quadro: ")
                        nome_cartao = input("Digite o nome do cartão: ")
                        contole_trello.remover_cartao(lista, nome_cartao)
                        print()

                    if escolha == 7:
                        registro = contole_trello.registros()
                        cont = 0
                        for acao in registro:
                            cont += 1
                            print(str(cont) + '-> ' + acao)

            else:
                print("Falha ao selecionar :(")

        if opcao == 3:
            quadros = contole_trello.exibir_quadros()
            print("****** QUADROS ******* ")
            for quadro in quadros:
                print("---> " + quadro)
            print()

        if opcao == 4:
            quadro_escolhido = input("Digite o quadro que deseja excluir: ")
            contole_trello.remove_quadro(quadro_escolhido)
            print()

        if opcao == 5:
            registro = contole_trello.registros()
            cont = 0
            for acao in registro:
                cont += 1
                print(str(cont) + '-> ' + acao)
            print()

        if opcao == 0:
            op_sair = input("Tem certesa disso? s/n ")
            if op_sair == "s":
                op_sair = input("Se voce digitar s todos os dados serão perdidos : s/n ")
                if op_sair == "s":
                    print("Eu avisei, xau :) ")
                    break
                if op_sair == "n":
                    print()


if __name__ == '__main__':
    main()
