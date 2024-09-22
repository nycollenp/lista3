valor = int(input("digite um valor positivo: "))

if valor < 0:
    print("valor invalido")
else:
    fatorial = 1
    for i in range(1, valor + 1):
        fatorial = fatorial * i
print("fatorial", fatorial)