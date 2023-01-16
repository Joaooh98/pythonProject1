# operadores logicos
# AND = so retorna True se ambas expressoes forem verdadeira
# OR = qualquer uma das expressoes for verdadeiro o resultado e True
#############
# NOT = inverte o valor
# a = 2
# b = 3
# if not b > a:
#     print('b e maior do que a')
# else:
#     print('a e maior do que b')
##########
# A = ''
# b = 0
# if not A:
#     print('Por favor preencher o valor de a.')
##########
# IN usado para verificar o valor da variavel
# nome = 'joao carlos de paiva'
# if 'j' in nome:
#     print('a letra j esta na variavel nome')
# ########
# not in se a valor nao extiver dentro da variavel ele retornara verdadeiro, se estiver ele retorna falso.
# nome = 'joao carlos'
# if 'hgfdhdb' not in nome:
#     print('esses valores nao estao na variavel nome')
########## PRATICANDO VALIDANDO ACESSO
usuario = input('usuario: ')
senha = input('senha: ')
usuario_db = 'joaocp'
senha_db = '123456'
if usuario_db == usuario and senha_db==senha:
    print('voce esta logado no sistema')
else:
    print('usuario ou senha nao esta correto')

