def registar_viagem():
    nome_do_motorista = str(input("Qual o nome do motorista: ")).strip().lower()
    destino = str(input("Qual o destino da viagem?: ")).strip().lower()
    ditancia_percorrida = int(input("Qual a distância percorrida?: "))
    valor_gasto_com_combustivel = float(input("Qual o valor gasto de combustível?: "))
    viagem = {
        "nomeMotorista": nome_do_motorista,
        "destino": destino,

    }