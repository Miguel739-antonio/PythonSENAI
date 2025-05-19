idade = int(input("digite o seu ano de nascimento"))

am = ""
mp = 2025
mi = mp -  idade


print(mi,"anos")

if mi < 18:
    am = "é menor"
elif mi > 18:
    am = "é maior"
print(am,"de idade")
   