quant = 0
valor_total = 0


print("")
while True:
    print("escolha uma das opções abaixo")
    print("1 - Adicionar valor da despesa")
    print("2 - Mostrar a quantidade e o valor total das despesas")
    print("0 -  Sair")
    menu_calculador = int(input("coloque um dos números da sua escolha aqui[0, 1 e 2] :"))
    if  menu_calculador == 0:
        break
    elif menu_calculador == 1:
        despesa = int(input("adicione o valor de suas despesas"))
        quant = quant + despesa
        valor_total = valor_total + 1
    elif menu_calculador == 2:
        print("quantidade de despesas", quant)
        print("valor total é", valor_total)
         
    