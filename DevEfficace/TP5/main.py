import sys
from affichage import affiche_boite_pygame
from exemples import exemples_parties_12, exemples_partie_3, exemples_partie_4



def affiche_dimensions_exemple(exemple, details=False):
    print("=" * 80)
    if details:
        exemple.affiche_dims_reelles()
    else:
        exemple.affiche()
        print("-" * 80)
        print("Hauteur réelle:", exemple.hauteur_reelle())
        print("Largeur réelle:", exemple.largeur_reelle())
    print("=" * 80)

def choix_partie(partie=-1):
    while not(0 < partie <= 4):
        print("quelle partie traitez-vous actuellement?")
        print("1-2: questions 1 à 6 («Quelques longeurs pour s'échauffer» & «Dans les grandes largeurs»")
        print("3: questions 7 à 10 («Dans tous les sens»)")
        print("4: questions 11 à 14 («Les coudées franches»)")
        try:
            partie = int(input("[1-4] > "))
        except ValueError:
            print("Hein?")
        if partie in (0, 1, 2):        
            return ("Parties 1 & 2", exemples_parties_12)
        elif partie == 3:
            return ("Partie 3", exemples_partie_3)
        elif partie == 4:
            return ("Partie 4", exemples_partie_4)

def choix_exemple(exemples, num_exemple=-1):
    while not (0 <= num_exemple < len(exemples)):
        try:
            num_exemple = int(input("numéro de l'exemple à visualiser? [0 - {}] >".format(len(exemples)-1)))
            return num_exemple
        except ValueError:
            pass
    
        
    
if __name__ == "__main__":
    nom_partie, exemples = choix_partie()
    num_exemple = choix_exemple(exemples)
    exemple = exemples[num_exemple]

    opération = -1
    while not (opération == 5):
        print(nom_partie)
        print("Exemple numéro {}".format(num_exemple))
        print("Que voulez-vous faire?")
        print("0: afficher l'exemple dans la console sans les détails")
        print("1: afficher l'exemple dans la console avec les détails")
        print("2: afficher l'exemple dans pygame")
        print("3: changer d'exemple")
        print("4: changer de partie")
        print("5: quitter")
        try:
            opération = int(input("[0-5] > "))
        except ValueError:
            pass
        
        if opération == 0:
            affiche_dimensions_exemple(exemple)
        elif opération == 1:
            affiche_dimensions_exemple(exemple, details=True)
        elif opération == 2:
            affiche_boite_pygame(exemple)
        elif opération == 3:
            num_exemple = choix_exemple(exemples)
        elif opération == 4:
            nom_partie, exemples = choix_partie()
            num_exemple = choix_exemple(exemples)
        exemple = exemples[num_exemple]
                                
    sys.exit(0)
