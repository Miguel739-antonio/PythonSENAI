def input_str(mensagem):
    while True:
        nome = str(input(mensagem))

        if not nome.isalpha():
            print("Digite apenas letras")
        else:
            return nome
def input_int():
    while True:
        try:
            num = int(input())
            return num      
        except ValueError:
            print("Digite apenas numeros")
        else:
            return num
def input_float(mensagem, decimal = 2):
    while True:
        try:
            num2 = float(input(mensagem))
            return round(num2, decimal)
        except ValueError:
            print("Digite somente numeros")
