

for i in range(20):
    valor = int(input("digite o valor: "))
    if i == 0:
        menor = valor
        maior = valor
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
print("menor", menor)
print("maior", maior)