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

def calcular_media(notas):
    return sum(notas) / len(notas)

notas = []

for i in range(4):
    nota = float(input("Digite as notas: "))
    notas.append(nota)

media = calcular_media(notas)

print("Aprovado" if media >= 7 else "Reprovado")
        
def busca_em_lista():
    lista_de_numeros=[]
    lista_de_busca=[]
    for i in range(6):
        entrada=int(input("Digite os números que você deseja adicionar: "))
        lista_de_numeros.append(entrada)
    
    busca = int(input("O que você deseja buscar?: "))
    if busca in lista_de_numeros:
        lista_de_busca.append(busca)
        
def main():
    ascii_art = figlet_format("MENU")
    print(Fore.RED + ascii_art)
    op = str(input("O que você deseja?: "))
    opt = op.strip().lower()
    
    match opt:
        case _ if opt in ["questão 1", "primeira questão", "1"]:
            analize_de_nomes()
        case _ if opt in ["questão 2", "segunda questão", "2" ]:
            calcular_media()
        case _ if opt in ["questão 2", "segunda questão", "2" ]:
            busca_em_lista()
            
if __name__ == "__main__":
    main()