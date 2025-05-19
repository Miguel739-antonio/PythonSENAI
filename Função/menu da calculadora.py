import inputs

def soma (n1 , n2):
    return n1 + n2
def subtração(n1, n2):
    return n1 - n2
def multiplicação(n1, n2):
    return n1 * n2
def divisão (n1, n2):
    return n1/n2
def resultado():
    print(soma(n1, n2), "é o resultado da adição!")
    print(subtração(n1, n2), "é o resultado da subtração!")
    print(multiplicação(n1, n2), "é o resultado da multiplicação!")
    print(divisão(n1, n2), "é o resultado da divisão!")
def menu_calculadora():
    while True:
        
            
            print("escolha uma das opções abaixo")
            print("0 - sair")
            print("1 - soma")
            print("2 - subtração")
            print("3-  multiplicação")
            print("4- divisão")
            menu = inputs.input_int("Escolha uma das opções")
            if menu == 1:
                print(soma(n1, n2))
            elif menu == 2:
                print(subtração(n1, n2))
            elif menu == 3:
                print(multiplicação(n1, n2))
            elif menu == 4:
                print(divisão(n1, n2))    
            elif menu == 0:
                break

   
n1= inputs.input_float("digite um numero:")
n2 = inputs.input_float("digite outro numero:")

menu_calculadora()

    