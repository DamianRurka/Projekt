import pygame
pygame.init()
x = 10
box = pygame.Rect(10,10,50,50)
clock = pygame.time.Clock()
delta = 0.0
screen = pygame.display.set_mode((640,420))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    #Odliczanie?
    delta += clock.tick()/1000.0
    while delta > 1/2.0:
        print("hey")
        delta -= 1/2.0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        box.x += 1
    if keys[pygame.K_s]:
        box.y += 1
    if keys[pygame.K_w]:
        box.y -= 1
    if keys[pygame.K_a]:
        box.x -= 1


    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 150, 255),box)
    pygame.display.flip()