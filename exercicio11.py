valor = int(input("digite o valor: "))

media = 0
soma = 0
valores = 0
positivos = 0
negativos = 0


while valor != 0:
    soma += valor
    valores += 1
    media = soma / valores
    if valor >= 1:
        positivos += 1
    else:
        negativos += 1
    valor = int(input("digite o valor: "))

percentual_positivos = (positivos / valores) * 100
percentual_negativos = (negativos / valores) * 100

print("media", media)
print("positivos", positivos)
print("negativos", negativos)
print("percentual positivo", percentual_positivos )
print("percentual negativo", percentual_negativos )