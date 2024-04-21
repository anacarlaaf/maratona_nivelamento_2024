# Link do problema: https://judge.beecrowd.com/pt/problems/view/2670

a1 = int(input())
a2 = int(input())
a3 = int(input())

no1 = a3 * 4 + a2 * 2
no2 = a1 * 2 + a3 * 2
no3 = a1 * 4 + a2 * 2

menor = [no1, no2, no3]

print(min(menor))
