import os
import random 

nomes = []

for x in range(10):
    n = input(f'Digite um nome: ')
    nomes.append(n)
    
sorteio = random.choice(nomes)

print('O nome da sua alma gêmea é ', sorteio)