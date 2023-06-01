import pygame

# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Drawing Objects")


# Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
UNKNOWN = (101, 33, 20)

# Give a background color to display
display_surface.fill(BLACK)

# Draw shapes on display
# Line (surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, BLUE, (0,0), (100,100), 5)

# Circle (surface, color, center, radius, thickness (put 0 to fill circle completely))
pygame.draw.circle(display_surface, WHITE, (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 190, 0)

# Rectangle (surface, color, (top left x, top left y, width, height),)
pygame.draw.rect(display_surface, MAGENTA, (500, 0, 100, 100))
pygame.draw.rect(display_surface, CYAN, (500, 100, 100, 150))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# End the game
pygame.Quit()