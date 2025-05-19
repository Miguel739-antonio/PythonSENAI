t1 = int(input("digite um numero de um lado do triangulo"))
t2 = int(input("digte outro numero de outro lado do triangulo"))
t3 = int(input("digite outro numero de outro lado de triangulo"))

if t1 == t2 and t3 == t2:
    print('O TRIANGULO É EQUILATERO')
elif t1 == t2 or t1 == t3:
    print("o triangulo é isósceles")
elif t2 == t1 or t2 == t3:
    print("o triangulo é isósceles")
elif t3 == t1 or t3 == t2:
    print("o triangulo é isósceles")
elif t1 != t2 and t1 != t3 and t2 != t1 and t2 != t3 and t3 != t1 and t3 != t2:
    print("o triangulo é escaleno")