def serprimo(n):

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contprimos(limite):
    quantprimos = 0
    for i in range(2, limite + 1):
        if serprimo(i):
            quantprimos += 1
    return quantprimos

def insery():
    y = int(input("Digite um valor para Y: "))
    return y

def calcprimos(y):

    limite = y * 2 + 5
    primos = [i for i in range(2, limite + 1) if serprimo(i)]
    soma_primos = sum(primos)
    return primos, soma_primos
def yprimo(y):

    if serprimo(y):
        print(f"{y} é um número primo.")
    else:
        print(f"{y} não é um número primo.")

y = insery()
yprimo(y)

quantprimos = contprimos(y)
print(f"Quantidade de números primos até {y}: {quantprimos}")
primos, soma_primos = calcprimos(y)
print(f"Lista de números primos até {y * 2 + 5}: {primos}")
print(f"Soma dos números primos da lista {y * 2 + 5}: {soma_primos}")