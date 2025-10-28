
producao_real = float(input("Digite a produção real: "))
producao_esperada = float(input("Digite a produção esperada: "))

eficiencia = (producao_real / producao_esperada) * 100

if eficiencia >= 90:
    classificacao = "Excelente"
elif 70 <= eficiencia < 90:
    classificacao = "Boa"
else:
    classificacao = "Precisa melhorar"

print(f"\nEficiência: {eficiencia:.2f}%")
print(f"Classificação: {classificacao}")
