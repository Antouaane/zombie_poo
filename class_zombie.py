import pygame
import random

pygame.init()

LARGEUR = 2300
HAUTEUR = 1300
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

perso_taille = 15
perso_pos_x = 400
perso_pos_y = 300
perso_vitesse = 5

class Zombie:
    def __init__(self):
        self.taille = 10
        self.x = random.randint(0, LARGEUR - self.taille)
        self.y = random.randint(0, HAUTEUR - self.taille)
        self.vitesse = 1
        self.couleur = (26, 162, 53)
        
    def affichage(self):
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.taille)
        
    def mvt(self, target_x, target_y):
        distance_x = target_x - self.x
        distance_y = target_y - self.y
        distance = (distance_x**2 + distance_y**2)**0.5
        
        if distance < 1000:
            if self.x < perso_pos_x:
                self.x += self.vitesse
            if self.x > perso_pos_x:
                self.x -= self.vitesse
            if self.y < perso_pos_y:
                self.y += self.vitesse
            if self.y > perso_pos_y:
                self.y -= self.vitesse
        else:
            self.x = self.x
            self.y = self.y
        
            
lst_zmb = [Zombie() for k in range(15)]
            

running = True
while running:  
    fenetre.fill((0, 0, 0))
    pygame.draw.circle(fenetre, (255, 255, 255), (perso_pos_x, perso_pos_y), perso_taille)
    
    for zmb in lst_zmb:
        zmb.affichage()
        zmb.mvt(perso_pos_x, perso_pos_y)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        perso_pos_x -= perso_vitesse
    if keys[pygame.K_RIGHT]:
        perso_pos_x += perso_vitesse
    if keys[pygame.K_UP]:
        perso_pos_y -= perso_vitesse
    if keys[pygame.K_DOWN]:
        perso_pos_y += perso_vitesse

    if perso_pos_x < 0:
        perso_pos_x = 0
    if perso_pos_x > LARGEUR - perso_taille:
        perso_pos_x = LARGEUR - perso_taille
    if perso_pos_y < 0:
        perso_pos_y = 0
    if perso_pos_y > HAUTEUR - perso_taille:
        perso_pos_y = HAUTEUR - perso_taille

    pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
