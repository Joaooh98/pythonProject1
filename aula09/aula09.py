# ENTRADA DE DADOS
nome = input('qual o seu nome?')
idade = input('qual a sua idade? ')
ano_nascimento = 2022 - int(idade)
print()
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}')

# para realizar calculos com o input e necessario converter o valor recebido de str para inteiro caso contrario nao ira somar e sim concatenar
numero_01 = int(input('digite um numero: '))
numero_02 = int(input('digite um numero: '))

print(numero_01 + numero_02)

# exemplo de conversao
variavel = '5.5'
outra_variavel = (int(float(variavel)))
print(type(outra_variavel))