def Nota_Tarefa(Soma_tarefa):
    NotaT = Soma_tarefa / 5
    return NotaT

def Nota_AAS(Soma_AAS):
    NotaAAS = Soma_AAS / 5
    return NotaAAS

def Nota_AS(Soma_AS):
    NotaAS = Soma_AS / 3
    return NotaAS

def Media():
    MF = 0.25 * Nota_Tarefa(SomaT) + 0.25 * Nota_AAS(SomaAAS) + 0.5 * Nota_AS(SomaAS)
    if MF < 5:
        return 'Sua média no momento é {:.2F} e você está sendo REPROVADO. Tente melhorar suas notas.'.format(MF)
    elif 5 <= MF < 6:
        return 'Sua média no momento é {:.2F} e por enquanto você está de RECUPERAÇÃO. Estude bastante para a prova!'.format(MF)
    else:
        return 'Sua média no momento é {:.2F} e você já está APROVADO em Geometria Analítica, meus parabéns!!'.format(MF)

T1 = float(input('Insira a nota da T1: '))
T2 = float(input('Insira a nota da T2: '))
T3 = float(input('Insira a nota da T3: '))
T4 = float(input('Insira a nota da T4: '))
T5 = float(input('Insira a nota da T5: '))

SomaT = (T1 + T2 + T3 + T4 + T5)

AAS1 = float(input('Insira a nota da AAS1: '))
AAS2 = float(input('Insira a nota da AAS2: '))
AAS3 = float(input('Insira a nota da AAS3: '))
AAS4 = float(input('Insira a nota da AAS4: '))
AAS5 = float(input('Insira a nota da AAS5: '))

SomaAAS = (AAS1 + AAS2 + AAS3 + AAS4 + AAS5)

AS1 = float(input('Insira a nota da AS1: '))
AS2 = float(input('Insira a nota da AS2: '))
AS3 = float(input('Insira a nota da AS3: '))

SomaAS = (AS1 + AS2 + AS3)

print()
print(Media())
print()