import pygame
import sys

pygame.init()

# Set window properties
screen = pygame.display.set_mode((300, 100), pygame.NOFRAME)
pygame.display.set_caption("Floating Window")

# Colors
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.Font(None, 36)

def draw_button(text, x, y, color):
    button_rect = pygame.Rect(x, y, 70, 40)
    pygame.draw.rect(screen, color, button_rect)
    text_surface = font.render(text, True, black)
    screen.blit(text_surface, (x + 10, y + 5))
    return button_rect

# Floating behavior
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)
    draw_button("Tools", 10, 30, white)
    draw_button("🎤", 90, 30, red)
    draw_button("Settings", 170, 30, white)
    draw_button("?", 250, 30, white)

    pygame.display.flip()

