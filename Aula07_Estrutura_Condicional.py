idade = 20 

if idade > 18:
    print("Você e maior de idade!")
else:
    print('Voce é menor de idade!')
    
media = float(input("Informe a média do estudante: "))

if media >= 7:
    print('Você foi Aprovado!:')
elif media>=5:
    print('Recuperação')
else:
    print('Você foi reprovado!')
    
media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Você foi Aprovado!:')
elif  media>=5 and presenca >= 70:
    print('Recuperação')
else:
    print('Você foi reprovado!')
