#exemplos funções:
from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def mostrar_idade(ano_nascimento):
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    print("Você tem", idade, "anos")

def definir_idade():
    ano = int(input("Digite seu ano de nascimento "))
    mostrar_idade(ano)

definir_idade()
