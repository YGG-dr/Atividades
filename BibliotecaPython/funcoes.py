from tabulate import tabulate

def adicionar_livro(listLivros):
    titulo = str(input("Título do livro: ")).strip().lower()
    autor  = str(input("Autor do livro: ")).strip().lower()
    livro  = str(input("Status do livro: ")).strip().lower()
    livro = {
    "titulo": titulo,
    "autor": autor,
    "status": "disponível"
}
    listLivros.append(livro)
    print(f"\nLivro '{titulo}' foi adcionado com sucesso!\n")

def emprestar_livro(listLivros):
    titulo = input("Digite o título do livro para ser adicionado: ").strip().lower()
    for livro in listLivros:
        if livro["status"] == "emprestado":
            print("Esse livro já foi emprestado, volte depois!")
        else:
            livro["status"] = "emprestado"
            print(f"livro '{titulo}' foi emprestado com sucesso!")
        return
    print("Esse livro não foi encontrado.")

def devolver_livro(listLivros):
    titulo = str(input("Qual o título do livro para a devolução?: ")).strip().lower()

    for livro in listLivros:
        if livro['titulo'].lower().strip() == titulo.strip().lower():
            print("Este livro está deisponível!")
        else:
            livro['status'] = 'disponível'
            print(f"O seu livro foi devolvido com suscesso: {livro}")
        return
    print("Não foi possível encontrar esse livro.")

def exibir_livros(listLivros):
    if not listLivros:
        print("\n Não há nenhum livro cadastrado ainda.\n")
        return
    
    table = [[livro["titulo"], livro["autor"], livro["status"]] for livro in listLivros]
    print("\nLista dos livros: ")
    print(tabulate(table, headers=["Título", "Autor", "Status"], tablefmt="fancy_grid"))
    print()