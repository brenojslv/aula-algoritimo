a = float(input("Coloque a largura do aposento: "))
b = float(input("Coloque o comprimento do aposento: "))
c = float(input("Coloque o valor de litros da lata de tinta: "))
pd = 2.8
p1 = ((a * pd) * 2)
p2 = ((b * pd) * 2)
pt = 1.68
area = ((p1 + p2)- pt)
tin = (area % c)
vtin = round(tin)
print("Valor da area a ser pintada: ", area)
print("Quantidade de latas de tinta: ", vtin)
