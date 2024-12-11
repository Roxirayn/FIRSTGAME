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
    win.fill((0,0,0))
    pygame.draw.circle(win,(255, 255, 255), (int(x),int(y)), radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel
    if userInput[pygame.K_RIGHT] and x < 500:
        x += vel
    if userInput[pygame.K_UP] and y > 0:
        y -= vel
    if userInput[pygame.K_DOWN] and y < 500:
        y += vel

    pygame.time.delay(40)

    pygame.display.update()