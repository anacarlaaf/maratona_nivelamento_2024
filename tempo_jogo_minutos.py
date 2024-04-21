# Link do problema: https://judge.beecrowd.com/pt/problems/view/1047

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

duracao_horas = hora_final - hora_inicial
duracao_minutos = minuto_final - minuto_inicial

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
