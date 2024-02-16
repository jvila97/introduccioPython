try:
    numero = int(input("Introduce un número: "))
    
    if numero < 1:
        print("Por favor, introduce un número positivo.")
    else:
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        print(f"Los divisores de {numero} son: {divisores}")

except ValueError:
    print("Por favor, introduce un número entero válido.")
