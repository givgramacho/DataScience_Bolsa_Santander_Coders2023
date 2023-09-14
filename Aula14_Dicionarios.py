# DICIONARIO 

#criando dicionario 
lista = {}
dicionario = dict()
lista = [1, 2, 3]

dicionario = {'nome': 'Givanildo', 'idade':26, 'altura':1.77}

print(dicionario)

print(dicionario['idade'])

# adicionando elementos em um dicionario 

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] =2
print(dicionario)


# Iteração sobre um dicionário

for variavel in dicionario:
    print(variavel)

    
for chave in dicionario:
    print(chave, dicionario[chave])

# testando a existência de uma chave 
print('peso' in dicionario)