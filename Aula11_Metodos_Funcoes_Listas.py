# MÉTODOS DE LISTAS é uma função que está atrelado a uma variavél.

lista = [1, 3, 12, 8, 2]

# append - adiciona elementos a lista sempre no final da lista 
print(f'Lista antes do append \n {lista}')
lista.append(3)
print(f'Lista depois do append \n {lista}')

# insert adiciona os elemento na lista em qualquer lugar da lista
lista.insert(2,10)
print(f'Lista depois do insert \n {lista}')

#Extend  junta as listas, porem a lista2 vai para o final 
lista2 = [1, 2, 3]
lista.extend(lista2)
print(f'Lista depois do extend \n {lista}')

# pop remover elementos 
lista.pop() # remove o ultimo elemento da lista 
print(f'Lista depois do pop \n {lista}')

lista.pop(0) # remove o índice 0 da lista
print(f'Lista depois do pop(0) \n {lista}')

# remove - remove o elemento da lista
lista.remove(3)
print(f'Lista depois do pop(0) \n {lista}')

# count - conta quantos elementos 2 tem na lista
print(f'Quantidade de 2 na lista:{lista.count(2)}')

# index mostra o elemento do índice. 
print(f'Índice do elemento 12:', lista.index(12))

# sort ordena a lista 
lista.sort(reverse=True)
print(f'Lista depois do sort(reverse=True) \n {lista}')
lista.sort()
print(f'Lista depois do sort(0) \n {lista}')

# Funções de lista 

#len 
print(f'Funções de lista len \n {len(lista)}')

# sum
print(f'Funções de lista sum  \n {sum(lista)}')

# Max
print(f'Funções de lista max Máxima lista  \n {max(lista)}')

#min
print(f'Funções de lista min - Mínimo lista \n {min(lista)}')