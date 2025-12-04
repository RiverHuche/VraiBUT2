import pygame

WINDOWWIDTH, WINDOWHEIGHT = 800, 600

class Quitte(Exception ):
    pass

def isQuitEvent(event):
    return (event.type == pygame.QUIT or 
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE))

def handleKey(event, points_trace):
    pass

def handleEvents():
    for event in pygame.event.get():
        # pour chaque évènement depuis le dernier appel de cette fonction
        if isQuitEvent(event):
            raise Quitte

def drawApp(ecran, boite):
    """
    Redessine l'écran.
    """
    ecran.fill((255,255,255)) # on remplit avec du blanc
    boite.dessine(ecran)
    pygame.display.update()

def affiche_boite_pygame(boite):
    pygame.init()
    pygame.display.set_caption('')
    ecran = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    while True:
        try:
            handleEvents()
            drawApp(ecran, boite)
        except Quitte:
            break
        
    pygame.quit()
