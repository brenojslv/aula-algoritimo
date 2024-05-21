def entrada_ra(ra_em_str):
    soma = 0
    multiplicacao = 1

    for char in ra_em_str:
        digito = int(char)
        soma += digito
        multiplicacao *= digito

    return soma, multiplicacao

numero = input(str("Digite um número: "))
soma, multiplicacao = entrada_ra(numero)

print("Soma dos dígitos:", soma)
print("Multiplicação dos dígitos:", multiplicacao)
