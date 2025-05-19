idade = int(input("digite o ano de seu nascimento "))
ano = int(input("digite o ano atual"))

if idade >= 1908 and idade <= 2025 and ano > 0 and ano <= 2025:
    idade_atual = ano - idade
if idade_atual <= 10:
    print(idade_atual,"criança")
elif idade_atual == 11 or idade_atual <=17:
    print(idade_atual,"adolescente")
elif idade_atual == 18 or idade_atual <=59:
    print(idade_atual,"adulto")
elif idade_atual >= 60 and idade_atual <= 117:
    print("idoso")
else:
    print("você não existe")