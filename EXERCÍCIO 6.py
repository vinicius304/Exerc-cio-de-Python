total = 0

for hora in range(1, 9):
    producao = int(input(f"Digite a produção da hora {hora}: "))
    total += producao

print(f"Total produzido no turno: {total} unidades")