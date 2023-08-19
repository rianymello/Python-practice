def pode_construir_banco(grelha, N, K):
    for linha in grelha:
        vazios_consecutivos = 0
        for char in linha:
            if char == '.':
                vazios_consecutivos += 1
                if vazios_consecutivos >= K:
                    return 1
            else:
                vazios_consecutivos = 0
    return 0

# Exemplo de utilização
N = int(input("Digite o tamanho da grelha (N): "))
K = int(input("Digite o número de pessoas no grupo (K): "))

grelha = []
for _ in range(N):
    linha = input()
    grelha.append(linha)

resultado = pode_construir_banco(grelha, N, K)

if resultado == 1:
    print("É possível construir um banco.")
else:
    print("Não é possível construir um banco.")
