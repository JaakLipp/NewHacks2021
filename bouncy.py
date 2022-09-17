import pygame

print("Hello World!")
pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
crashed = False

white = (255, 255, 255)
red = (255, 0, 0)
g = 9.8 / 60
x = 200
y = 0
vy = 0
vx = 5

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.fill(white)

    vy += g
    y += vy
    x += vx

    if y > 450:
        vy = -vy

    if x > 700 or x < 0:
        vx = -vx

    pygame.draw.rect(gameDisplay, red, (x, y, 100, 150))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
