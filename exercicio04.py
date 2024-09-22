soma = 0.0
habitantes = 0
soma_filhos = 0
maior_salario = 0.0
salario = float(input("informe o salario: "))


while salario >= 0.0:
    numero_filhos = int(input("informe o numero de filhos?: "))
    soma_filhos += numero_filhos
    soma += salario
    habitantes += 1
    salario = float(input("informe o salario: "))

if salario >= maior_salario:
    maior_salario = salario

media_filhos = soma_filhos / habitantes
media_salarial = soma / habitantes
print("media salarial:",media_salarial)
print("media de filhos:", media_filhos)
print("maior salario:", maior_salario)