import pygame


pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")



# define the players starting variables
x = 250 # initial positions
y = 250 # initial positions
radius = 15 #this circle to 15 pix
vel_x = 10 # movement speed
vel_y = 10
jump = False

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
        x -= vel_x
    if userInput[pygame.K_RIGHT] and x < 500:
        x += vel_x

    if jump is False and userInput [pygame.K_SPACE]:
        jump = True

    if jump is True:
        y -= vel_y
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10
    if userInput[pygame.K_UP] and y > 0:
        y -= vel_y
    if userInput[pygame.K_DOWN] and y < 500:
        y += vel_y

    pygame.time.delay(40)

    pygame.display.update()