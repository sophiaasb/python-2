idade = int(input('Digite sua idade: '))

if(idade>=18):
    print('Você é adulto')
elif(idade<18 and idade>=12):
    print('Você é adolescente.')
else:
    print('Você é criança.')