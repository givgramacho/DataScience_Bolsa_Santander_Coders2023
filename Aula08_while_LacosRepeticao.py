numero_sorteado = 15

numero_escolhido = int(input('Informe o número entre 1 e 20: \n'))

while numero_sorteado != numero_escolhido:
    print('Você errou o numero,tente novamente')
    numero_escolhido = int(input('Informe o número entre 1 e 20: \n'))
else:
    print('Você acertou!!')

# EXEMPLO2 Estrutura de repetição com contador 


# contador = 0 
# while contador < 5:
#     print(contador)
#     contador = contador + 1 
#     #contador += 1
    