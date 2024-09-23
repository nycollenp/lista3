n = int(input("digite um valor: "))

soma = 1 + 1/2 + 1/3 + 1/4 

while n >= 0:
    soma += 1/n
    n = int(input("digite um valor: "))
print("soma:", soma)