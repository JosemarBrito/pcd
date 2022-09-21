curso = "curso Python"
nome_curso = curso
saldo, limite = 200, 200

exp1 = curso is nome_curso

exp2 = curso is not nome_curso

exp3 = saldo is limite

print (exp1, exp2, exp3)

print("--------------------------")

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)
