# Link do problema: https://judge.beecrowd.com/pt/problems/view/1101

respostas = []
while True:
    soma = 0
    sequencia = []
    n, m = map(int, input().split())
    if n <= 0 or m <= 0:
        break
    if n == m:
        sequencia = [m]
    if n > m:
        sequencia = [i for i in range(m, n+1)]
    else:
        sequencia = [i for i in range(n, m + 1)]
    soma = sum(sequencia)
    respostas.append([sequencia, soma])
for i in respostas:
    print(*i[0], f"Sum={i[1]}")
