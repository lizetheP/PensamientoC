saldo = int(input("Introduce el saldo: "))
if saldo > 1000000:
    print("Excelente_cliente")
elif saldo > 100000 and saldo <=1000000:
    print("Buen_cliente")
elif saldo > 2000 and saldo <= 100000:
    print("Cliente_promedio")
elif saldo >= 0 and saldo <= 2000:
    print("Cliente_saldo_insuficiente")
else:
    print("Y_tu_dinero")

    