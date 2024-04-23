# Link do problema: https://judge.beecrowd.com/pt/problems/view/2544

from math import log

casos = []
while True:
    try:
        casos.append(int(input()))
    except EOFError:
        break

respostas = []
for i in casos:
    if i == 1:
        respostas.append(0)
    else:
        respostas.append(log(i+1, 2))  # progressão geométrica
for i in respostas:
    print(int(i))
