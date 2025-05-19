altura = float(input("digte a sua altura"))
peso = float(input("digite seu peso"))

imc = peso / altura ** 2

if imc <= 19:
    print(f'{imc:.2f} imc, voce esta abaixo do peso')
elif imc > 19 and imc <= 27:
    print(f'{imc:.2f} imc, voce esta com o peso ideal')
elif imc > 27 and imc <= 32:
    print(f'{imc:.2f} imc, voce esta acima do peso')
elif imc > 32:
    print(f'{imc:.2f} imc, voce esta obeso')

