import pygame
import sys


class Balle():
    def __init__(self, position_x  , position_y , vitesse_x , vitesse_y  , couleur , taille ):
        self.position_x = position_x
        self.position_y = position_y
        self.vitesse_x = vitesse_x
        self.vitesse_y = vitesse_y
        self.couleur = couleur
        self.taille = taille

    def avance(self,t, max_x, max_y):
        x = self.position_x
        y = self.position_y
        dx = self.vitesse_x
        dy = self.vitesse_y
        x = int(x+dx * (t/1000)) % max_x
        y = int(y +dy * (t/1000)) % max_y
        self.position_x = int(x)
        self.position_y = int(y)
    
    def dessine(self, s):
        position = (int(self.position_x),int(self.position_y))
        pygame.draw.circle(s, self.couleur,position,self.taille)

