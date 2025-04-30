print("===== ELEIÇÃO =====\n")

qntdeleitores = int(input("Digite a quantidade de eleitores: "))

candidato1 = 0
candidato2 = 0
candidato3 = 0

for x in range(qntdeleitores):
    voto = int(input("Digite 1 para o Candidato 1 - Digite 2 para o Candidato 2 - Digite 3 para o Candidato 3: "))
    if (voto == 1):
        candidato1 += 1
    elif (voto == 2):
        candidato2 += 1
    elif (voto == 3):
        candidato3 += 1

if candidato1 > candidato2 and candidato1 > candidato3:
    print(f"O Candidato 1 ganhou a eleição com {candidato1} votos!")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print(f"O Candidato 2 ganhou a eleição com {candidato2} votos!")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print(f"O Candidato 3 ganhou a eleição com {candidato3} votos!")
else: 
    print(f"Houve algum empate na eleição. ")
