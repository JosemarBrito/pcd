saldo = 1000
saque = 200
limite =100

print (saldo >= saque)
print (saldo <= saque)

# Operador E

print (saldo >= saque and saque <= limite)

# Operador O

print (saldo >= saque or saque <= limite)

# Operador Negação

contatos_emergencia = [1]
print (not 1000 > 1500)
print (type(contatos_emergencia))

print (not (contatos_emergencia))

print (not "saque 1500;")

print("--------------------------------")
print (True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print (False or False)
print("--------------------------------")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp1 = saldo>= saque and saque <= limite or conta_especial and saldo >= saque
exp2 = saldo>= saque and saque <= limite or conta_especial and saldo >= saque
print (exp1)
print (exp2)