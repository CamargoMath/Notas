def Calculo_Media(soma, P1, P2, AO):
    Media_Semana = soma / 18
    Media_Final = Media_Semana * 0.15 + P1 * 0.3 + P2 * 0.3 + AO * 0.25
    if Media_Final < 5:
        return 'Sua nota nesse momento é {} e você está sendo REPROVADO. Tente melhorar sua média!'.format(Media_Final)
    elif 5 <= Media_Final < 6:
        return 'Sua nota nesse momento é {} e você está de RECUPERAÇÃO. Estude para a prova final!'.format(Media_Final)
    else:
        return 'Sua nota nesse momento é {} e você está APROVADO em Probabilidade-1. Meus parabéns!!'.format(Media_Final)

soma_numero_lista = 0

S2 = float(input('Nota questionário semana 2: '))
S3 = float(input('Nota questionário semana 3: '))
S4 = float(input('Nota questionário semana 4: '))
S5 = float(input('Nota questionário semana 5: '))
S6 = float(input('Nota questionário semana 6: '))
S8 = float(input('Nota questionário semana 8: '))
S9 = float(input('Nota questionário semana 9: '))
S10 = float(input('Nota questionário semana 10: '))
S11 = float(input('Nota questionário semana 11: '))
S12 = float(input('Nota questionário semana 12: '))
S13 = float(input('Nota questionário semana 13: '))
S14 = float(input('Nota questionário semana 14: '))
S15 = float(input('Nota questionário semana 15: '))
S16 = float(input('Nota questionário semana 16: '))
S17 = float(input('Nota questionário semana 17: '))
S18 = float(input('Nota questionário semana 18: '))
S19 = float(input('Nota questionário semana 19: '))
S20 = float(input('Nota questionário semana 20: '))

lista_de_notas = [S2, S3, S4, S5, S6, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20]

for k in range(len(lista_de_notas)):
    for j in range(len(lista_de_notas)):
        if lista_de_notas[k] > lista_de_notas[j]:
            lista_de_notas[k], lista_de_notas[j] = lista_de_notas[j], lista_de_notas[k]
            
for k in range(len(lista_de_notas) - 2):
    soma_numero_lista += lista_de_notas[k]

P1 = float(input('Nota prova 1: '))
P2 = float(input('Nota prova 2: '))
AO = float(input('Nota prova oral: '))

print()
print(Calculo_Media(soma_numero_lista, P1, P2, AO))
print()