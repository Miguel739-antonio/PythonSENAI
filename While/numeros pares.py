num = int(input("digite um número "))
quant = 0

print(num)
while True:
    num = num - 1
    
    if num % 2 == 0:
        print(num)
        quant = quant + 1
    elif num <= 0:
        print("a quantidade de numeros par é", quant + 1)
        
        break 