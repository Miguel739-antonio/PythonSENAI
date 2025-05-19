num1 = (input('solicite um numero inteiro '))
num2 = (input('solicite outro numero inteiro '))
num3 = (input('solicite outro numero inteiro '))

if num1 > num2:
    if num1 > num3:
        print("o primeiro é o maior")
elif num2 > num1:
    if num2 > num3:
        print("o segundo é o maior")
elif num3 > num1:
    if num3 > num2:
        print("o terceiro é o maior")
