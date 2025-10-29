import random

leitura_sensor = random.randint(-50, 150)

print(f"Leitura do sensor: {leitura_sensor}")

if 1 <= leitura_sensor <= 100:
    print("Sensor OK")
else:
    print("Sensor com problema")
