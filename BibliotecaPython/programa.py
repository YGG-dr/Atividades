from pyfiglet import figlet_format
from rich.console import Console
from funcoes import *
from time import sleep
import shutil
import os

console = Console()

def clear():
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")

def void(string, cor="white", speed=0.004):
    length = shutil.get_terminal_size().columns
    for Line in string.splitlines():
        characterized_line = Line.center(length)
        for charactere in characterized_line:
            console.print(charactere, style=cor, end="", highlight=False, markup=False, soft_wrap=False)
            console.file.flush()
            sleep(speed)
        console.print()

def main():
    clear()
    books = []

    ascii_art = figlet_format("MENU")
    void(ascii_art, cor="yellow", speed=0.007)

    void("\nDigite 'h', 'help' ou 'ajuda' para obter informações de como usar!", speed=0.01, cor="green")
    while True:
        op = str(input("> ")).strip().lower()
        match op:
            case "h" | "help" | "ajuda":
                void(""" 
1. 1 - Adicionar livro
2. 2 - Exibir todos os livros
3. 3 - Emprestar livro
4. 4 - Devolver livro
5. 0 - Sair
\n
""", cor="green", speed=0.002)
            case "1" | "adicionar livro" | "add books":
                adicionar_livro(books)

            case "3"| "emprestar livro" | "lend book":
                emprestar_livro(books)

            case "4" | "devolver livro" | "return book":
                devolver_livro(books)

            case "2" | "exibir livros" | "mostrar livros" | "ver livros" | "show books":
                exibir_livros(books)

            case "0" | "sair" | "fechar" | "close":
                console.print("[blink][yellow]Fechando programa...[/yellow][/blink]")
                sleep(4)
                clear()
                break

            case _:
                void("Essa opção não esxiste, tente novamente")
                clear()
                


if __name__ == "__main__":
    main()