import pygame
import random

pygame.init()

LARGEUR = 1500
HAUTEUR = 1100
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

perso_taille = 15
perso_pos = [400, 300]
perso_vitesse = 1

class Zombie:
    def __init__(self):
        self.taille = 10
        self.pos = [random.randint(0, LARGEUR-self.taille), random.randint(0, HAUTEUR-self.taille)]
        self.vitesse = 0.1
        self.couleur = (26, 162, 53)
        
    def affichage(self):
        pygame.draw.circle(fenetre, self.couleur, self.pos, self.taille)
        
    def mvt(self):
        if self.pos[0] < perso_pos[0]:
            self.pos[0] += self.vitesse
        if self.pos[0] > perso_pos[0]:
            self.pos[0] -= self.vitesse
        if self.pos[1] < perso_pos[1]:
            self.pos[1] += self.vitesse
        if self.pos[1] > perso_pos[1]:
            self.pos[1] -= self.vitesse
        
            
lst_zmb = [Zombie() for k in range(15)]
            

running = True
while running:  
    fenetre.fill((0, 0, 0))
    pygame.draw.circle(fenetre, (255, 255, 255), perso_pos, perso_taille)
    
    for zmb in lst_zmb:
        zmb.affichage()
        zmb.mvt()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        perso_pos[0] -= perso_vitesse
    if keys[pygame.K_RIGHT]:
        perso_pos[0] += perso_vitesse
    if keys[pygame.K_UP]:
        perso_pos[1] -= perso_vitesse
    if keys[pygame.K_DOWN]:
        perso_pos[1] += perso_vitesse

    if perso_pos[0] < 0:
        perso_pos[0] = 0
    if perso_pos[0] > LARGEUR - perso_taille:
        perso_pos[0] = LARGEUR - perso_taille
    if perso_pos[1] < 0:
        perso_pos[1] = 0
    if perso_pos[1] > HAUTEUR - perso_taille:
        perso_pos[1] = HAUTEUR - perso_taille

    pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
