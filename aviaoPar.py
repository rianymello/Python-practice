def virar_direita(direcao):
    direcoes = ['leste', 'sul', 'oeste', 'norte']
    return direcoes[(direcoes.index(direcao) + 1) % 4]

def encontra_pares_distintos(avis, K):
    coordenadas = {}  # Dicionário para armazenar as coordenadas dos aviões em cada unidade de tempo
    pares = set()     # Conjunto para armazenar pares de aviões distintos

    for unidade_tempo in range(K + 1):
        coordenadas_atuais = {}  # Dicionário temporário para armazenar as coordenadas dos aviões nesta unidade de tempo

        for i, (x, y, direcao) in enumerate(avis):
            if direcao == 'leste':
                x += 1
            elif direcao == 'sul':
                y -= 1
            elif direcao == 'oeste':
                x -= 1
            elif direcao == 'norte':
                y += 1

            # Verifica se o avião colidiu com uma nuvem
            if (x, y) in coordenadas_atuais:
                direcao = virar_direita(direcao)
                avis[i] = (x, y, direcao)

            coordenadas_atuais[(x, y)] = i

        for coordenada, avioes in coordenadas_atuais.items():
            if len(avioes) > 1:
                for i in avioes:
                    for j in avioes:
                        if i < j:
                            pares.add((i, j))

        coordenadas[unidade_tempo] = coordenadas_atuais

    return len(pares)

# Exemplo de utilização
N = int(input())
K = int(input())

avis = []
for _ in range(N):
    x, y, direcao = input().split()
    avis.append((int(x), int(y), direcao))

resultado = encontra_pares_distintos(avis, K)
print(resultado)
