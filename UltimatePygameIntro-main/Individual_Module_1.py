import pygame
from sys import exit

# Starting variables
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Individual Module #1")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font\Pixeltype.ttf", 50)

# Surfaces
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Text surface
text_surface = test_font.render("Jump over the snails to survive!", False, (64,64,64))
text_rectangle = text_surface.get_rect(center = (400, 50))

# Snail surfaces
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (600, 300))
snail_x_pos =  600

# Player surfaces
player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# Start the game, loop it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Jumping
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom == 300:
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom == 300:
                player_gravity = -20

# Draw surfaces
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_rectangle)
    pygame.draw.rect(screen, "#c0e8ec", text_rectangle,6)
    screen.blit(text_surface, text_rectangle)

# Draw characters
    snail_rectangle.x -= 5
    if snail_rectangle.right < 0:
        snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)

    # Player stuff
    player_gravity += 1
    player_rectangle.y += player_gravity
    if player_rectangle.bottom >= 300:
        player_rectangle.bottom = 300
    screen.blit(player_surface, player_rectangle)

# Collisions
    if snail_rectangle.colliderect(player_rectangle):
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)