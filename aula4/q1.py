import os

vetor = []

for i in range(3):
    ir_para_vetor = int(input(f'Digite o {i+1}º numero: '))
    vetor.append(ir_para_vetor)
    
os.system('cls')

print(f"O maior número é: {max(vetor)}") 