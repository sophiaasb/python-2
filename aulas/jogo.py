import os
import random

sorteado = random.randint(1,100)
contador = 0

while True:
    numero = int(input('Digite um número entre 1-100: '))
    contador = contador+1
    if(numero == sorteado):
        print(f'Parabéns! Você acertou o número em {contador} tentativas.')
    elif(numero > sorteado):
        print(f'O número é menor!')
    else: 
        print(f'O número é menor!')