from colorama import Style, Fore, Back, init
from pyfiglet import figlet_format
from rich.console import Console
from time import sleep
import shutil
import os

console = Console()
init(autoreset=True)

def es(text, color=Fore.WHITE, speed=0.05):
    for letra in text:
        print(color + letra, end="", flush=True)
        sleep(speed)
    print(Style.RESET_ALL)

es("Bom dia", color=Fore.RED, speed=0.02)


def analize_de_nomes():
    nomes_ = []
    names_ = []

    for nomes in range(5):
        x = str(input("Quais os nomes das pessoas?: "))
        i = x.strip().lower()

        if i.startswith("a".lower()):
            nomes_.append(i)
        else:
            names_.append(i)

    print(Fore.GREEN + "Esses nomes tem a inicial 'a' no nome ", nomes_)
    print(Fore.RED + "Esses nomes não tem a inicial 'a' no nome ", names_)

def main():
    ascii_art = figlet_format("MENU")
    print(Fore.RED + ascii_art)

if __name__ == "__main__":
    main()
