from ast import Break


while True:  # 1 == 1
    numero = int(input('Informe um numero: '))

   
    if numero == 13:
        break

    if numero % 2 == 0:
        continue

    print(numero)