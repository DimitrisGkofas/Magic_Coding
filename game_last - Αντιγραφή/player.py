import pygame

import object as obj

import dynamic_object as dy_obj

import fier

import random as rd

# player is part of the map class as monster and other things like keys boxes fierballs and other dynamic objects
class Player:
    # player starts and ends the level other changes will not save the progress!!!
    def __init__(self, menu, level, map, speed, init_pos, all_objects):
        self.master_level = level

        self.image = dy_obj.DynamicObject(menu, map, 'player', init_pos, 0, order_frames = (
            'ri_mo',
            'ri_up_mo_0',
            'ri_up_mo_1',
            'up_mo_0',
            'up_mo_1',
            'up_le_mo_0',
            'up_le_mo_1',
            'le_mo',
            'le_do_mo_0',
            'le_do_mo_1',
            'do_mo_0',
            'do_mo_1',
            'do_ri_mo_0',
            'do_ri_mo_1',
            'ri_st',
            'ri_up_st',
            'up_st',
            'up_le_st',
            'le_st',
            'le_do_st',
            'do_st',
            'do_ri_st'
            ),
            order_animations = (
                (14, 0, 14, 0),
                (21, 12, 21 , 13),
                (20, 10, 20, 11),
                (19, 8, 19, 9),
                (18, 7, 18, 7),
                (17, 5, 17, 6),
                (16, 3, 16, 4),
                (15, 1, 15, 2)
            ), order_sounds = ('steps', 'hit'), all_objects = all_objects)
        
        self.image.set_frame_time(4)
        
        self.sound_cont_playing = self.sound_cont_playing_old = False
        
        self.fiers = []

        self.menu = menu

        self.map = map

        self.speed = speed

        self.magic_key = False

        self.magic_boxes_unlock_order = 1

        self.reading = self.old_reading = False

        self.life = 100 # life gets up with coins only!
        self.magic = 100 # magic gose up by itself
        self.time_remaining = 100

        # self.show_life = obj.Object()
        self.show_life_container = obj.Object(name = 'life', init_pos = (0, 0), init_pos_z = 0.98, order_frames = ('life',), all_objects = all_objects)
        self.show_life_container.change_active_state()
        self.show_life = obj.Object(name = 'life', init_pos = (11, 0), init_pos_z = 0.98, order_frames = (
            'blank',
            'coin_0'
        ), all_objects = all_objects)
        self.show_life.get_cur_frame().scale((11, 2))
        self.show_life.change_active_state()

        # self.show_magic = obj.Object()
        self.show_magic_container = obj.Object(name = 'magic', init_pos = (0, 48), init_pos_z = 0.98, order_frames = ('magic',), all_objects = all_objects)
        self.show_magic_container.change_active_state()
        self.show_magic = obj.Object(name = 'magic', init_pos = (11, 48), init_pos_z = 0.98, order_frames = (
            'blank',
            'elixir'
        ), all_objects = all_objects)
        self.show_magic.get_cur_frame().scale((11, 2))
        self.show_magic.change_active_state()

        # self.show_time = obj.Object()
        self.show_time_container = obj.Object(name = 'time', init_pos = (0, 96), init_pos_z = 0.98, order_frames = ('time',), all_objects = all_objects)
        self.show_time_container.change_active_state()
        self.show_time = obj.Object(name = 'time', init_pos = (11, 96), init_pos_z = 0.98, order_frames = (
            'blank',
            'clock'
        ), all_objects = all_objects)
        self.show_time.get_cur_frame().scale((11, 2))
        self.show_time.change_active_state()


        # Initialize a dictionary to keep track of key states
        self.key_states = {
            pygame.K_d: False,
            pygame.K_s: False,
            pygame.K_a: False,
            pygame.K_w: False,
            pygame.K_RIGHT: False,
            pygame.K_DOWN: False,
            pygame.K_LEFT: False,
            pygame.K_UP: False
        }

        # self.old_dir = (1, 0)

    def blit_all(self):
        # life
        self.show_life.get_cur_frame().clear_texture()
        for counter in range(int(self.life / 10)):
            self.show_life.blit((1, 0), (counter * 8, 0))

        # magic
        self.show_magic.get_cur_frame().clear_texture()
        for counter in range(int(self.magic / 10)):
            self.show_magic.blit((1, 0), (counter * 8, 0))

        # time
        self.show_time.get_cur_frame().clear_texture()
        for counter in range(int(self.time_remaining / 10)):
            self.show_time.blit((1, 0), (counter * 8, 0))

    def get_life(self):
        return round(self.life)
    
    def get_magic(self):
        return round(self.magic)
    
    def get_time_remaining(self):
        return round(self.time_remaining)

    def get_key(self):
        if not (self.master_level.MK is None):
            if self.image.get_dynamic_dist(self.master_level.MK.image, True) < 1:
                self.master_level.MK.image.render_obj.set_cur_sound_num(1)
                self.master_level.MK.image.render_obj.play_sound()
                self.master_level.MK.image.remove_from_all_objects()
                self.master_level.MK = None
                self.magic_key = True

    def get_unlock_num(self):
        return self.magic_boxes_unlock_order
    
    def change_unlock_num(self):
        self.magic_boxes_unlock_order += 1

    def unlock(self):
        for box in self.master_level.info_boxes:
            if self.image.get_dynamic_dist(box.image, True) < 1 and self.have_key() and box.is_locked() and box.get_unlock_num() == self.get_unlock_num():

                if self.get_unlock_num() == len(self.master_level.info_boxes) - 1:
                    box.image.render_obj.set_cur_sound_num(2)
                    box.image.render_obj.play_sound()
                    box.image.render_obj.set_cur_sound_num(0)
                else:
                    box.image.render_obj.play_sound()

                box.unlock()
                self.change_unlock_num()

    def read_box_info(self):
        self.reading = False
        for box in self.master_level.info_boxes:
            if not box.is_locked():
                if self.image.get_dynamic_dist(box.image, True) < 1:
                    box.image.render_obj.set_cur_frame_num(2)
                    self.reading = True
                else:
                    box.image.render_obj.set_cur_frame_num(1)

        if self.reading != self.old_reading:
            box.image.render_obj.set_cur_sound_num(1)
            box.image.render_obj.play_sound()
            self.old_reading = self.reading

    def have_key(self):
        return self.magic_key

    def move_on_key_input(self, game_events):
        for event in game_events:
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_states:
                    self.key_states[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in self.key_states:
                    self.key_states[event.key] = False
        # Calculate the direction based on key states
        dir = (0, 0)
        if self.menu.bool_wasd_arrows:
            if self.key_states[pygame.K_d]:
                dir = (dir[0] + 1, dir[1])
            if self.key_states[pygame.K_s]:
                dir = (dir[0], dir[1] + 1)
            if self.key_states[pygame.K_a]:
                dir = (dir[0] - 1, dir[1])
            if self.key_states[pygame.K_w]:
                dir = (dir[0], dir[1] - 1)
        else:  # Use arrow keys instead of WASD
            if self.key_states[pygame.K_RIGHT]:
                dir = (dir[0] + 1, dir[1])
            if self.key_states[pygame.K_DOWN]:
                dir = (dir[0], dir[1] + 1)
            if self.key_states[pygame.K_LEFT]:
                dir = (dir[0] - 1, dir[1])
            if self.key_states[pygame.K_UP]:
                dir = (dir[0], dir[1] - 1)

        self.image.change_map_rel_pos(self.image.set_dir_from_map_col((dir[0] * self.speed, dir[1] * self.speed)))
         # Play sound and stop it, without overlay
         # Reset keys to False if there is a direction without key_pres
        if dir[0] != 0 or dir[1] != 0:
            self.sound_cont_playing = True
            # self.old_dir = dir
        else:
            self.sound_cont_playing = False

        if self.sound_cont_playing != self.sound_cont_playing_old:
            if self.sound_cont_playing == True:
                self.image.render_obj.play_sound()
            else:
                self.image.render_obj.stop_sound()

        self.sound_cont_playing_old = self.sound_cont_playing

        self.animation_on_key_input(dir)

    def animation_on_key_input(self, dir):
        if dir[0] != 0 or dir[1] != 0:
            self.image.play_cur_animation()

        if dir == (1, 0):
            self.image.set_cur_animation(0)
        elif dir == (1, 1):
            self.image.set_cur_animation(1)
        elif dir == (0, 1):
            self.image.set_cur_animation(2)
        elif dir == (-1, 1):
            self.image.set_cur_animation(3)
        elif dir == (-1, 0):
            self.image.set_cur_animation(4)
        elif dir == (-1, -1):
            self.image.set_cur_animation(5)
        elif dir == (0, -1):
            self.image.set_cur_animation(6)
        elif dir == (1, -1):
            self.image.set_cur_animation(7)

    def get_coin(self):
        for coin in self.master_level.coins:
            if self.image.get_dynamic_dist(coin.image, (True)) < 1 and self.life < 100:
                coin.image.render_obj.play_sound()
                coin.image.remove_from_all_objects()
                self.master_level.coins.remove(coin)

                self.maximize_life()
                break

    def minimize_life(self):
        self.life -= 1
        if self.life <= 0:
            self.close_level_unsuccessfully()

        self.play_hit_sound()
    
    def close_level_unsuccessfully(self):
        if not (self.menu.selected_level is None):
            if not self.menu.selected_level.exit:
                self.menu.focus = False
                self.menu.open()
                self.menu.selected_level.change_active_state()
                # show loser_image first
                self.menu.loser_image.change_active_state()
                self.menu.loser_image.play_sound() # testing if this line will play the loser sound

                self.menu.selected_level.remove_from_all_objects()

                self.menu.selected_level.exit = True

    def maximize_life(self):
        self.life += 10
        if self.life > 100:
            self.life = 100

    def minimize_magic(self):
        self.magic -= 10
        if self.magic < 0:
            self.magic = 0

    def maximize_magic(self):
        self.magic += 0.0625
        if self.magic > 100:
            self.magic = 100

    def minimize_time(self):
        self.time_remaining -= 0.01
        if self.time_remaining <= 0:
            self.close_level_unsuccessfully()


    def play_hit_sound(self):
        if rd.random() > 0.9375:
            self.image.render_obj.set_cur_sound_num(1)
            self.image.render_obj.play_sound()
            self.image.render_obj.set_cur_sound_num(0)

    def add_fier(self, mouse_image, game_events):
        if self.magic > 10:
            for event in game_events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    '''
                    # This was the original F for player's fier but it is better with mouse klick!
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:
                    '''
                    mx, my = mouse_image.get_pos()
                    # because the player is at the center of screen it could be done with p_x, p_y = player.image.render_obj.get_pos(). It is almost equal with 256, 256
                    dx = mx - 256
                    dy = my - 256
                    radius = (dx * dx + dy * dy) ** 0.5
                    mouse_dir = (round(dx / abs(radius)), round(dy / abs(radius)))
                    self.fiers.append(fier.Fier(self.menu, self.map, self, mouse_dir, self.image.rel_pos, self.image.render_obj.all_objects))
                    self.fiers[-1].change_active_state()
                    self.fiers[-1].image.render_obj.play_sound()

                    self.minimize_magic()

    def run(self, mouse_image, game_events):
        self.image.run()
        self.move_on_key_input(game_events)
        
        self.add_fier(mouse_image, game_events)

        for fier in self.fiers:
            fier.run()

        self.blit_all()
        # self.show_life.run()

        self.get_key()

        self.unlock()

        self.read_box_info()

        self.get_coin()

        self.maximize_magic()

        self.minimize_time()
    
    def change_active_state(self):
        self.image.change_active_state()

        self.sound_cont_playing = self.sound_cont_playing_old = False

        for fier in self.fiers:
            fier.change_active_state()

        self.show_life_container.change_active_state()
        self.show_life.change_active_state()

        self.show_magic_container.change_active_state()
        self.show_magic.change_active_state()

        self.show_time_container.change_active_state()
        self.show_time.change_active_state()

        # Reset keys to False

        self.key_states = {
            pygame.K_d: False,
            pygame.K_s: False,
            pygame.K_a: False,
            pygame.K_w: False,
            pygame.K_RIGHT: False,
            pygame.K_DOWN: False,
            pygame.K_LEFT: False,
            pygame.K_UP: False
        }

    def remove_from_all_objects(self):
        self.image.remove_from_all_objects()

        for fier in self.fiers:
            fier.remove_from_all_objects()

        self.show_life_container.remove_from_all_objects()
        self.show_life.remove_from_all_objects()

        self.show_magic_container.remove_from_all_objects()
        self.show_magic.remove_from_all_objects()

        self.show_time_container.remove_from_all_objects()
        self.show_time.remove_from_all_objects()