from pyfiglet import *
from colorama import *
from tabulate import *
from rich import *
from time import *
import shutil
import os

length = shutil.get_terminal_size().columns
init(autoreset=True)


def clear():
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


def void(string, cor="white", speed=0.004):
    for Line in string.splitlines():
        characterized_line = Line.center(length)
        for charactere in characterized_line:
            print(f"[{cor}]{charactere}", end="", flush=True)
            sleep(speed)
        print()


def carregar_cardapio():
    return [
        {"id": 1, "nome": "Hambúrguer", "preco": 12.5},
        {"id": 2, "nome": "Pizza", "preco": 30},
        {"id": 3, "nome": "Refrigerante", "preco": 5},
    ]


def exibir_cardapio(cardapio):
    dados_tabela = []
    for item in cardapio:
        dados_tabela.append([item["id"], item["nome"], f"R${item['preco']:.2f}"])
    
    print("\n--- CARDÁPIO DISPONÍVEL ---")
    print(tabulate(dados_tabela, headers=["ID", "NOME", "PREÇO"], tablefmt="pretty"))
    print()


def adicionar_pedido(cardapio, pedido):
    try:
        print("Qual o ID do item que você quer comprar?: ")
        idEscolhido = int(input("> "))
    except ValueError:
        print(f"{Fore.RED}Esse ID é inválido!{Fore.RESET}")
        return

    item = next((i for i in cardapio if i["id"] == idEscolhido), None)

    if item is None:
        print(f"{Fore.RED}Este item não foi encontrado!{Fore.RESET}")
        return

    try:
        print("Qual a quantidade que você quer?")
        qtd = int(input("> "))
        if qtd <= 0:
            print(f"{Fore.RED}A quantidade deve ser maior do que 0!{Fore.RESET}")
            return
    except ValueError:
        print(f"{Fore.RED}Quantidade inválida!{Fore.RESET}")
        return

    total_item = qtd * item["preco"]

    pedido.append(
        {"id": item["id"], "item": item["nome"], "qtd": qtd, "total": total_item}
    )

    print(f'{Fore.GREEN}{item["nome"]} foi adicionada com sucesso ao pedido! {qtd}x.{Fore.RESET}\n')


def exibir_pedido(pedido):
    if not pedido:
        print(f"{Fore.YELLOW}Não há pedidos para a sua mesa!{Fore.RESET}")
        return

    print("\n--- PEDIDO ATUAL ---")
    total_geral = 0
    dados_tabela = []

    for p in pedido:
        dados_tabela.append([
            p["id"], 
            p["item"], 
            p["qtd"], 
            f'R${p["total"]:.2f}'
        ])
        total_geral += p["total"]
    
    print(tabulate(dados_tabela, headers=["ID", "ITEM", "QTD", "SUBTOTAL"], tablefmt="pretty"))
    print(f"\n{Fore.CYAN}TOTAL A PAGAR: R${total_geral:.2f}{Fore.RESET}")


def remover_pedido(pedido):
    if not pedido:
        print(f"{Fore.YELLOW}Não há pedidos para serem removidos!{Fore.RESET}")
        return

    print("Qual pedido (ID ou nome) você deseja remover?")
    lookingfor_input = input("> ").strip()
    found = None
    
    try:
        lookingfor_id = int(lookingfor_input)
        found = next((p for p in pedido if p["id"] == lookingfor_id), None)
    except ValueError:
        found = next(
            (p for p in pedido if p["item"].lower() == lookingfor_input.lower()), None
        )

    if found is None:
        print(f"{Fore.RED}O item '{lookingfor_input}' não foi encontrado no seu pedido!{Fore.RESET}")
        return

    pedido.remove(found)
    print(f'{Fore.GREEN}O item {found["item"]} foi removido com sucesso!{Fore.RESET}')