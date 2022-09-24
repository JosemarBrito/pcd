MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input('Informa sua Idade: '))

if idade >= MAIOR_IDADE:
    print ('Maior de idade, pode tirar a CNH. ')

if idade < MAIOR_IDADE:

    print ('Menor de idade, Não pode tirar CNH')
print()

if idade >= MAIOR_IDADE:
    print ('Maior de idade, pode tirar a CNH. ')
else:
    print ('Menor de idade, Não pode tirar CNH')

print()
print('--------------------------------------')
print()

if idade >= MAIOR_IDADE:
    print ('Maior de idade, pode tirar a CNH')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer aulas teoricas, mas ainda nao pode fazer aulas praticas. ')
else:
    print ('Menor de idade, Não pode tirar CNH')
