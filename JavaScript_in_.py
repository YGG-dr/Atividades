def calcuadora():
    num1=int(input(f"Qual o 1º número?: "))
    num2=int(input(f"Qual o 2º número?: "))

    operacao=str(input("Qual operação você deseja fazer?: "))
    match operacao:
        case _ if "+" in operacao:
            print(f"Resposta: {num1 + num2}!")
        case _ if "-" in operacao:
            print(f"Resposta: {num1 - num2}!")
        case _ if "*" in operacao:
            print(f"Resposta: {num1 * num2}!")
        case _ if "/" in operacao:
            print(f"Resposta: {num1 / num2}!")

calcuadora()