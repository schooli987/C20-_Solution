import pygame
import pymunk
import pymunk.pygame_util


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pymunk Physics Setup")
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 981)  # Gravity pointing downwards
draw_options = pymunk.pygame_util.DrawOptions(screen)

running = True
while running:
    screen.fill((0, 0, 0))  # Black background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    space.step(1/60)  # Update physics simulation
    space.debug_draw(draw_options)  # Draw physics objects
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


