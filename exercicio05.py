altura_chico = 1.50
altura_ze = 1.30
crescimento_chico = 0.02
crescimento_ze = 0.03
ano = 0

while altura_ze <= altura_chico:
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    ano += 1

print("anos:", ano)