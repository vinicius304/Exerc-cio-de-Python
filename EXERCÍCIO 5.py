hora = int(input("Digite a hora atual (0–23): "))

if 6 <= hora < 12:
    print("Turno: Manhã")
elif 12 <= hora < 18:
    print("Turno: Tarde")
else:
    print("Turno: Noite")