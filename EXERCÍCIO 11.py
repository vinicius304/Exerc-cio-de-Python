

boas = 0
defeituosas_seguidas = 0

print("=== INSPEÇÃO DE LOTE ===")
print("Digite 'B' para peça BOA e 'D' para peça DEFEITUOSA.\n")

while defeituosas_seguidas < 5:
    peca = input("Informe o resultado da peça (B/D): ").strip().upper()

    if peca == "B":
        boas += 1
        defeituosas_seguidas = 0  
    elif peca == "D":
        defeituosas_seguidas += 1
        print(f"{defeituosas_seguidas} defeituosa(s) consecutiva(s).")
    else:
        print("Entrada inválida! Digite apenas 'B' ou 'D'.")
        continue  

print("\nInspeção encerrada: 5 peças defeituosas seguidas encontradas!")
print(f"Total de peças boas no lote: {boas}")
