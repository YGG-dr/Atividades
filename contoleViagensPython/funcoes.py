from tabulate import tabulate

def registrar_viagem(listViagens):
    print("\nRegistrar nova viagem\n")
    motorista = str(input("Qual o nome do motorista?: ")).strip().lower()
    destino = str(input("Qual o seu destino?: ")).strip().lower()
    data = str(input("Quando você deseja viajar?: ")).strip().lower()
    
    try:
        distancia = float(input("Qual foi a distância percorrida (km)?: "))
        gasto = float(input("Quanto foi gasto com combustível (R$)?: "))
    except ValueError:
        print("Por favor digite apenas números em disância e gastos!")
        return

    if distancia <= 0 or gasto <= 0:
        print("A distancia e os gastos devem ser maiores do que zero!")
        return

    consumo = gasto / distancia
    viagem = {
        "motorista": motorista.title(),
        "destino": destino.title(),
        "distancia": distancia,
        "data": data,
        "gasto": gasto,
        "consumo": round(consumo, 2)
    }

    listViagens.append(viagem)
    print(f"Sua viagem foi marcada com sucesso para o dia {data}!")

def exibir_viagens(listViagens):
    print("\nTodas as viagens que você registrou:")
    if not listViagens:
        print("Você nunca fez nenhuma viagem!")
        return

    table = [
        [v["motorista"], v["destino"], f"{v['distancia']} km", f"Dia {v['data']}", f"{v['gasto']:.2f}R$", f"{v['consumo']:.2f}R$/km"]
        for v in listViagens
    ]
    print(tabulate(table, headers=["Motorista", "Destino", "Distância", "Data", "Gasto", "Consumo Médio"], tablefmt="fancy_grid"))

def buscar_motorista(listViagens):
    nome = str(input("\nQue motorista você quer encontrar? ")).strip().title()
    viagens_motorista = [v for v in listViagens if v["motorista"] == nome]

    if not viagens_motorista:
        print(f"Não foi possível encontrar nenhuma viagem para {nome}!")
        return

    table = [
        [v["destino"], f"{v['distancia']} km", f"{v['gasto']:.2f}R$", f"{v['consumo']:.2f}R$/km"]
        for v in viagens_motorista
    ]
    print(tabulate(table, headers=["Destino", "Distância", "Gasto", "Consumo Médio"], tablefmt="fancy_grid"))

def viagem_mais_cara(listViagens):
    print("\nA sua viagem mais cara é:")
    if not listViagens:
        print("Você nunca viajou para nenhum lugar? Meus pezames...")
        return

    mais_cara = max(listViagens, key=lambda v: v["gasto"])
    print(f"""A sua viagem mais cara foi com o motorista {mais_cara['motorista']}
    Para {mais_cara['destino']}
    E gastou {mais_cara['gasto']:.2f}R$""")

def media_consumo(listViagens):
    print("\nA sua média geral de consumo é (R$/km):")
    if not listViagens:
        print("Você deveria tocar a grama...")
        return

    media = sum(v["consumo"] for v in listViagens) / len(listViagens)
    print(f"Média geral: {media:.2f}R$/km")