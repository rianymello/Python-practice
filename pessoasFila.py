def contar_pessoas_enxergam(alturas):
    pessoas_enxergam = 1  # Inicialmente, a primeira pessoa sempre enxerga

    altura_anterior = alturas[0]

    for i in range(1, len(alturas)):
        if alturas[i] > altura_anterior:
            pessoas_enxergam += 1
            altura_anterior = alturas[i]

    return pessoas_enxergam

# Solicitar a quantidade de pessoas na fila
quantidade_pessoas = int(input("Digite a quantidade de pessoas na fila: "))

# Solicitar as alturas das pessoas na fila
alturas = []
for i in range(quantidade_pessoas):
    altura = int(input(f"Digite a altura da pessoa {i+1} em cm: "))
    alturas.append(altura)

# Calcular e exibir o número de pessoas que conseguem enxergar a bilheteira
resultado = contar_pessoas_enxergam(alturas)
print(f"O número de pessoas que conseguem enxergar a bilheteira é: {resultado}")
