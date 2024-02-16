numeros = []

while True:
    entrada = input("Introdueix un número enter (o escriu 'final' per acabar): ")

    if entrada.lower() == 'final':
        break
    
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Si us plau, introdueix un número enter vàlid o escriu 'final' per acabar.")

suma_total = sum(numeros)
print(f"La suma dels números introduïts és: {suma_total}")
