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

    if userInput[pygame.K_LEFT]:
        x -= vel
    if userInput[pygame.K_RIGHT]:
        x += vel
    if userInput[pygame.K_UP]:
        y -= vel
    if userInput[pygame.K_DOWN]:
        y += vel

    pygame.time.delay(50)

    pygame.display.update()




