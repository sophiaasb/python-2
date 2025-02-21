def peixes(quilos):
    if (quilos > 50):
        excedente = quilos - 50
        multa = excedente * 4
        print('O peso dos peixes excede o valor estabelecido! Deverá pagar uma multa de R$ 4,00 por quilo excedente.')
        print(f'Quilo pescado: {quilos:.2f} kg | Quilo excedente: {excedente:.2f} kg | Valor da multa: R$ {multa:.2f}')
    else:
        print(f'Quilo pescado: {quilos:.2f} kg')
        print('O peso dos peixes não excede o valor estabelecido. Portanto, não há multa a ser paga. ')

quilos = int(input('Quantos kg de peixe João pescou? '))


peixes(quilos)