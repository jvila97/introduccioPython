nota = int(input("Introdueix la teva nota: "))

if nota >= 1 and nota <= 4:
    print("Insuficient")
elif nota == 5:
    print("Suficient")
elif nota == 6:
    print("Bé")
elif nota >= 7 and nota <= 8:
    print("Notable")
elif nota >= 9 and nota <= 10:
    print("Excel·lent")
else:
    print("Nota no vàlida. La nota ha d'estar entre 1 i 10.")
