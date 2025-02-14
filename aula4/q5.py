import os

numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

    media = sum(numeros) / 10

print(f"A média dos números é: {media}")