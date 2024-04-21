# Link do problema: https://judge.beecrowd.com/pt/problems/view/1146

respostas = []
while True:
    sequencia = []
    n = int(input())
    if n == 0:
        break
    else:
        sequencia = [i for i in range(1, n+1)]
        respostas.append(sequencia)
for i in respostas:
    print(*i)
