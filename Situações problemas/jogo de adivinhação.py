import random
numero_secreto = random.randint(1,100)
print("Bem vindo ao Jogo de Adivinhação!")   
print('Tente adivinhar o mumero que estou pensando') 
while True:  
        adivinhaçao = int(input("Tente adivinhar o número: "))
        if adivinhaçao < numero_secreto:
            print("Tente um número maior")
        elif adivinhaçao > numero_secreto:
            print("Tente um número menor.")
        elif adivinhaçao == numero_secreto:
            print("Parabéns! Você acertou!")
            print("2 - Deseja sair")
            print("1 - Deseja jogar de novo")
            escolha = int(input(""))
            if escolha == 1:
                print("jogar de novo")
                numero_secreto = random.randint(1,100)
            else:
                print("o jogo acabou")
                break
            
         
