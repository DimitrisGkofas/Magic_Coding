import pygame

import object as obj

import dynamic_object as dy_obj

from book import text

import EXEC

import random as rd

# player is part of the map class as monster and other things like keys boxes fierballs and other dynamic objects
class Riddle:
    def __init__(self, menu, level, map, player, init_pos, riddle_string, all_objects):
        self.menu = menu

        self.master_level = level

        self.my_exe = EXEC.SpellRun()

        self.inputs = ''
        if self.master_level.get_num() == 1:
            self.inputs += 'variable_1 = ' + str(rd.random()) + '\nvariable_2 = ' + str(rd.randint(-10, 10)) + '\n'
        elif self.master_level.get_num() == 2 or self.master_level.get_num() == 3:
            self.inputs += 'table = [' + str(rd.random()) + ',' + str(rd.random()) + ',' + str(rd.random()) + ',' + str(rd.random()) + ']\n'
        elif self.master_level.get_num() == 4:
            self.inputs += "string_1 = 'Hello World!'\n"
            if rd.choice([True, False]):
                self.inputs += "string_2 = 'World!'\n"
            else:
                self.inputs += "string_2 = 'Worlds!'\n"

        print(self.inputs + riddle_string)

        self.my_exe.restricted_exec_run(self.inputs + riddle_string)
        self.test_code_output_list = self.my_exe.get_printed_outputs()

        print(self.test_code_output_list)

        self.player = player

        self.papirus = obj.Object(name = 'papirus', init_pos = (0, 0), init_pos_z = 0.99, order_frames = ('script',), order_sounds = ('paper',), all_objects = all_objects)
        self.papirus.change_active_state()

        self.papirus_text = text.Text(32, 132, None, 16, initial_text = '# Python scripts only!', max_text = 17 * 40)

        self.image = dy_obj.DynamicObject(menu, map, 'player_fier', init_pos = init_pos, init_pos_z = 0, order_frames = ('locked_gate_0', 'locked_gate_1'), order_animations = ((0, 1),), all_objects = all_objects)
        self.image.set_cur_animation(0)
        self.image.set_frame_time(4)

        self.locked = True

        self.see = False

    def render_script(self, surface):
        text_lines = self.papirus_text.text.split('\n')

        for counter, line in enumerate(text_lines):
            render_line = text.Text(32, 132 + counter * 20, None, 16, initial_text = line, max_text = 40)
            render_line.render(surface)

        self.set_script_limits(text_lines)

    def set_script_limits(self, text_lines):
        if self.papirus_text.text.count('\n') > 17 or len(text_lines[-1]) > 40:
            self.papirus_text.text = "# Don't get out of the magic paper!!!"


    def is_locked(self):
        return self.locked
    
    def unlock(self):
        if self.player.get_unlock_num() >= self.master_level.info_boxes[-1].get_unlock_num():
            self.locked = False

    def if_close_and_unlocked_to_see(self):
        return self.see




    def close_level_successfully(self):

        print(self.inputs + self.papirus_text.text)

        self.my_exe.restricted_exec_run(self.inputs + self.papirus_text.text)
        player_code_output_list = self.my_exe.get_printed_outputs()

        print(player_code_output_list)

        if self.test_code_output_list == self.my_exe.get_printed_outputs():
            if not (self.menu.selected_level is None):
                if not self.menu.selected_level.exit:
                    self.menu.focus = False
                    self.menu.open()
                    self.menu.selected_level.change_active_state()
                    # show loser_image first
                    self.menu.winner_image.change_active_state()
                    self.menu.winner_image.play_sound() # testing if this line will play the loser sound

                    self.menu.selected_level.remove_from_all_objects()

                    self.menu.selected_level.exit = True
        else:
            self.papirus_text.text = '# Wrong spell!'

        # End of game's level if the code is successfull!




    def is_player_close_on_click(self, mouse_image, game_events):
        for event in game_events:
            x, y = mouse_image.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and not self.is_locked() and self.image.get_dynamic_dist(self.player.image, (True)) < 2 and x < 384:
                self.see = not self.see
                self.papirus.change_active_state()
                self.papirus.play_sound()
                # reset also players motion to not glitch the game
                self.player.key_states = {
                    pygame.K_d: False,
                    pygame.K_s: False,
                    pygame.K_a: False,
                    pygame.K_w: False,
                    pygame.K_RIGHT: False,
                    pygame.K_DOWN: False,
                    pygame.K_LEFT: False,
                    pygame.K_UP: False
                }
            elif event.type == pygame.KEYDOWN and not self.is_locked() and self.image.get_dynamic_dist(self.player.image, (True)) > 2 and x < 384:
                if  event.key == pygame.K_e:
                    self.close_level_successfully()

    def run(self):
        self.image.run()
        self.image.play_cur_animation()

        self.unlock()

    def change_active_state(self):
        self.image.change_active_state()
        if self.see == True:
            self.papirus.change_active_state()

    def remove_from_all_objects(self):
        self.image.remove_from_all_objects()
        self.papirus.remove_from_all_objects()