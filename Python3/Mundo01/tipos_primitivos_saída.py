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

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2

print('A soma vale', s)
# ou
print(f'A soma vale {s}.')
# ou
print('A soma vale {}.'.format(s))
