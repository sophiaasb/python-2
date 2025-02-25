def calcular_preco(dias, km):
    preco_diario = 60
    preco_km = 0.15
    
    total = (dias * preco_diario) + (km * preco_km)
    
    return total

dias = int(input("Digite o número de dias que o carro foi alugado: "))
km = float(input("Digite o número de quilometros percorridos: "))

preco = calcular_preco(dias, km)

print(f"\n============================================")
print(f"\nO total a pagar pelo aluguel é: R$ {preco:.2f}")