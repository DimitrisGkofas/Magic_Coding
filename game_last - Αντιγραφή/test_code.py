import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Create a Pygame Surface (replace this with your game content)
pygame.init()
game_width, game_height = 800, 600
game_surf = pygame.Surface((game_width, game_height))

# Initialize Pygame and OpenGL
pygame.display.set_mode((game_width, game_height), DOUBLEBUF | OPENGL)
glViewport(0, 0, game_width, game_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, game_width, 0, game_height, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Create an OpenGL Texture from the Pygame Surface
texture_id = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, game_width, game_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(game_surf, 'RGBA', 1))

# Scaling factor (adjust as needed)
scale_factor = 2.0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Apply scaling transformation
    glLoadIdentity()
    glTranslatef((game_width * scale_factor - game_width) / 2, (game_height * scale_factor - game_height) / 2, 0)
    glScalef(scale_factor, scale_factor, 1)
    
    # Enable texture mapping and render the texture
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(0, 0)
    glTexCoord2f(1, 0)
    glVertex2f(game_width, 0)
    glTexCoord2f(1, 1)
    glVertex2f(game_width, game_height)
    glTexCoord2f(0, 1)
    glVertex2f(0, game_height)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Swap the OpenGL buffers to display the scaled game surface
    pygame.display.flip()