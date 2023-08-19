"""

Enunciado:

Na cidade de "Vegópolis", os habitantes adoram diferentes tipos de legumes.
Cada legume possui uma altura que é calculada usando dois valores, A e B, juntamente com um número sequencial.
Um morador de "Vegópolis" deseja saber até que ponto ele pode consumir uma sequência de legumes, seguindo algumas regras.
Ele tem um número limitado de ações que pode realizar (chamado de "t") 
 e só pode diminuir a altura de um certo número de legumes por vez (chamado de "m"). 

O objetivo é determinar o maior número de legumes que ele pode consumir, obedecendo essas regras.
Sua tarefa é ajudar o morador a responder essas perguntas para diferentes consultas.

Input:
Três inteiros separados por espaço: A, B e n (1 ≤ A, B ≤ 10^6, 1 ≤ n ≤ 10^5).
Para cada uma das n consultas:
Três inteiros separados por espaço: l, t e m (1 ≤ l, t, m ≤ 10^6).

Output:
Para cada consulta, imprima o maior número possível de legumes que o morador pode consumir, ou -1 se não for possível
"""


def main():
    A, B, n = map(int, input().split())  # Lê A, B e o número de consultas n
    s = [A + (i - 1) * B for i in range(1, n + 1)]  # Calcula os tamanhos dos Legumes usando a fórmula
    
    for _ in range(n):
        l, t, m = map(int, input().split())  # Lê os valores da consulta: l, t e m
        
        max_heights = [s[i] + m * B for i in range(l - 1, n)]  # Calcula as alturas máximas após as operações
        last_consumed = -1
        
        for r, max_height in enumerate(max_heights):
            if s[r] <= max_height:  # Verifica se a operação é possível
                last_consumed = r + 1
        
        print(last_consumed)

if __name__ == "__main__":
    main()


""""
Nota:
No contexto do algoritmo, "A" e "B" são valores que influenciam a altura dos legumes na sequência.
"A" representa o valor inicial da altura do primeiro legume, enquanto "B" define o aumento na altura entre legumes consecutivos.
Cada legume subsequente terá sua altura aumentada em "B" unidades em relação ao legume anterior.

"""