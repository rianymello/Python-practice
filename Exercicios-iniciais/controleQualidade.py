def verifica_controlo_qualidade(A, L, C):
    if A >= 3 and A * L * C >= 50:
        return 1
    else:
        return 0


altura = float(input("Digite a altura da caixa em centímetros: "))
largura = float(input("Digite a largura da caixa em centímetros: "))
comprimento = float(input("Digite o comprimento da caixa em centímetros: "))

resultado = verifica_controlo_qualidade(altura, largura, comprimento)

if resultado == 1:
    print("A caixa passou no controle de qualidade.")
else:
    print("A caixa não passou no controle de qualidade.")
