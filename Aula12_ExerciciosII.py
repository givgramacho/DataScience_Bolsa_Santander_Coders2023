# Ex1: 
x = int(input("Digite um número inteiro: "))

if x < 0:
    resp1 = "negativo"
else:
    resp1 = "positivo"
    
if x % 2 == 0:
    resp2 = "par"
else:
    resp2 = "impar"
    

print("O número {} é {} e {}.".format(x, resp1, resp2))

# EX2:
cont = 0
resultado = 0
n = 1000

while cont != n:
    print(f'n: {n}')
    resultado = resultado + 1/(2**cont)
    cont = cont + 1
    
    print(f'cont: {cont} e {resultado}')
    
print(f'Final resultado: {resultado}')

# Ex3
for _ in range(10):
     
   print("Olá, mundo!") 
   
for _ in [10]:
    print("Olá, mundo!")
    

#Ex:4
lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append(-item)
    
        else:

            lista_final.append(item)
    else:

        if item < 0:
            
            lista_final.append(-2*item)
    
        else:

            lista_final.append(2*item)
print(f'A lista final é {lista_final}')

#Ex5:

animais = ['gato', 'coelho', 'macaco', 'girafa']

animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))