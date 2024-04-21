# Link do problema: https://judge.beecrowd.com/pt/problems/view/1094

testes = int(input())
cobaias = {"C": 0, "R": 0, "S": 0}
for i in range(testes):
    qtd, especie = input().split()
    qtd = int(qtd)
    cobaias[especie] += qtd

total = sum(cobaias.values())
total_coelhos = cobaias["C"]
total_ratos = cobaias["R"]
total_sapos = cobaias["S"]

percentual_coelhos = 100 * total_coelhos / total
percentual_ratos = 100 * total_ratos / total
percentual_sapos = 100 * total_sapos / total

print(f"Total: {total} cobaias")
print("Total de coelhos:", total_coelhos)
print("Total de ratos:", total_ratos)
print("Total de sapos:", total_sapos)
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
