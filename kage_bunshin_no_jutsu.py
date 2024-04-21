# Link do problema: https://judge.beecrowd.com/pt/problems/view/2544

from math import log

teste = int(input())
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
        respostas.append(int(log(i, 2)))
for i in respostas:
    print(i)
