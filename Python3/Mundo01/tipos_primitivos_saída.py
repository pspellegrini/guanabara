'''
Curso Python #06 - Tipos Primitivos e Saída de Dados

Números Inteiros
  sintaxe > int()
    = 7, -4, 0, 9875
Números com casas decimais ou Ponto Flutuante
  sintaxe >  float()
    = 4.5, 0.076, -15.223, 7.0
Booleano (Verdadeiro ou Falso)
  sintaxe > bool()
    = True, False
Textos Alfanuméricos ou Strings
  sintaxe > str()
    = 'Olá', '7.5', ''
'''

# Entrada
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = float(input('Digite um número decimal: '))
n4 = str(input('Digite uma frase: '))
n5 = bool(input('Digite qualquer coisa: '))

# Processamento
s = n1 + n2


# Saída
print(type(n1))
print(n4.isalnum())


print('A soma vale', s)
# ou
print(f'A soma vale {s}.')
# ou
print('A soma vale {}.'.format(s))
# ou
print('A soma entre', n1, 'e', n2, 'vale', s)
# ou
print('A soma entre {} e {} vale {}.'.format(n1, n2, s))
# ou
print(f'A soma entre {n1} e {n2} vale {s}.')
