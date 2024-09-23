n = int(input("digite um valor: "))

contador = 0

while contador < n:
    valor = int(input("informe o valor: "))
    fatorial = 1
    i = valor

    while i > 1:
        fatorial = fatorial * i
        i = i - 1

    print("valor", valor, "fatorial", fatorial)