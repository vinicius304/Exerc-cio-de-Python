temperatura = float(input("Digite a temperatura atual (°C): "))

if temperatura > 80:
    print("Alerta! Temperatura crítica!")
elif 60 <= temperatura <= 80:
    print("Aviso: Temperatura elevada.")
else:
    print("Temperatura normal.")