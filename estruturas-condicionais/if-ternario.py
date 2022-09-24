saldo = 1000
saque = int(input('Valor '))
restante = saldo - saque

status = 'Sucesso' if saldo >= saque else 'Falha'

print (f'{status} ao realizar o saque" ')
print ('Seu saldo atual é ', restante)