import random
print("Olá, seja bem vindo ao jogo par ou ímpar")

while True:
    print("Escolha uma das opções abaixo")
    print("1 - par")
    print("2 - ímpar")
    print("3 - sair")
    opcao = int(input("Digite a sua opção "))
    jogador = int(input("Digite um número "))
    pc = random.randint(0,10)
    total = pc + jogador
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total deu {total}.')
    print("Deu par"  if total % 2 == 0 else "Deu ímpar")
    if opcao == 1:
        if total % 2 == 0:
           print("Voce ganhou")
        else:
            print("Voce perdeu")
    if opcao == 2:
        if total % 2 == 1:
           print("Voce ganhou")
        else:
            print("Voce perdeu")
    elif opcao == 3:
            print("Voce saiu do jogo")
            break