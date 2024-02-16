try:
    numero = int(input("Introdueix un numero: "))
    
    suma_impares = sum(i for i in range(1, numero + 1) if i % 2 != 0)

    print(f"La suma de numeros impars entre 1 i {numero} es: {suma_impares}")

except ValueError:
    print("Siusplau, introdueix un numero sancer valid.")
