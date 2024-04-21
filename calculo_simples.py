# Link do problema: https://judge.beecrowd.com/pt/problems/view/1010

codigo1, n_pecas1, v_uni1 = input().split()
codigo1, n_pecas1 = int(codigo1), int(n_pecas1)
v_uni1 = float(v_uni1)
codigo2, n_pecas2, v_uni2 = input().split()
codigo2, n_pecas2 = int(codigo2), int(n_pecas2)
v_uni2 = float(v_uni2)

total = n_pecas1*v_uni1 + n_pecas2*v_uni2
print(f"VALOR A PAGAR: R$ {total:.2f}")
