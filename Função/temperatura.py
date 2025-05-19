from  datetime import datetime

def celsius_fahrenheit(graus):
    n1 = 1.8 + 32
    fahrenheit = graus * n1
    return fahrenheit

def celsius_kelvin(kelvin):
    parakelvin = graus + 273
    return parakelvin

def mostrar_conversão(graus):
    print("O resultado é",celsius_fahrenheit(graus),"em fahrenheit")
    print("O resultado", celsius_kelvin(graus), "em kelvin")
   

graus = float(input("Digite a temperatura:"))
mostrar_conversão(graus)
