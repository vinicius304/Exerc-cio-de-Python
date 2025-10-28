peso = float(input("Digite o peso da peça (kg): "))

if peso <= 0.5:
    print("Classificação: Leve")
elif peso <= 2:
    print("Classificação: Média")
elif peso <= 5:
    print("Classificação: Pesada")
else:
    print("Classificação: Muito pesada")
