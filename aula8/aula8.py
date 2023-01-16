#Criar variaveis para nome (str), idade (int)
#Altura (float) e peso (float) de uma pessoa
# Criar variavel com o ano atual (int)
# obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
# obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
# Exibir um texto com todos os valores na tela usando F-Strings(com chaves)
nome = 'joao'
ano_atual = 2022
ano_nascimento = 1998
idade = ano_atual - ano_nascimento
altura = 1.75
e_maior = idade > 18
peso = 82
imc = peso/(altura*altura)
print(f'{nome} tem {idade}  anos de idade e {altura}m de altura')
print(f'{nome} pesa {peso}kg e seu imc e: {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')




