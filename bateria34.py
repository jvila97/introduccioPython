def suma_numeros():
    opcio = input("Vols sumar els números parells o senars? (p/s): ")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    suma = 0
    if opcio == "p":
        for num in nums:
            if num % 2 == 0:
                suma += num
    elif opcio == "s":
        for num in nums:
            if num % 2 != 0:
                suma += num
    else:
        print("Opció no vàlida")
        return
    print(f"La suma dels números {opcio} és: {suma}")

suma_numeros()
