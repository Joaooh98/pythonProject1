#operadores relacionais
#  ==, >, >=, <, <=, !=
# = ultilizado para afirmar se um valor e igual a outro
# == e ultilizado para perguntar se um valor igual a outro

# print('2 e igual a 3?  ', 2 == 3)
# print('2 e maior que 3? ', 2 > 3)
# print('2 e maior ou igual a 3? ', 2 >= 3)
# print('2 e menor que 3? ', 2 < 3)
# print('2 e menor ou igual a 3? ', 2 <= 3)
# print('2 e diferente de 3? ', 2 != 3)

# praticando
# analise financeira
# nome = input('qual o seu nome? ')
# ano_de_nascimento = input('em que ano vc nasceu? ')
# ano_atual = 2022
# idade_limite = 18
# idade = ano_atual - int(ano_de_nascimento)
#
# if idade > idade_limite:
#     print(f'{nome}, sua ficha finaceira vai para analise aguarde retorno')
# else:
#     print(f" {nome}, voce nao tem idade para realizar financiamento.")

nome = input('qual o seu nome? ')
ano_de_nascimento = input('em que ano vc nasceu? ')
ano_atual = 2022
idade_menor = 18
idade_maior = 50
idade = ano_atual - int(ano_de_nascimento)

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome}, sua ficha finaceira vai para analise aguarde retorno')
else:
    print(f" {nome}, voce nao tem idade para realizar financiamento.")
