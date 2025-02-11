import os
import random 

nomes = []

for x in(range(10)):
    n = input('Digite um nome: ')
    nomes.append(n)
    
sorteio = random.choice(nomes)
print('A sua alma gêmea é: ', sorteio)