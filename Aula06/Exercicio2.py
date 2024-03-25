x = float(input("Insira o valor total da compra: "))

if (x <= 1000.00):
    x = x * 0.9
    print("O valor da sua compra com 10% de desconto é:", x)
elif (x >= 1001.00) or (x >= 4999.99):
    x = x * 0.8
    print("O valor da sua compra com 20% de desconto é:", x)
else:
    x = x * 0.7
    print("O valor da sua compra com 30% de desconto é:", x)