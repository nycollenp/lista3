numero = int(input("digite o numero: "))

pares = 0
impares = 0
soma_pares = 0
soma_total = 0
numeros = 0

while numero > 0:
    soma_total += numero
    numeros += 1
    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1
    numero = int(input("digite o numero: "))

media_pares = soma_pares / pares
media_geral = soma_total / numeros

print("pares", pares)
print("impares", impares)
print("media pares", media_pares)
print("media geral", media_geral)
