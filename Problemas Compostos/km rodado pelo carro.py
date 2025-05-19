#passo a passo

#1 - Descobrir quantos litros de gasolima e quantos reais é preciso pra fazer uma viagem de 800km
#2 - Sendo que o carro faz 7 km por litro e ainda resta 10 litros no tanque

#3
#Passo1:O preço da gasolina esta 6,90 reais
#Passo2:Pegar o km total e fazer menos o km percorrido
#Passo3:Pegar o preço da gasolina vezes reias


total = int(800 - 90)
kmtotal = int(total / 7)
km = int(kmtotal - 10)
litros = int(km * 6.90)
print("vai ser gasto",km,"de reais na viagem")
print("vai ser rodados",litros,"km")
