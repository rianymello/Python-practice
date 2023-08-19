def pesquisabinaria(arr, q):
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2

        if arr[m] == q:
            return "Encontrado"
        elif arr[m] < q:
            l = m + 1
        else:
            h = m - 1
    return "Não Encontrado"

# Solicita ao usuário para inserir a lista de números
n = int(input("Digite o número de elementos na lista: "))
seq = []
for i in range(n):
    num = int(input(f"Digite o número {i + 1}: "))
    seq.append(num)

q = int(input("Digite o número que deseja pesquisar: "))
print(pesquisabinaria(seq, q))
