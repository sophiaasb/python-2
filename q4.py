nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes.sort()

print("Nomes em ordem alfabética:")
for nome in nomes:
    print(nome)
