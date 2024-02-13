import pygame

import object as obj

import menu as mn

from book import image as im

import objects_ordered_rendering as obj_ord_re

import all_textures as all_tx

from book import connection as con

all_tx.collect()

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("HOW TO TRAIN YOUR WIZARD")

# Load and set the custom icon image
icon_image = pygame.image.load("textures/game_logo_2.png")  # Replace with your icon image path
pygame.display.set_icon(icon_image)

game_surf = pygame.Surface((512, 512), pygame.SRCALPHA)
game_rect = pygame.Rect(0, 0, 0, 0) # testing

all_objects = obj_ord_re.OrderedZList(game_surf)

background = obj.Object(name = 'sky', init_pos = (0, 0), init_pos_z = 0, order_frames = ('sky',), order_sounds = ('game_music',), all_objects = all_objects)
background.set_cur_sound_volume(0.5) # in the final state the volume will be 0.5 !!!
background.loop_sound()

game_cursor = obj.Object('cursor', init_pos = (0, 0), init_pos_z = 2, order_frames = ('magic_cursor','locked_level'), all_objects = all_objects)
pygame.mouse.set_visible(False)

vfx_objects = [] # to pass them inside the menu and change their sound volume at once, objects like the game_cursor

main_menu = mn.Menu('main_menu', all_objects)

if con.is_internet_connected():
    chat_book = im.Book('magic_book', all_objects)
else:
    chat_book = None

    no_internet_logo = obj.Object(name = 'no internet for chat:(', init_pos = (448, 0), init_pos_z = 1.94, order_frames = ('no_internet',), all_objects = all_objects)

# map_1 = mp.Map('map_1', 1, all_objects, main_menu)
# map_2 = mp.Map('map_2', 2, all_objects, main_menu)


# Main game loop

# Frames counter
frame = 0

running = True
while running:
    game_events = pygame.event.get()
    for event in game_events:
        if event.type == pygame.QUIT:
            running = False
    
    # Check if the window is active (not minimized)
    if pygame.display.get_active():
        # Book activations
        if not chat_book is None:
            chat_book.open_close(game_cursor, game_events)

        # Menu activations
        if chat_book is None:
            main_menu.run(None, background, game_cursor, game_events)
        else:
            if chat_book.state == 'closed':
                main_menu.run(chat_book, background, game_cursor, game_events)

        # Render all_objects
        all_objects.sort_objects_by_z_pos()

        all_objects.render_all()
        # this code gose after all_objects_render.render_all() and it's perpuse is to ensure stop rendering unessesary textsurfaces on objects that have activates the text whene they are done in this frame!
        main_menu.player_name.get_cur_frame().set_text(False)
        if not (chat_book is None):
            chat_book.book.get_cur_frame().set_text(False)

        # lastly render the book's insides
        if not (chat_book is None):
            internet = chat_book.run(game_cursor, game_events)
            if not internet:
                chat_book.book.remove_from_all_objects()
                chat_book = None

                no_internet_logo = obj.Object(name = 'no internet for chat:(', init_pos = (448, 0), init_pos_z = 1.94, order_frames = ('no_internet',), all_objects = all_objects)

        # Scale the surface and render it on the screen
        screen.blit(pygame.transform.scale(game_surf, (1280, 720)), game_rect.topleft)

        # Set costume game cursor at the mouse position
        x, y = pygame.mouse.get_pos()
        x *= 512 / 1280
        y *= 512 / 720
        game_cursor.set_pos((x, y))

        # map_1.set_map_pos((-10*x, -10*y))
        # map_1.play_spooky_sound()

        # map_1.run((-10*x, -10*y))
        # map_2.run((-10*x, -10*y))

        pygame.draw.circle(screen, (255, 255, 255), (1280 // 2, 720 // 2), 2) # test dot for camera

        # Update the display
        pygame.display.flip()

        frame += 1
        # Game doesn't have to print anything anywhere
        # print('Focus on name:', main_menu.focus)

# Quit Pygame
pygame.quit()