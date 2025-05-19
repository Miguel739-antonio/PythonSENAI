notas = input("solicite duas notas para calcular a media de um aluno")

nota1 = float(input("digite um numero"))
nota2 = float(input("digite outro numero"))

resultado = (nota1 + nota2)/2

if resultado >=70:
    print("aluno aprovado")
elif resultado <70:
    print("aluno reprovado")
    