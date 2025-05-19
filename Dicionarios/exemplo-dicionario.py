
#------Dicionarios-------

# Criar
aluno = {
     "nome": "Miguel",
     "idade": 16,
     "altura": 1.76,
     "matriculado": True     
}

carro = {
     "nome": "santana",
     "preço": 14.123,
     "cor": "vermelha"
}

print(carro)
for chave, valor in carro.items():
    print(f"{chave}: {valor}")
carro2 = {
      "nome": "belina",
      "preço": 5.712,
      "cor": "prata"
}    
print(carro2)
for chave, valor in carro2.items():
    print(f"{chave}: {valor}")
carro3 = {
     "nome": "gol g3",
     "preço": 6.211,
     "cor": "preto"
}
print(carro3)
for chave, valor in carro3.items():
    print(f"{chave}: {valor}")
# Adicionar campo
aluno["peso"] = 65

# print(aluno)

# Alterar campo
aluno["idade"] = 22
#print(aluno)

# deletar campo
del aluno["altura"]

# verificar
if "altura" in aluno:
    print("altura existente")
else:
    print()
# Exibir
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Exibir  uma lista de Dicionarios
lista_carros = [carro, carro2, carro3]

    # Escolhendo os campos
for carro in lista_carros:
    print(f"{carro['nome']} - {carro['cor']}")
    
    # Exibindo todos
for carro in lista_carros:
    for chave, valor in carro.items():
        print(f"{chave} - {valor}")
    print()




