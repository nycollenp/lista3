
intervalo = 0
fora_intervalo = 0

for i in range(10):
    valor = int(input("digite um valor: "))
    if 10 <= valor <= 20:
        intervalo += 1
    else:
       fora_intervalo += 1
print("intervalo:", intervalo)
print("fora do intervalo:", fora_intervalo)
