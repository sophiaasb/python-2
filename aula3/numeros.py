numeros = []

while True:
    valor = int(input('Digite um número: '))
    if(valor == -1):
        break
    else:
        numeros.append(valor)
        
for x in numeros:
    if(x % 2 == 0):
        print(x)
