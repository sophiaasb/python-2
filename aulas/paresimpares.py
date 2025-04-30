import os

numero = int(input('Digite um número: '))

os.system('cls')

if(numero % 2 == 0):
    print("O número é par.")
else:
    print("O número é impar.")