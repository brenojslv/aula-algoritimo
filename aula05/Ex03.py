a = int(input("Coloque o valor do primeiro segmento: "))
b = int(input("Coloque o valor do segundo segmento: "))
c = int(input("Coloque o valor do terceiro segmento: "))

if ((a + b) < c) or ((b + c) < a) or ((a+c < b)):
    print ("Não pode ser um triangulo")
elif (a == b == c):
    print ("É um triangulo Equilátero")
elif (a == b) or (b == c) or (c == a):
    print ("É um triangulo Isóceles")
else:
    print ("É um triangulo escaleno")