nomes = []

while True:
    n = input('Digite um nome: ').lower
    
    if(n == 'exit'):
        break
    else:
        nomes.append(n)
    
for x in nomes:
    if(x.startswith('a')):
        print(x.capitalize())