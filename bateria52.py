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

if numeros:
    suma_total = sum(numeros)
    valor_maxim = max(numeros)
    valor_minim = min(numeros)

    print(f"La suma dels números introduïts és: {suma_total}")
    print(f"El valor màxim de la llista és: {valor_maxim}")
    print(f"El valor mínim de la llista és: {valor_minim}")
else:
    print("No s'han introduït números per calcular la suma, el valor màxim i el valor mínim.")
