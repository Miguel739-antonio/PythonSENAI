import inputs
inscritos = []

while True:
    print("")
    print("1 - Cadastrar nomes dos participantes")
    print("2 - Exibir o total de inscritos")
    print("3 - Exibir a lista de nomes em ordem alfabética")
    print("4 - Permitir a consulta de um nome")
    op = inputs.input_int("Escolha uma das opções ")
    if op == 1:
        nome = inputs.input_str("Coloque seu nome na lista ") 
        if nome in inscritos:
            print("Seu nome já esta na lista")
        else:
            inscritos.append(nome)
            print("Nome cadastrado")
    if op == 2:
        nome1 = len(inscritos)
        print("quantidade de nomes ", nome1)
    if op == 3:
        for item in sorted(inscritos):
            print(item)
    if op == 4:
        encontrar = inputs.input_str("Digite o nome desejado encontrar ")
        if encontrar in inscritos:
            print(nome)
            print("1 - sim")
            print("2 - não")
            remover = inputs.input_int("Deseja removelo da lista (1/2)")
            if remover == 1:
                inscritos.remove(encontrar)
                print("nome retirado")
            else:
                print("cadastro encerrado")
        else:
            print("Nome não achado")
            print("1 - sim")
            print("2 - não")
            acrescentar = inputs.input_int("Deseja acrescentar nome na lista (1/2)")
            if acrescentar == 1:
                inscritos.append(encontrar)
                print("Nome acrescentado")
            else:
                print("cadastro encerrado")
