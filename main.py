import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x, y, R, delta = 400, 300, 100, 10

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
            elif e.key == pygame.K_PERIOD and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                R += delta
            elif e.key == pygame.K_COMMA and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                R = max(1, R - delta)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (x, y), R, 1)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()