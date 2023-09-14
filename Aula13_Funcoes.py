# 2. Criação de funções 

# Função inicial com parametros 

def saudacao(name):
    print('Seja bem vindo' )
    print(f'ola, é um prazer ter você fazendo parte desse curso, {name}')
saudacao("Givanildo ")

print('---------------------------- \n') 

# Função com parâmetros 
def saudacao2(nome, curso='Python'):
    print(f'Seja bem vindo, {nome}' )
    print(f'ola, é um prazer ter você fazendo parte desse curso {curso}')
saudacao2("Givanildo","Python")

print('---------------------------- \n') 

# Funções com retorno

def soma(num1,num2):
    return num1+num2

resultado = soma(5,7)
print(f'O resultado da soma é {resultado}')