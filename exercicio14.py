codigo = int(input("digite o codigo: "))

preco_novo = 0
soma_aumento = 0
soma_geral = 0
quantidade_preco = 0

while codigo >= 0:
    preco = float(input("digite o preço: "))
    preco_novo = preco * 1.2
    print("codigo:", codigo)
    print("preço novo:", preco_novo)
    soma_aumento += preco_novo
    soma_geral += preco
    quantidade_preco += 1
    codigo = int(input("digite o codigo: "))

    media_aumento = soma_aumento / quantidade_preco
    media_geral = soma_geral / quantidade_preco

print("media aumento:", media_aumento)
print("media geral:", media_geral)