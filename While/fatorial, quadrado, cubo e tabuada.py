while True:
    print("Selecione uma das alternativas abaixo")
    print("")
    print("[1] Fatorial")
    print("[2] Quadrado")
    print("[3] Cubo")
    print("[4] Tabuada")
    print("[0] Sair")
    opcao = int(input("Digite sua opcao "))
    if opcao == 0:
        break
    elif opcao == 1:
   
        valor = int(input('Entre com um número para saber o fatorial: '))  
        fatorial = 1  
        while (valor > 1):  
          fatorial = fatorial * valor  
          valor = valor - 1  
        print('O fatorial é {}.'.format(fatorial))
    elif opcao == 2:
        num1 = int(input("Digite um numero para saber seu quadrado: "))
        quadrado = num1 * num1
        print("seu resultado é ", quadrado)
    elif opcao == 3:
        num1 = int(input("Digite um numero para saber seu cubo: "))
        quadrado = num1 * num1 * num1
        print("seu resultado é ", quadrado)
    elif opcao == 4:
        n = int(input("digite um numero para saber sua tabuada "))
        print(n, 'X 1 =', n*1)
        print(n, 'X 2=', n*2)
        print(n, 'X 3 =', n*3)
        print(n, 'X 4 =', n*4)
        print(n, 'X 5 =', n*5)
        print(n, 'X 6 =', n*6)
        print(n, 'X 7 =', n*7)
        print(n, 'X 8 =', n*8)
        print(n, 'X 9 =', n*9)
        print(n, 'X 10 =', n*10)
