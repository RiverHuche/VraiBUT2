import pygame
from boite_base import Boite

class BoiteOrientable(Boite):
    def __init__(self, l_min, h_min, couleur, orientation_h, enfants):
        self.largeur_min = l_min
        self.hauteur_min = h_min
        self.couleur = couleur
        self.orientation_horizontale = orientation_h
        self.enfants = enfants

    def hauteur_reelle(self):            
        # TODO question 10
        return 74

    # En dessous de cette ligne, circulez il n'y a rien à voir!


































    
    
    def affiche(self, indent = 0):
        orientation = "H" if self.orientation_horizontale else "V"
        print(" " * indent, "- orientation: {}; l_min: {} × h_min: {}".format(orientation, self.largeur_min, self.hauteur_min))
        for e in self.enfants:
            e.affiche(indent = indent + 2)

    def affiche_dims_reelles(self, indent = 0):
        orientation = "H" if self.orientation_horizontale else "V"
        print(" " * indent, "- orientation: {}; l_min: {} × h_min: {} => l_reelle: {} × h_reelle:  {}".format(orientation, self.largeur_min, self.hauteur_min, self.largeur_reelle(), self.hauteur_reelle()))
        for e in self.enfants:
            e.affiche_dims_reelles(indent = indent + 2)

    def dessine(self, surface, x=0, y=0):
        w = self.largeur_reelle()
        h = self.hauteur_reelle()
        pygame.draw.rect(surface, self.couleur, (x, y, w, h), border_radius=5)
        y_enfants = y
        x_enfants = x
        for e in self.enfants:
            e.dessine(surface, x_enfants, y_enfants)
            if self.orientation_horizontale:
                x_enfants += e.largeur_reelle()
            else:
                y_enfants += e.hauteur_reelle()

    # Ci-dessous, implémentation de largeur_reelle, ne pas regarder
    #





















    
    # N'gai, n'gha'ghaa, bugg-shoggog, y'hah; Yog-Sothoth, Yog-Sothoth...
    # OGTHROD AI'F GEB'L--EE'H YOG-SOTHOTH 'NGAH'NG AI'Y ZHRO





















    # N'insistez pas, ça ne vous aidera pas
    


















    
    
    def transposee(self):
        enfants_transposes = [e.transposee() for e in self.enfants]
        b = BoiteOrientable(self.largeur_min, self.hauteur_min,
                            self.couleur, not self.orientation_horizontale,
                            enfants_transposes)
        return b

    def largeur_reelle(self):
        return self.transposee().hauteur_reelle()


    # Voilà, ça ne vous a pas aidé
