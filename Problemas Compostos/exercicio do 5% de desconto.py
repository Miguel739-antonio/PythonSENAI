#passo a passo

#1 - Achar o nome do produto e o preço

#2 - Aplicar um desconto de 5%
     #Valor com o desconto
#3
#Passo 1: Multiplicar o valor pela porcentagem
#Passo 2: Multiplicar o novo valor por 100
#Passo 3: Exibir o novo preço e quanto diminuiu


produto = input("digite o nome do produto")
preço = float(input("valor do produto"))
cupom = preço / 20
cupom2 = preço - cupom

print("com o desconto de", cupom, "reais " "o preço com cupom sera de",cupom2)