from rich.console import *
from pyfiglet import *
from colorama import *
from funcoes import *
from rich import *
from time import *
import shutil
import sys
import os

length = shutil.get_terminal_size().columns
init(autoreset=True)
console = Console()

cols = shutil.get_terminal_size().columns

def clear():
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")

def void(string, cor="white", speed=0.004):
    for Line in string.splitlines():
        characterized_line = Line.center(length)
        for charactere in characterized_line:
            print(f'[{cor}]{charactere}', end='', flush=True)
            sleep(speed)
        print()

def main():
    clear()
    listViagens = []

    menu = 'MENU'
    print(figlet_format(menu.center(length)))

    void("\nDigite 'h', 'help' ou 'ajuda' para obter informações de como usar!", speed=0.01, cor="green")
    while True:
        op = str(input("\n> ")).strip().lower()
        match op:
            case "h" | "help" | "ajuda":
                void(""" 
1. 1 - Registrar viagem
2. 2 - Exibir viagens
3. 3 - Buscar motorista
4. 4 - Ver viagem mais cara
5. 5 - Média de viagens
6. 0 - Sair
\n
""", cor="yellow", speed=0.002)
            case "1" | "registrar viagem" | "register trip":
                registrar_viagem(listViagens)

            case "2" | "exibir viagem mais cara" | "exibir viagens mais caras" | "show more expansive trip" | "show more expensive trips":
                exibir_viagens(listViagens)

            case "3" | "buscar motorista" | "looking for a driver":
                buscar_motorista(listViagens)
            
            case "4" | "ver viagem mais cara" | "ver viagens mais caras" | "show more expensive trip" |"show more expensive trips":
                viagem_mais_cara(listViagens)
            
            case "5" | "média de viagem" | "média de viagens" | "avarage trip" | "avarage trips":
                media_consumo(listViagens)
                
            case "0" | "sair" | "fechar" | "close" | "exit":
                console.print("[blink][yellow]Fechando programa...[/yellow][/blink]")
                sleep(4)
                clear()
                break
                sys.exit(0)

            case _:
                void("Essa opção não esxiste, tente novamente!")
                clear()
                


if __name__ == "__main__":
    main()