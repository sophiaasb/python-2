def calcular_distancia(distancia,consumo,preco):
    valor_gasto = (distancia/consumo)*preco
    
distancia = int(input('Qual a distância a ser percorrida na viagem? '))
consumo = int(input('Quantos km o carro percorre com um litro de combustível? '))
preco = int(input('Qual o valor do litro de combustível no momento? '))