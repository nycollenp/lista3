valor = int(input("informe um valor positivo: "))
media = 0
soma = 0
quantidade_valores = 0

while valor >= 1:
    soma += valor
    quantidade_valores += 1
    media = soma / quantidade_valores
    valor = int(input("informe um valor positivo: "))
print(media)