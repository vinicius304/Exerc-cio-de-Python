nome_materia_prima = "Parafusos M8"
limite_alerta = 50
quantidade_sugerida_reposicao = 1000

print(f"--- GERENCIAMENTO DE ESTOQUE: {nome_materia_prima} ---")


while True:
    try:
        estoque_atual = int(input(f"Digite a quantidade atual de '{nome_materia_prima}' em estoque: "))
        if estoque_atual >= 0:
            break
        else:
            print("A quantidade em estoque não pode ser negativa. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"\nEstoque atual reportado: {estoque_atual} unidades.")


if estoque_atual < limite_alerta:
    print("\n\n*** ALERTA DE ESTOQUE BAIXO! ***")
    print(f"O estoque de {nome_materia_prima} está abaixo do limite crítico de {limite_alerta} unidades.")
    print("---------------------------------")
    print(f"SUGESTÃO DE REPOSIÇÃO:")
    print(f"  Realizar pedido de {quantidade_sugerida_reposicao} unidades.")
    print(f"  Estoque futuro estimado: {estoque_atual + quantidade_sugerida_reposicao} unidades (após reposição).")
    print("---------------------------------")
else:
    print("\nSTATUS: Estoque OK.")
    print(f"O estoque atual de {nome_materia_prima} ({estoque_atual} unidades) está acima do limite de alerta ({limite_alerta} unidades).")