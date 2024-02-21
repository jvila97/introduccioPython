import random
def dau_6():
    return random.randint(1, 6)

resultat_tirada = dau_6()
print(resultat_tirada)

def daus_6(num_daus):
    resultats = [random.randint(1, 6) for _ in range(num_daus)]
    return resultats

num_llençades = int(input("¿Quants daus vols llençar? "))

resultat =  daus_6(num_llençades)

print("Resultat: ", resultat)



def dau_x(num_cares):
    if num_cares < 2:
        return "Mierda enbotellada"

    resultat_tirada = random.randint(1, num_cares)
    return resultat_tirada


num_cares_dau = int(input("De quantes cares vols que sigui el dau? "))

resultat_tirada = dau_x(num_cares_dau)
print("El resultat de la tirada és:", resultat_tirada)
