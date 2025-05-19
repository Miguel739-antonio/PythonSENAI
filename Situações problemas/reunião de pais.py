import inputs
pais_inscritos = []
pais_ausentes = []
pais_presentes = []
while True:

    print("")
    print("1 - Cadastrar nomes dos pais")
    print("2 - Exibir o total de pais ")
    print("3 - Exibir a lista de nomes em ordem alfabética")
    print("4 - Confirmação de presenças dos pais")
    print("5 - Exibir o relatório da chamada")
    op = inputs.input_int("Escolha uma das opções")
    if op == 1:
        nome = inputs.input_str("Coloque seu nome na lista ")        
        
        if nome in pais_inscritos:
            print("Seu nome já está na lista") 
        else:
            pais_inscritos.append(nome)
            print("Nome adicionado")
    if op == 2:
        nome1 = len(pais_inscritos)
        print("quantidade de nomes ", nome1)
    if op == 3:
        for item in sorted(pais_inscritos):
            print(item)
    if op == 4:
        for nome in pais_inscritos:
            print(nome)
            print("1 - sim")
            print("2 - não")
            presenca = inputs.input_str("Esta presente")
            if presenca == 1:
                pais_presentes.append(nome)
            else:
                pais_ausentes.append(nome)
    if op == 5:
        print("Ausentes:")
        for ausentes in sorted(pais_ausentes):
            print(ausentes)
        print("Presentes:")
        for presentes in sorted(pais_presentes):
            print(presentes)
    
                    