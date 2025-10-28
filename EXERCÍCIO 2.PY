quantidade = int(input("Digite a quantidade produzida hoje: "))
meta = 1000

if quantidade >= meta:
    print("Meta atingida! Parabéns!")
else:
    print(f"Faltam {meta - quantidade} unidades para atingir a meta.")