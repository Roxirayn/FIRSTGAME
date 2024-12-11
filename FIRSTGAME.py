import pygame


pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")



# define the players starting variables
x = 250 # initial positions
y = 250 # initial positions
radius = 15 #this circle to 15 pix
vel = 10 # movement speed


# game loop
#it keeps the game running till the user quits.
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


            pygame.display.update()
