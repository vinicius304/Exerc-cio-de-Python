
horas_operacao = 0


while True:
    horas_operacao += 1
    print(f"Horas de operação: {horas_operacao}")

    
    if horas_operacao == 500:
        print("⚠️ ALERTA: Manutenção preventiva necessária! (500 horas atingidas)")
        break 
