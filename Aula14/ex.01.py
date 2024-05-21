def calcularanimais(totalcabecas, totalpes):
    coelhos = (totalpes - 2 * totalcabecas) // 2
    patos = totalcabecas - coelhos
    return patos, coelhos

totalcabecas = int(input("Digite o total de cabeças: "))
totalpes = int(input("Digite o total de pés: "))

patos, coelhos = calcularanimais(totalcabecas, totalpes)
print("Quantidade de patos:", patos)
print("Quantidade de coelhos:", coelhos)

