print("--- CLASSIFICAÇÃO DE PRODUTOS FINAIS ---")


PESO_IDEAL_MIN = 95.0
PESO_IDEAL_MAX = 105.0
TOLERANCIA_MAX_VARIACOES = 115.0
TOLERANCIA_MIN_VARIACOES = 85.0


while True:
    try:
        peso = float(input("\nDigite o peso do produto (em gramas): "))
        if peso > 0:
            break
        else:
            print("O peso deve ser um valor positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o peso.")


while True:
    possui_defeitos = input("O produto possui defeitos visíveis (S/N)? ").upper()
    if possui_defeitos in ["S", "N"]:
        break
    else:
        print("Resposta inválida. Digite 'S' para Sim ou 'N' para Não.")


print("\n--- RESULTADO DA CLASSIFICAÇÃO ---")


if PESO_IDEAL_MIN <= peso <= PESO_IDEAL_MAX and possui_defeitos == "N":
    print("CLASSIFICAÇÃO: PREMIUM")
    print("Critérios atendidos: Peso ideal e zero defeitos.")


elif peso < TOLERANCIA_MIN_VARIACOES or peso > TOLERANCIA_MAX_VARIACOES or possui_defeitos == "S":
    print("CLASSIFICAÇÃO: REJEITADO")
    print("Motivo:")
    if possui_defeitos == "S":
        print("- Possui defeitos visíveis.")
    if peso < TOLERANCIA_MIN_VARIACOES or peso > TOLERANCIA_MAX_VARIACOES:
        print(f"- Peso ({peso:.2f}g) está fora da tolerância de {TOLERANCIA_MIN_VARIACOES}g a {TOLERANCIA_MAX_VARIACOES}g.")


else:
    print("CLASSIFICAÇÃO: STANDARD")
    print("Critérios: Pequenas variações de peso, mas dentro da tolerância aceitável.")
    print(f"Detalhe: Peso de {peso:.2f}g (fora da faixa ideal, mas dentro da faixa de tolerância).")