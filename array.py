comunitat = ["Gandalf", "Legolas", "Gimli","Aragorn","Merry","Pippin","Frodo","Sam","Boromir"]
# Primer element
print(comunitat[0])
#L'ultim element
print(comunitat[len(comunitat)-1])
#L'element del mig
print(comunitat[int(len(comunitat)/2)])
#L'element que alfabèticament va primer.
comunitat.sort()
print(comunitat[0])
#L'element que alfabèticament va darrer.
comunitat.sort()
print(comunitat[8])
#Elimina "Aragorn" de la llista y mostra l'element que va alfabèticament primer.
comunitat.remove("Aragorn")
comunitat.sort()
primer = comunitat[0]
print(primer)
#Afegeix "Arwen" a la llista y mostra la llista ordenada alfabèticament.
comunitat.append("Arwen")
comunitat.sort()
print(comunitat[0])
