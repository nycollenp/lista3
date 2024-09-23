numero = int(input("digite um numero: "))

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while numero >= 0:
    if numero <= 25:
        intervalo1 += 1
    else:
        if numero <= 50:
            intervalo2 += 1
        else:
            if numero <= 75:
                intervalo3 += 1
            else:
                if numero <= 100:
                    intervalo4 +=1
    numero = int(input("digite um numero: "))

print("intervalo 1:", intervalo1)
print("intervalo 2;", intervalo2)
print("intervalo 3:", intervalo3)
print("intervalo 4:", intervalo4)