n1 = int(input("digite um valor: "))
n2 = int(input("digite um valor: "))

if n1 > n2:
    menor = n2
    maior = n1
else:
    menor = n1
    maior = n2

contador = menor

while contador <= maior:
    print(contador)
    contador = contador + 1

