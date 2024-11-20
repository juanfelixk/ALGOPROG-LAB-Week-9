import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    radius = 40
    pygame.draw.circle(screen, 'red', player_pos, radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y - radius > 0:
        player_pos.y -= 200 * dt
    if keys[pygame.K_s] and player_pos.y + radius < screen.get_height():
        player_pos.y += 200 * dt
    if keys[pygame.K_a] and player_pos.x - radius > 0:
        player_pos.x -= 200 * dt
    if keys[pygame.K_d] and player_pos.x + radius < screen.get_width():
        player_pos.x += 200 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()