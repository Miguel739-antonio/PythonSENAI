from datetime import datetime

def saudação(nome):
    hora = datetime.now().hour
    if hora < 5:
        print("Boa madrugada", nome)
    elif hora < 12:
        print("Bom dia", nome)
    elif hora < 19:
        print("Boa tarde", nome)
    elif hora < 20:
        print("Boa noite", nome)

nome = input("Digite seu nome ")
hora = saudação(nome)