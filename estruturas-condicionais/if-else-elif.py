import sys


saldo = 2000
saque = float(input('Informe o valor de saque: '))

if saldo >= saque:
    print('Realizando Saque!')

else:
    print('Saldo insuficiente!')

print()
print('--------------------------')
print()

opcao = int(input('Informe uma opção: \n[1] Sacar \n[2] Extrato: '))
if opcao == 1:
    valor = float(input('Informe a quantia para o saque: '))
elif opcao == 2:
    print ('Exibindo o Extrato ... ')
else:
    sys.exit ('Opção Invalida')