print("--- CONTROLE DE VELOCIDADE DA ESTEIRA ROLANTE ---")


while True:
    tipo_produto = input("Digite o tipo de produto (A, B ou C): ").upper() 
    
    if tipo_produto in ["A", "B", "C"]:
        break
    else:
        print("Tipo de produto inválido. Por favor, digite A, B ou C.")

velocidade_esteira = 0


if tipo_produto == "A":
    velocidade_esteira = 1
    nome_velocidade = "Velocidade Mínima"
elif tipo_produto == "B":
    velocidade_esteira = 2
    nome_velocidade = "Velocidade Média"
elif tipo_produto == "C":
    velocidade_esteira = 3
    nome_velocidade = "Velocidade Máxima"
else:
    
    print("\nERRO: Tipo de produto não reconhecido após a validação.")
    velocidade_esteira = 0
    nome_velocidade = "Velocidade 0 (Parada de Segurança)"


print("\n--- AJUSTE DA ESTEIRA ---")
print(f"Produto Selecionado: Tipo {tipo_produto}")
print(f"Velocidade Ajustada: {velocidade_esteira} ({nome_velocidade})")