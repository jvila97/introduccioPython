paraules = []

while True:
    paraula = input("Introdueix una paraula (o escriu 'final' per acabar): ")

    if paraula.lower() == 'final':
        break

    paraules.append(paraula)
    
paraula_a_buscar = input("Introdueix la paraula a buscar: ")

vegades = paraules.count(paraula_a_buscar)
print(f"La paraula '{paraula_a_buscar}' estava a la llista {vegades} vegades.")

paraules = [paraula for paraula in paraules if paraula != paraula_a_buscar]

print("Llista actualitzada:", paraules)
