producao_total = 0
maior_producao = -1  
linha_maior_producao = 0

print("--- DASHBOARD DE PRODUÇÃO DA FÁBRICA ---")


for i in range(1, 6):
    while True:
        try:
            
            producao_linha = int(input(f"Digite a produção da Linha {i} (em unidades): "))
            if producao_linha >= 0:
                break
            else:
                print("A produção deve ser um valor não negativo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    
    producao_total = producao_total + producao_linha

   
    if producao_linha > maior_producao:
        maior_producao = producao_linha
        linha_maior_producao = i
    
    print(f"-> Produção da Linha {i}: {producao_linha} unidades.")


print("\n========== RELATÓRIO FINAL DE PRODUÇÃO ==========")
print(f"Total de Linhas de Produção: 5")
print(f"Produção Total da Fábrica: {producao_total} unidades")
print("-------------------------------------------------")
print(f"LINHA DE MAIOR DESTAQUE:")
print(f"  Linha Número: {linha_maior_producao}")
print(f"  Produção: {maior_producao} unidades")
print("=================================================")