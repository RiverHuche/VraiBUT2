import pygame

class Boite:
    def __init__(self, largeur_min, hauteur_min, couleur, enfants):
        self.largeur_min = largeur_min
        self.hauteur_min = hauteur_min
        self.couleur = couleur
        self.enfants = enfants

    def hauteur_reelle(self):
        res = self.hauteur_min
        if self.enfants == []:
            return res
        else :
            h = 0 
            for e in self.enfants:
                h += e.hauteur_reelle()
            if h > res:
                return h
        return res

    def largeur_reelle(self):
        # TODO question 6
        return 101

    # En dessous de cette ligne, circulez il n'y a rien à voir!




#Question 60-50-60

























    
    
    def affiche(self, indent = 0):
        print(" " * indent, "- l_min: {} × h_min: {}".format(self.largeur_min, self.hauteur_min))
        for e in self.enfants:
            e.affiche(indent = indent + 2)

    def affiche_dims_reelles(self, indent = 0):
        print(" " * indent, "- l_min: {} × h_min: {} => l_reelle: {} × h_reelle:  {}".format(self.largeur_min, self.hauteur_min, self.largeur_reelle(), self.hauteur_reelle()))
        for e in self.enfants:
            e.affiche_dims_reelles(indent = indent + 2)

    def dessine(self, surface, x=0, y=0):
        w = self.largeur_reelle()
        h = self.hauteur_reelle()
        pygame.draw.rect(surface, self.couleur, (x, y, w, h), border_radius=5)
        y_enfants = y
        for e in self.enfants:
            e.dessine(surface, 0, y_enfants)
            y_enfants += e.hauteur_reelle()
