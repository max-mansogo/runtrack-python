
#calcule vertical
def calcule_dv(hauteur_escalier, fois_toilettes):
    distance_vertical = hauteur_escalier * fois_toilettes
    return distance_vertical

#calcule horizontal
def calcule_dh(num_mésures, dh):
    distance_totale = num_mésures * dh
    return distance_totale

#distance totale
import math

def calcule_dt(dv, dh):
    distance_totale = math.sqrt(dv**2 + dh**2)
    return distance_totale

# distance totale par semaine
def calcule_dts(distance_totale, fois_toilettes, jours_semaine):
    distance_hebdomadaire = distance_totale * fois_toilettes * jours_semaine
    return distance_hebdomadaire

# calcule total
def calcule_ds_gardien(num_mésures, hauteur_escalier, fois_toilettes, dh):
    dv = calcule_dv(hauteur_escalier, fois_toilettes)
    distance_totale = calcule_dt(dv, dh)
    distance_totale = calcule_dts(distance_totale, fois_toilettes, 7)
    return distance_totale

num_mésures = 100
hauteur_escalier = 20
fois_toilettes = 5
dh = 30

distance_hebdomadaire = calcule_ds_gardien(num_mésures, hauteur_escalier, fois_toilettes, dh)
print(f"Pour {num_mésures} étapes de {hauteur_escalier} cm, le gardien parcourt {distance_hebdomadaire:.2f} m par semaine.")
