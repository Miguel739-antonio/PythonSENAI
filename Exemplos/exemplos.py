msg = input("Digite uma mensagem")

periodo = input("Digite qual periodo estamos(manha, tarde, noite): ")

saudacao = ""

if periodo == "manha":
   saudacao = "Bom dia"
elif periodo == "tarde":
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"
    
print(saudacao, "segundo colegial", msg)