import pygame

import object as obj

import level as lv

from book import text

import players_data as p_d

import datetime

class Menu:
    def __init__(self, name, render_list):
        self. name = name

        self.small_menu = obj.Object(name = 'small_menu', init_pos = (448, 64), init_pos_z = 1, order_frames = ('menu_small',), all_objects = render_list)

        self.theme = obj.Object(name = 'theme', init_pos = (0, 128), init_pos_z = 1, order_frames = ('theme',), all_objects = render_list)

        #                                                        v this is x offset of the hole menu it could be a variable but is not a necessity
        self.background = obj.Object(name = 'menu', init_pos = (128, 0), init_pos_z = 1, order_frames = ('menu_large',), order_sounds = ('click',), all_objects = render_list)
        self.background.set_cur_sound_volume(0.5)
        # to all pages with runk greater than 1
        self.main = obj.Object(name = 'main', init_pos = (128 + 80, 164), init_pos_z = 1.1, order_frames = ('main',), all_objects = render_list)
        self.main.change_active_state()
        # page_1
        self.player_name = obj.Object(name = 'name_input', init_pos = (128 + 32, 100), init_pos_z = 1.1, order_frames = ('name_input',), all_objects = render_list)
        self.player_name_text = text.Text(128 + 64, 132, None, 20, initial_text = 'cse 47123', max_text = 16)

        self.levels = obj.Object(name = 'levels', init_pos = (128 + 32, 164), init_pos_z = 1.1, order_frames = ('levels',), all_objects = render_list)
        self.keys = obj.Object(name = 'keys', init_pos = (128 + 32, 196), init_pos_z = 1.1, order_frames = ('keys',), all_objects = render_list)
        self.sound = obj.Object(name = 'sound', init_pos = (128 + 128, 164), init_pos_z = 1.1, order_frames = ('sound',), all_objects = render_list)
        self.help = obj.Object(name = 'help', init_pos = (128 + 128, 196), init_pos_z = 1.1, order_frames = ('help',), all_objects = render_list)
        # page_2
        self.level_1 = obj.Object(name = 'level_1', init_pos = (128 + 32, 100), init_pos_z = 1.1, order_frames = ('level_1',), all_objects = render_list)
        self.level_1.change_active_state()
        self.level_2 = obj.Object(name = 'level_2', init_pos = (128 + 32, 132), init_pos_z = 1.1, order_frames = ('level_2',), all_objects = render_list)
        self.level_2.change_active_state()
        self.level_3 = obj.Object(name = 'level_3', init_pos = (128 + 128, 100), init_pos_z = 1.1, order_frames = ('level_3',), all_objects = render_list)
        self.level_3.change_active_state()
        self.final_level = obj.Object(name = 'final_level', init_pos = (128 + 128, 132), init_pos_z = 1.1, order_frames = ('final_level',), all_objects = render_list)
        self.final_level.change_active_state()
        # page_3
        self.buttons_det = obj.Object(name = 'button_details', init_pos = (128 + 32, 100), init_pos_z = 1.1, order_frames = ('but_det',), all_objects = render_list)
        self.buttons_det.change_active_state()
        self.wasd = obj.Object(name = 'WASD', init_pos = (128 + 32, 132), init_pos_z = 1.1, order_frames = ('wasd',), all_objects = render_list)
        self.wasd.change_active_state()
        self.arrows = obj.Object(name = 'ARROWS', init_pos = (128 + 32, 132), init_pos_z = 1.1, order_frames = ('arrows',), all_objects = render_list)
        self.arrows.change_active_state()
        # page_4
        self.sfx_label = obj.Object(name = 'sfx_label', init_pos = (128 + 32, 100), init_pos_z = 1.1, order_frames = ('sfx_label',), all_objects = render_list)
        self.sfx_label.change_active_state()
        self.sfx_bar = obj.Object(name = 'sfx_bar', init_pos = (128 + 128, 100), init_pos_z = 1.1, order_frames = ('bar',), all_objects = render_list)
        self.sfx_bar.change_active_state()
        self.sfx_vol = obj.Object(name = 'sfx_vol', init_pos = (128 + 224, 100), init_pos_z = 1.2, order_frames = ('vol_pad',), all_objects = render_list)
        self.sfx_vol.change_active_state()
        self.sfx_vol.set_scale((0.5, 0.5))

        self.music_label = obj.Object(name = 'music_label', init_pos = (128 + 32, 132), init_pos_z = 1.1, order_frames = ('music_label',), all_objects = render_list)
        self.music_label.change_active_state()
        self.music_bar = obj.Object(name = 'music_bar', init_pos = (128 + 128, 132), init_pos_z = 1.1, order_frames = ('bar',), all_objects = render_list)
        self.music_bar.change_active_state()
        self.music_vol = obj.Object(name = 'music_vol', init_pos = (128 + 224, 132), init_pos_z = 1.2, order_frames = ('vol_pad',), all_objects = render_list)
        self.music_vol.change_active_state()
        self.music_vol.set_scale((0.5, 0.5))
        # page_5
        self.help_details = obj.Object(name = 'help_details', init_pos = (128 + 9, 84), init_pos_z  = 1.1, order_frames = ('help_details',), all_objects = render_list)
        self.help_details.change_active_state()
        # loser image
        self.loser_image = obj.Object(name = 'You_Lost', init_pos = (0, 0), init_pos_z = 1.99, order_frames = ('loser_image',), order_sounds = ('lost',), all_objects = render_list)
        self.loser_image.change_active_state()
        # winner image
        self.winner_image = obj.Object(name = 'You_Won', init_pos = (0, 0), init_pos_z = 1.99, order_frames = ('winner_image',), order_sounds = ('winner',), all_objects = render_list)
        self.winner_image.change_active_state()
        # object to render the list of player's best performances for json file initially visible like menu
        self.best_players = obj.Object(name = 'players_list', init_pos = (128 + 8, 256 - 32), init_pos_z = 1.1, order_frames = ('players',), all_objects = render_list)
        self.loader = p_d.ExampleClass('players_data.json')
        self.data = self.loader.get_json_as_string()
        self.cur_line = 0
        # every higher level obj must have a value for every graphical element in the worst case
        self.menu = 'main'
        self.focus = False # for focusing on name place
        # self.selected_level = 0
        self.selected_level = None
        # page_2 vars
        self.max_level = 1
        # page_3 vars
        self.bool_wasd_arrows = True
        # page_4 vars
        self.sfx_volume = 0.5
        self.music_volume = 0.5
        # every hier level obj must have name and active in this ex background obj holds the menu's active state
        # create mouse events here

    def run(self, chat_book, background_sound, mouse_image, game_events): # it also needs levels here to change their sounds and open them
        if self.background.get_active_state():
            if self.menu == 'main':
                self.player_name.get_cur_frame().set_text(True)
                self.player_name.get_cur_frame().clear_text()

                self.player_name_text.render(self.player_name.get_cur_frame().get_text_surface())

                # All_players that have played already rendered (fast code)
                self.best_players.get_cur_frame().set_text(True)
                self.best_players.get_cur_frame().clear_text()

                lines = self.data.split('\n')
                players_surface = self.best_players.get_cur_frame().get_text_surface()

                self.cur_line += 0.03125
                if  int(self.cur_line) > len(lines) - 8:
                    self.cur_line = 0

                counter = 0
                for index in range(int(self.cur_line / 8) * 8, int(self.cur_line / 8) * 8 + 8):
                    player_text = text.Text(128 + 8, 256 + 4 + counter * 20, None, 20, initial_text = lines[index], max_text = 16)
                    player_text.render(players_surface)
                    counter += 1
                # (fast code ends here)

            for event in game_events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position when a mouse button is pressed
                    x, y = mouse_image.get_pos()
                    # print(f"Mouse X: {x}, Mouse Y: {y}")
                    coll_obj = self.background.all_objects.check_all((x, y))
                    if coll_obj != None:
                        if self.menu == 'main':
                            if coll_obj == self.loser_image:
                                self.loser_image.change_active_state()
                                if not (self.selected_level is None):
                                    if self.selected_level.exit:
                                        self.selected_level = None
                                # print(self.selected_level)

                            elif coll_obj == self.winner_image:
                                self.winner_image.change_active_state()
                                if not (self.selected_level is None):
                                    if self.selected_level.exit:
                                        new_record = {
                                                "name": self.player_name_text.text,
                                                "level": self.selected_level.get_num(),
                                                "life": self.selected_level.player.get_life(),
                                                "magic": self.selected_level.player.get_magic(),
                                                "time": self.selected_level.player.get_time_remaining(),
                                                "date": datetime.datetime.now().date().isoformat()
                                        }
                                        self.loader.update_or_add_record(new_record)
                                        self.data = self.loader.get_json_as_string()
                                        self.selected_level = None
                                # print(self.selected_level)

                            elif coll_obj == self.levels:
                                self.background.play_sound()
                                self.focus = False

                                # set max_level to whatever player playing max level is!
                                lev_num = self.loader.max_level_for_name(self.player_name_text.text)
                                if not lev_num is None:
                                    self.max_level = lev_num + 1

                                # self.background.set_cur_frame_num(1)
                                # self.background.set_pos((0, 0))

                                self.player_name.change_active_state()
                                self.levels.change_active_state()
                                self.keys.change_active_state()
                                self.sound.change_active_state() # False
                                self.help.change_active_state()
                                self.best_players.change_active_state()

                                self.level_1.change_active_state()
                                self.level_2.change_active_state()
                                self.level_3.change_active_state()
                                self.final_level.change_active_state()

                                self.main.change_active_state() # True

                                self.menu = 'levels'
                            elif coll_obj == self.player_name:
                                if self.selected_level == None:
                                    self.background.play_sound()
                                    self.focus = True
                                else:
                                    self.focus = False
                            elif coll_obj == self.keys:
                                self.background.play_sound()
                                self.focus = False

                                # self.background.set_cur_frame_num(1)
                                # self.background.set_pos((0, 0))

                                self.player_name.change_active_state()
                                self.levels.change_active_state()
                                self.keys.change_active_state()
                                self.sound.change_active_state() # False
                                self.help.change_active_state()
                                self.best_players.change_active_state()

                                self.buttons_det.change_active_state()
                                if self.bool_wasd_arrows:
                                    self.wasd.change_active_state()
                                else:
                                    self.arrows.change_active_state()

                                self.main.change_active_state() # True
                                self.main.set_pos((128 + 128, 164))

                                self.menu = 'keys'
                            elif coll_obj == self.sound:
                                self.background.play_sound()
                                self.focus = False

                                # self.background.set_cur_frame_num(1)
                                # self.background.set_pos((0, 0))

                                self.player_name.change_active_state()
                                self.levels.change_active_state()
                                self.keys.change_active_state()
                                self.sound.change_active_state() # False
                                self.help.change_active_state()
                                self.best_players.change_active_state()

                                self.sfx_label.change_active_state()
                                self.sfx_bar.change_active_state()
                                self.sfx_vol.change_active_state()
                                dims = self.sfx_bar.get_cur_frame().get_dims()
                                self.sfx_vol.set_pos((128 +  128 + (dims[0] - 16) * self.sfx_volume, 100))

                                self.music_label.change_active_state()
                                self.music_bar.change_active_state()
                                self.music_vol.change_active_state()
                                dims = self.music_bar.get_cur_frame().get_dims()
                                self.music_vol.set_pos((128 + 128 + (dims[0] - 16) * self.music_volume, 132))

                                self.main.change_active_state() # True

                                self.menu = 'sound'
                            elif coll_obj == self.help:
                                self.background.play_sound()
                                self.focus = False

                                # self.background.set_cur_frame_num(1)
                                # self.background.set_pos((0, 0))

                                self.player_name.change_active_state()
                                self.levels.change_active_state()
                                self.keys.change_active_state()
                                self.sound.change_active_state() # False
                                self.help.change_active_state()
                                self.best_players.change_active_state()

                                self.help_details.change_active_state() # True

                                self.menu = 'help'
                        elif self.menu == 'levels':
                            self.focus = False
                            if coll_obj == self.level_1:
                                self.background.play_sound()

                                mouse_image.set_cur_frame_num(0)

                                selected_level_num = 0
                                if not (self.selected_level is None):
                                    selected_level_num = self.selected_level.get_num()
                                if self.selected_level is None or selected_level_num != 1:
                                    if not (self.selected_level is None):
                                        self.selected_level.remove_from_all_objects()
                                    self.selected_level = lv.Level('level_1', 1, (16, 16), self, self.background.all_objects)
                                self.close()
                                self.selected_level.change_active_state()

                            elif coll_obj == self.level_2:
                                self.background.play_sound()

                                if self.max_level >= 2:

                                    mouse_image.set_cur_frame_num(0)

                                    selected_level_num = 0
                                    if not (self.selected_level is None):
                                        selected_level_num = self.selected_level.get_num()
                                    if self.selected_level is None or selected_level_num != 2:
                                        if not (self.selected_level is None):
                                            self.selected_level.remove_from_all_objects()
                                        self.selected_level = lv.Level('level_2', 2, (-256, -256), self, self.background.all_objects)
                                    self.close()
                                    self.selected_level.change_active_state()

                                else:
                                    mouse_image.set_cur_frame_num(1)
                            elif coll_obj == self.level_3:
                                self.background.play_sound()

                                if self.max_level >= 3:

                                    mouse_image.set_cur_frame_num(0)

                                    selected_level_num = 0
                                    if not (self.selected_level is None):
                                        selected_level_num = self.selected_level.get_num()
                                    if self.selected_level is None or selected_level_num != 3:
                                        if not (self.selected_level is None):
                                            self.selected_level.remove_from_all_objects()
                                        self.selected_level = lv.Level('level_3', 3, (-256, -128), self, self.background.all_objects)
                                    self.close()
                                    self.selected_level.change_active_state()

                                else:
                                    mouse_image.set_cur_frame_num(1)
                            elif coll_obj == self.final_level:
                                self.background.play_sound()

                                if self.max_level >= 4:

                                    mouse_image.set_cur_frame_num(0)

                                    selected_level_num = 0
                                    if not (self.selected_level is None):
                                        selected_level_num = self.selected_level.get_num()
                                    if self.selected_level is None or selected_level_num != 4:
                                        if not (self.selected_level is None):
                                            self.selected_level.remove_from_all_objects()
                                        self.selected_level = lv.Level('final_map', 4, (-256, -256), self, self.background.all_objects)
                                    self.close()
                                    self.selected_level.change_active_state()

                                else:
                                    mouse_image.set_cur_frame_num(1)
                            elif coll_obj == self.main:
                                self.background.play_sound()

                                # self.background.set_cur_frame_num(0)
                                # self.background.set_pos((63, 0))

                                self.player_name.change_active_state()
                                self.levels.change_active_state()
                                self.keys.change_active_state()
                                self.sound.change_active_state() # True
                                self.help.change_active_state()
                                self.best_players.change_active_state()

                                self.level_1.change_active_state()
                                self.level_2.change_active_state()
                                self.level_3.change_active_state()
                                self.final_level.change_active_state()

                                mouse_image.set_cur_frame_num(0)

                                self.main.change_active_state() # False
                                self.main.set_pos((128 + 80, 164))

                                self.menu = 'main'
                        elif self.menu == 'keys':
                            self.focus = False
                            if coll_obj == self.wasd or coll_obj == self.arrows:
                                self.background.play_sound()
                                self.focus = False

                                self.wasd.change_active_state()
                                self.arrows.change_active_state()

                                self.bool_wasd_arrows = not self.bool_wasd_arrows
                                print('Keys state (wasd):', self.bool_wasd_arrows)
                            elif coll_obj == self.main:
                                self.background.play_sound()

                                # self.background.set_cur_frame_num(0)
                                # self.background.set_pos((63, 0))

                                self.player_name.change_active_state()
                                self.levels.change_active_state()
                                self.keys.change_active_state()
                                self.sound.change_active_state() # True
                                self.help.change_active_state()
                                self.best_players.change_active_state()

                                self.buttons_det.change_active_state()
                                if self.bool_wasd_arrows:
                                    self.wasd.change_active_state()
                                else:
                                    self.arrows.change_active_state()

                                self.main.change_active_state() # False
                                self.main.set_pos((128 + 80, 164))

                                self.menu = 'main'
                        elif self.menu == 'sound':
                            self.focus = False
                            if coll_obj == self.sfx_bar:
                                print(self.sfx_bar.name)
                                dims = self.sfx_bar.get_cur_frame().get_dims()
                                self.sfx_vol.set_pos((x - 8, 100))

                                self.sfx_volume = (x - 136 - 128) / (dims[0] - 16)

                                self.background.set_cur_sound_volume(self.sfx_volume)

                                self.loser_image.set_cur_sound_volume(self.sfx_volume)
                                self.winner_image.set_cur_sound_volume(self.sfx_volume)

                                if chat_book != None:
                                    chat_book.book.set_cur_sound_volume(self.sfx_volume)

                                self.background.play_sound()
                            elif coll_obj == self.music_bar:
                                print(self.music_bar.name)
                                dims = self.music_bar.get_cur_frame().get_dims()
                                self.music_vol.set_pos((x - 8, 132))

                                self.music_volume = (x - 136 - 128) / (dims[0] - 16)

                                background_sound.set_cur_sound_volume(self.music_volume)
                            elif coll_obj == self.main:
                                self.background.play_sound()

                                # self.background.set_cur_frame_num(0)
                                # self.background.set_pos((63, 0))

                                self.player_name.change_active_state()
                                self.levels.change_active_state()
                                self.keys.change_active_state()
                                self.sound.change_active_state() # True
                                self.help.change_active_state()
                                self.best_players.change_active_state()

                                self.sfx_label.change_active_state()
                                self.sfx_bar.change_active_state()
                                self.sfx_vol.change_active_state()

                                self.music_label.change_active_state()
                                self.music_bar.change_active_state() # False
                                self.music_vol.change_active_state()

                                self.main.change_active_state() # False
                                self.main.set_pos((128 + 80, 164))

                                self.menu = 'main'
                        elif self.menu == 'help':
                            if coll_obj == self.help_details:
                                self.background.play_sound()
                                self.focus = False

                                # self.background.set_cur_frame_num(0)
                                # self.background.set_pos((63, 0))

                                self.player_name.change_active_state()
                                self.levels.change_active_state()
                                self.keys.change_active_state()
                                self.sound.change_active_state() # True
                                self.help.change_active_state()
                                self.best_players.change_active_state()

                                self.help_details.change_active_state() # False

                                self.menu = 'main'
                elif self.focus:
                    self.player_name_text.handle_event(event)
                    self.player_name_text.update_text_surface()

        else:
            for event in game_events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position when a mouse button is pressed
                    x, y = mouse_image.get_pos()
                    # print(f"Mouse X: {x}, Mouse Y: {y}")
                    coll_obj = self.background.all_objects.check_all((x, y))
                    '''
                    # This was the original P for puse action but is now the new muse action on small menu icon
                    for event in game_events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                    '''
                    if coll_obj == self.small_menu:
                        self.focus = False
                        self.open()
                        self.selected_level.change_active_state()

                        print('All_obects num. in all_object list:')
                        print(len(self.background.all_objects.list_used) + len(self.background.all_objects.list_not_used))
                    
            self.selected_level.run(mouse_image, game_events)

    def close(self):
        # self active
        self.theme.change_active_state()
        self.background.change_active_state() # False
        # page 1 already altered in the menu page 1 to False

        # page 2
        self.level_1.change_active_state()
        self.level_2.change_active_state()
        self.level_3.change_active_state()
        self.final_level.change_active_state()
        self.main.change_active_state() # False

        # page 3 already altered in the menu page 1 to False
        # page 4 already altered in the menu page 1 to False

        self.menu = 'main' #Reset menu to main

    def open(self):
        # self active
        # reset the menu in the page 1 dims
        # self.background.set_cur_frame_num(0)
        # self.background.set_pos((63, 0))

        self.theme.change_active_state()
        self.background.change_active_state() # True

        self.background.play_sound()

        # open on page 1
        self.player_name.change_active_state()
        self.levels.change_active_state()
        self.keys.change_active_state()
        self.sound.change_active_state() # True
        self.help.change_active_state()
        self.best_players.change_active_state()