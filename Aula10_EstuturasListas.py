# LISTAS
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com listas
notas = [7.9, 9.7, 8.2]

# Criando listas colchetes 
lista =[]
lista = list()
lista = [26, 'Givanildo', 3.14159, True]
lista_de_listas = [10,[1, 2, 3]]


# Indexação e Slices(fatiamento)
lista = [26, 'Givanildo', 3.14159, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
#print(lista[4])

print(lista[-1])
print(lista[-2])
print(lista[-3])

#Slice
lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# Interação com for 

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)
    
# 2. Utilizando os indices

print(f'Comprimento da lista: {len(lista)}')

# Imprime o indice da lista
for i in range(len(lista)):
    print(i)

# Imprime os elementos da lista por indices
for i in range(len(lista)):
    print(lista[i])

