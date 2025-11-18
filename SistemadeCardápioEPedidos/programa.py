from funcoes import *


def main():
    cardapio = []
    pedido = []
    
    clear()

    ascii_art = figlet_format("MENU")
    void(ascii_art, cor="yellow", speed=0.007)

    void(
        "\nDigite 'h', 'help' ou 'ajuda' para obter informações de como usar!",
        speed=0.01,
        cor="green",
    )
    while True:
        op = str(input("\n> ")).strip().lower()
        match op:
            case "h" | "help" | "ajuda":
                void(
                    """ 
1. 1 - Ver cardápio
2. 2 - pedir comida
3. 3 - Ver pedido
4. 4 - Remover item
5. 5 - Remover tudo
0. 0 - Finalizar
\n
""", cor="yellow", speed=0.002)
            case "1" | "ver cardápio" | "cardápio":
                print(exibir_cardapio(cardapio))

            case "2" | "pedir comida":
                adicionar_pedido(cardapio, pedido)

            case "3" | "ver pedido":
                exibir_pedido(pedido)

            case "4" | "remover pedido":
                remover_pedido(pedido)
            
            case "5" | "remover tudo da lista":
                pedido.clear()
            
            case "0" | "sair" | "fechar" | "close" | "exit":
                print("[blink][yellow]Fechando programa...[/yellow][/blink]")
                sleep(4)
                clear()
                sys.exit(0)

            case _:
                void("Essa opção não esxiste, tente novamente!")
                clear()


if __name__ == "__main__":
    main()
