def pesquisa_binaria_modificada(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    indice = -1  # Inicializa com um valor inválido

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] <= valor:
            indice = meio
            esquerda = meio + 1
        else:
            direita = meio - 1

    return indice

# Ler o número de presentes
n = int(input("Insira o número de presentes: "))

# Ler os preços dos presentes
print("Insira os preços dos presentes, um por linha:")
precos = []
for _ in range(n):
    preco = int(input())
    precos.append(preco)

# Ordenar a lista de preços
precos.sort()

# Calcular as somas de prefixo
somas_prefixo = [0] * n
soma = 0
for i in range(n):
    soma += precos[i]
    somas_prefixo[i] = soma

# Ler o valor do orçamento
orcamento = int(input("\nInsira o valor do orçamento: "))
max_presentes = pesquisa_binaria_modificada(somas_prefixo, orcamento)
print("Máximo número de presentes:", max_presentes + 1)  # +1 porque os índices são base 0
