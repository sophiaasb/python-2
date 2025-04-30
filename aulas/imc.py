import os

peso = int(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso/(altura*altura)

if(imc<18.5):
    print(f'O seu IMC é: {imc:.1f}, Você está Abaixo do Peso.')
elif(imc>=18.5 and imc<24.9):
    print(f'O seu IMC é: {imc:.1f}, Você está com o Peso Normal.')
elif(imc>=25 and imc<29.9):
    print(f'O seu IMC é: {imc:.1f}, Você está com Sobrepeso.')
elif(imc>=30 and imc<34.9):
    print(f'O seu IMC é: {imc:.1f}, Você está com Obesidade Grau I.')
elif(imc>=35 and imc<39.9):
    print(f'O seu IMC é: {imc:.1f}, Você está com Obesidade Grau II.')
else:
    print(f'O seu IMC é: {imc:.1f}, Você está com Obesidade Grau III.')