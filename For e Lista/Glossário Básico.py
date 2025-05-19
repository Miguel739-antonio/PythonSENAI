#etapa 1:
objetos = ["lapis", "colher", "caneta", "faca", "apontador"]

#etapa 2:
objetos.append("controle")

#variaveis:
ob1 = objetos [0]
ob2 = objetos [len(objetos) - 1]

#etapa 3:
print(objetos[1])

#etapa 4:
objetos.pop(1)
print(objetos.pop(2))

#etapa 5:
quantidade = len(objetos)
print("a quantidade de objetos na lista é", quantidade)

#etapa 6:
for objeto in objetos:
  print(objeto)

#etapa 7:
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print("cadeira removida")
else:
    objetos.append("cadeira")
    print("cadeira adicionada")
    
#etapa 8:
print(objetos)
objetos.sort()
print(objetos)

#etapa 9:
ob1 = objetos[0]
ob2 = objetos [len(objetos) - 1]
print("o primeiro objeto é ", ob1)
print("o ultimo objeto é ", ob2)

#etapa 10:
objetos.clear()
print("a lista apagou")
print(objetos)