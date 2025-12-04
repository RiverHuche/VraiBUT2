import pygame
from boite_base import Boite

class BoiteAvecMarge(Boite):
    def __init__(self, largeur_min, hauteur_min, couleur, marge, enfants):
        self.largeur_min = largeur_min
        self.hauteur_min = hauteur_min
        self.couleur = couleur
        self.marge = marge
        self.enfants = enfants

    def hauteur_reelle(self):
        # TODO question 14
        return 147

    def largeur_reelle(self):
        # TODO question bonus A
        return 151


    # En dessous de cette ligne, circulez il n'y a rien à voir!


































    
    
    def affiche(self, indent = 0):
        print(" " * indent, "- l_min: {} × h_min: {}; marge: {}".format(self.largeur_min, self.hauteur_min, self.marge))
        for e in self.enfants:
            e.affiche(indent = indent + 2)

    def affiche_dims_reelles(self, indent = 0):
        print(" " * indent, "- l_min: {} × h_min: {}; marge: {} => l_totale: {} × h_totale:  {}".format(self.largeur_min, self.hauteur_min, self.marge, self.largeur_avec_marge(), self.hauteur_avec_marge()))
        for e in self.enfants:
            e.affiche_dims_reelles(indent = indent + 2)

    def dessine(self, surface, x=0, y=0):
        w_contenu = self.largeur_reelle()
        h_contenu = self.hauteur_reelle()
        x += self.marge
        y += self.marge
        pygame.draw.rect(surface, self.couleur, (x, y, w_contenu, h_contenu), border_radius=5)
        y_enfants = y
        x_enfants = x
        for e in self.enfants:
            e.dessine(surface, x_enfants, y_enfants)
            y_enfants += e.hauteur_reelle() + 2*e.marge









    
