suma = 0
contador = 0

while True:
    try:
        numero = float(input("Introdueix un numero (0 par a sortir): "))
        
        if numero == 0:
            break  # Salir del bucle si se ingresa 0
        
        suma += numero
        contador += 1

    except ValueError:
        print("Por favor, introduce un número válido.")

if contador > 0:
    media = suma / contador
    print(f"La mitja de numeros ingresats es: {media}")
else:
    print("No se han ingresat numeros per calcular la mitja.")
