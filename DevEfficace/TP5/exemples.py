from boite_base import Boite
from boite_orientable import BoiteOrientable
from boite_marge import BoiteAvecMarge
import math

noir = (0,0,0)
gris_clair = (192, 192, 192)
gris_moyen = (127, 127, 127)
gris_fonce = (63, 63, 63)

def creer_exemple_enonce():
    b1   = Boite(60*3, 20*3, gris_fonce, [])
    b2   = Boite(50*3, 20*3, gris_fonce, [])
    b3   = Boite(50*3, 10*3, gris_fonce, [])
    b12  = Boite(10*3, 50*3, gris_moyen, [b1, b2])
    b123 = Boite(70*3, 0, gris_clair, [b12, b3])
    return b123

exemple_enonce = creer_exemple_enonce()

def creer_exemple_parabole():
    petites_boites = []
    grandes_boites = []
    for i in range(60):
        gris = (2*i, 2*i, 2*i)
        nouvelle_boite = Boite(i*i / 5, 5, gris, [])
        petites_boites.append(nouvelle_boite)
    for j in range(0, 70, 4):
        brun = (j, j * 2, 0)
        nouvelle_boite = Boite(0, 0, brun, petites_boites[j:j+4])
        grandes_boites.append(nouvelle_boite)
    return Boite(0, 0, (0,255,9), grandes_boites)

def creer_exemple_binaire(profondeur=3):
    delta_largeur = 800 // profondeur
    hauteur_base = 600 // (2 ** profondeur)
    racine = Boite(delta_largeur*profondeur, hauteur_base, noir, [])
    feuilles = [racine]
    for i in range(profondeur):
        nouvelles_feuilles = []
        for f in feuilles:
            couleur_haut = (30 * i + 15, 0, 30*i + 15)
            couleur_bas = (0, 30 * i + 15, 30*i + 15)
            largeur = delta_largeur * (profondeur - i)
            boite_haut = Boite(largeur, hauteur_base, couleur_haut, [])
            boite_bas = Boite(largeur, hauteur_base, couleur_bas, [])
            f.enfants = [boite_haut, boite_bas]
            nouvelles_feuilles += [boite_haut, boite_bas]
        feuilles = nouvelles_feuilles
    return racine

exemple_parabole = creer_exemple_parabole()

exemples_parties_12 = [exemple_enonce, exemple_parabole, creer_exemple_binaire(3)]

def creer_exemple_orientable_simple():
    b1   = BoiteOrientable(60*3, 30*3, gris_fonce, False, [])
    b2   = BoiteOrientable(50*3, 10*3, gris_fonce, False, [])
    b3   = BoiteOrientable(50*3, 30*3, gris_fonce, False, [])
    b12  = BoiteOrientable(10*3, 0*3, gris_moyen, True, [b1, b2])
    b123 = BoiteOrientable(70*3, 50*3, gris_clair, False, [b12, b3])
    return b123


def creer_exemple_binaire_orientable(profondeur=7):
    phi = (1 + math.sqrt(5)) / 2
    largeur_base = int(800 / pow(phi, profondeur))
    hauteur_base = int(600 / pow(phi, profondeur))
    orientation_h = True
    racine = BoiteOrientable(largeur_base, hauteur_base, noir, orientation_h, [])
    orientation_h = not orientation_h
    feuilles = [racine]
    for i in range(profondeur):
        nouvelles_feuilles = []
        for f in feuilles:
            couleur_1 = (30 * i + 15, 30*i + 15, 0)
            couleur_2 = (0, 30 * i + 15, 30*i + 15)
            boite_1 = BoiteOrientable(largeur_base, hauteur_base, couleur_1, orientation_h, [])
            orientation_h = not orientation_h
            boite_2 = BoiteOrientable(hauteur_base, hauteur_base, couleur_2, orientation_h, [])
            orientation_h = not orientation_h
            f.enfants = [boite_1, boite_2]
            nouvelles_feuilles += [boite_1, boite_2]
        feuilles = nouvelles_feuilles
    return racine



exemples_partie_3 = [creer_exemple_orientable_simple(), creer_exemple_binaire_orientable()]

def creer_exemple_simple_avec_marge():
    b1   = BoiteAvecMarge(50*3, 10*3, gris_fonce, 10, [])
    b2   = BoiteAvecMarge(50*3, 10*3, gris_fonce, 10, [])
    b3   = BoiteAvecMarge(50*3, 20*3, gris_fonce, 0, [])
    b12  = BoiteAvecMarge(80*3, 0*3, gris_moyen, 10, [b1, b2])
    b123 = BoiteAvecMarge(120*3, 150*3, gris_clair, 10, [b12, b3])
    return b123
    

exemples_partie_4 = [creer_exemple_simple_avec_marge()]
