import os

valores = []

while True:
    numero = int(input("Digite um número: "))

    if(numero == 0):
        break
    else:
        valores.append(numero)

soma = sum(valores)

os.system('cls')

print(f"A soma dos números é: {soma}")