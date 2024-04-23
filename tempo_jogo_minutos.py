# Link do problema: https://judge.beecrowd.com/pt/problems/view/1047

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

duracao_horas = hora_final - hora_inicial
duracao_minutos = minuto_final - minuto_inicial

if duracao_horas == 0 and duracao_minutos == 0:
    duracao_horas = 24
elif duracao_horas < 0:
    duracao_horas = 24 - hora_inicial + hora_final
    if duracao_minutos < 0:
        duracao_horas -= 1
        duracao_minutos = 60 - minuto_inicial + minuto_final
else:
    if duracao_minutos < 0:
        duracao_horas -= 1
        duracao_minutos = 60 - minuto_inicial + minuto_final
    if duracao_horas < 0:
        duracao_horas = 23

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
