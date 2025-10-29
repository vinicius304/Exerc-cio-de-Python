100


consumo_total = 0


for i in range(1, 6):
    consumo = float(input(f"Digite o consumo da máquina {i} (em kWh): "))
    consumo_total += consumo  


print(f"\nO consumo total da fábrica é: {consumo_total:.2f} kWh")
