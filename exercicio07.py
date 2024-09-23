votação = int(input("digite seu voto: "))

candidato_1 = 0
canditado_2 = 0
canditado_3 = 0
canditado_4 = 0
voto_nulo = 0
voto_branco = 0

while votação >= 1:
        if votação == 1:
            candidato_1 += 1
        else:
            if votação == 2:
                canditado_2 += 1
            else:
                if votação == 3:
                    canditado_3 += 1
                else:
                    if votação == 4:
                        canditado_4 += 1
                    else:
                        if votação == 5:
                            voto_nulo += 1
                        else:
                            if votação == 6:
                                voto_branco += 1
        votação = int(input("digite seu voto: "))

print("candidato 1:", candidato_1)
print("candidato 2:", candidato_1)
print("candidato 3:", candidato_1)
print("candidato 4:", candidato_1)
print("votos nulos:", voto_nulo)
print("votos em branco:", voto_branco)


