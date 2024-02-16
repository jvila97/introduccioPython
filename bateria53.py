numeros_parells = []
numeros_senars = []

while True:
    entrada = input("Introdueix un número enter (o escriu 'final' per acabar): ")

    if entrada.lower() == 'final':
        break
    
    try:
        numero = int(entrada)

        if numero % 2 == 0:
            numeros_parells.append(numero)
        else:
            numeros_senars.append(numero)
          
print(f"Números parells introduïts: {numeros_parells}")
print(f"Números senars introduïts: {numeros_senars}")
