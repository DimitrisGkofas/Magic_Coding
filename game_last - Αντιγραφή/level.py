import map as mp

import player as pl

import monster as mn

import info_box as i_b

import gate_riddle as g_r

import coin as cn

import random as rd

import riddle

# Level must have spawn places in order to not get buggy code for this situation is not implemented because every level will have spawn places!
# Also because maps are hand made don't forget to add at least one spawn object inside all_maps module.
# If you do an infinite loop will ocure in monsters constructor! And the game will crash!
# You can make your own module with a time_out logic for monster spawn...

class Level:
    def __init__(self, name, level_num, init_camera_pos, menu, all_objects):
        self.menu = menu

        self.name = name

        self.level_num = level_num - 1

        self.old_menu_state = self.menu.background.get_active_state()

        self.map = mp.Map(self.name, self.level_num, self.menu, all_objects)
        self.camera_pos = init_camera_pos

        self.player = pl.Player(self.menu, self, self.map, 0.1, (4, 13), all_objects)

        self.max_monster_num = 4 * level_num
        self.monsters = []

        self.magic_key = True
        self.MK = None

        self.info_boxes = None
        if level_num == 1:
            self.info_boxes = (
                i_b.InfoBox(self.menu, self.map, self.player, 1, 'l1b0', (1, 4), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 2, 'l1b1', (32 - 4, 4), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 3, 'l1b2', (32 - 4, 8), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 4, 'l1b3', (32 - 4, 12), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 5, 'l1b4', (32 - 4, 16), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 6, 'l1b5', (32 - 4, 20), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 7, 'l1b6', (32 - 8, 20), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 8, 'l1b7', (32 - 12, 20), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 9, 'l1b8', (32 - 12, 24), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 10, 'l1b9', (32 - 12, 28), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 11, 'l1b10', (32 - 8, 28), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 12, 'l1b11', (32 - 4, 28), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 13, 'l1b12', (32 - 4, 30), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 14, 'l1b13', (32 - 8, 30), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 15, 'l1b14', (32 - 12, 30), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 16, 'l1riddle', (1, 32 - 4), all_objects),

                i_b.InfoBox(self.menu, self.map, self.player, 17, 'general_box', (13, 1), all_objects)
            )
            self.magic_gate_riddle = g_r.Riddle(self.menu, self, self.map, self.player, init_pos = (14, 0.5), riddle_string = riddle.level_1, all_objects = all_objects)
            self.coins = [
                cn.Coin(self.menu, self.map, (20, 4), all_objects = all_objects),
                cn.Coin(self.menu, self.map, (20, 8), all_objects = all_objects),
                cn.Coin(self.menu, self.map, (20, 12), all_objects = all_objects),
                cn.Coin(self.menu, self.map, (20, 16), all_objects = all_objects)
            ]
        elif level_num == 2:
            self.info_boxes = (
                i_b.InfoBox(self.menu, self.map, self.player, 1, 'l2b0', (1, 4), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 2, 'l2b1', (32 - 4, 4), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 3, 'l2b2', (32 - 4, 8), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 4, 'l2b3', (32 - 4, 12), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 5, 'l2b4', (32 - 4, 16), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 6, 'l2b5', (32 - 4, 20), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 7, 'l2b6', (32 - 8, 20), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 8, 'l2b7', (32 - 12, 20), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 9, 'l2b8', (32 - 12, 24), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 10, 'l2b9', (32 - 12, 28), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 11, 'l2b10', (32 - 8, 28), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 12, 'l2b11', (32 - 4, 28), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 13, 'l2riddle', (1, 32 - 4), all_objects),

                i_b.InfoBox(self.menu, self.map, self.player, 14, 'general_box', (13, 1), all_objects)
            )
            self.magic_gate_riddle = g_r.Riddle(self.menu, self, self.map, self.player, init_pos = (14, 0.5), riddle_string = riddle.level_2, all_objects = all_objects)
            self.coins = [
                cn.Coin(self.menu, self.map, (20, 4), all_objects = all_objects),
                cn.Coin(self.menu, self.map, (20, 8), all_objects = all_objects),
                cn.Coin(self.menu, self.map, (20, 12), all_objects = all_objects)
            ]
        elif level_num == 3:
            self.info_boxes = (
                i_b.InfoBox(self.menu, self.map, self.player, 1, 'l3b0', (1, 4), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 2, 'l3b1', (32 - 4, 4), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 3, 'l3b2', (32 - 4, 8), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 4, 'l3riddle', (1, 32 - 4), all_objects),

                i_b.InfoBox(self.menu, self.map, self.player, 5, 'general_box', (13, 1), all_objects)
            )
            self.magic_gate_riddle = g_r.Riddle(self.menu, self, self.map, self.player, init_pos = (14, 0.5), riddle_string = riddle.level_3, all_objects = all_objects)
            self.coins = [
                cn.Coin(self.menu, self.map, (20, 4), all_objects = all_objects),
                cn.Coin(self.menu, self.map, (20, 8), all_objects = all_objects)
            ]
        elif level_num == 4:
            self.info_boxes = (
                i_b.InfoBox(self.menu, self.map, self.player, 1, 'fb0', (1, 4), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 2, 'fb1', (2, 5), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 3, 'fb2', (3, 6), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 4, 'fb3', (4, 7), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 5, 'fb4', (5, 8), all_objects),
                i_b.InfoBox(self.menu, self.map, self.player, 6, 'fb5', (1, 32 - 4), all_objects),

                i_b.InfoBox(self.menu, self.map, self.player, 7, 'general_box', (13, 1), all_objects)
            )
            self.magic_gate_riddle = g_r.Riddle(self.menu, self, self.map, self.player, init_pos = (14, 0.5), riddle_string = riddle.level_4, all_objects = all_objects)
            self.coins = [
                cn.Coin(self.menu, self.map, (20, 4), all_objects = all_objects)
            ]

        self.exit = False

        # self.key # the key will also have a dropped bool variable once a random monster with the key value is kelled, 
        # key's droped value will become False or the key will be init. Then no monster will have another key in the future of this map logic.
        # Key will unlock the boxes in this level!
        # Unlock the magic code for the last gate to open and end the level

        #self.box = dy_obj.DynamicObject(self.menu, self.map, 'box_1', (0, 0), 0, order_frames = ('box_open','box_closed'), order_animations = ((0, 1),), all_objects = all_objects)
        #self.box.set_map_rel_pos((2, 2))
        #self.box.set_cur_animation(0)

        #print('Player to box dist:', self.player.image.get_dynamic_dist(self.box, True))

        # Levels main player
        # self.player = pl.Player()
    
    def get_num(self):
        return self.level_num + 1

    def get_level_num(self):
        return self.level_num
    
    def have_key(self):
        return self.magic_key
    
    def give_key(self):
        self.magic_key = False
    
    def add_monster(self):
        if self.max_monster_num > len(self.monsters):
            self.monsters.append(mn.Monster(self.menu, self, self.map, self.get_level_num(), self.player, self.map.floor.all_objects))
            self.monsters[-1].change_active_state()

            if rd.random() > 1- 1/16 and self.have_key():
                self.give_key()
                self.monsters[-1].get_key()

    def run(self, mouse_image, game_events):
        if not self.menu.background.get_active_state():
            if not self.magic_gate_riddle.if_close_and_unlocked_to_see():
                self.map.run(self.camera_pos)

                dims = self.player.image.render_obj.get_cur_frame().get_dims()
                rel_pos = self.player.image.get_map_rel_pos()
                self.set_level_camera_pos((-rel_pos[0] * 32 + 128 - dims[0] * 0.5, -rel_pos[1] * 16 + 169 + dims[1] * 0.5))
                # player's motion by level but it must be in player's class
                # self.player.image.change_map_rel_pos(self.player.set_dir_from_map_col((random.random() * 0.2 - 0.1, random.random() * 0.2 - 0.1)))

                if rd.random() > 0.95:
                    self.add_monster()

                for monster in self.monsters:
                    monster.run()

                if not (self.MK is None):
                    self.MK.run()

                for box in self.info_boxes:
                    box.run()

                '''
                # test prints only game will not print anything anywhere
                print('Fiers count:', len(self.player.fiers))

                print('Monsters count:', len(self.monsters))

                print('All_obects num. in all_object list:')
                print(len(self.menu.background.all_objects.list_used) + len(self.menu.background.all_objects.list_not_used))
                '''
                
                self.magic_gate_riddle.run()

                for coin in self.coins:
                    coin.run()

                self.player.run(mouse_image, game_events) # progress is needed here too!

            # here will probably go the riddle code
            else:
                self.magic_gate_riddle.papirus.get_cur_frame().set_text(True)
                self.magic_gate_riddle.papirus.get_cur_frame().clear_text()

                # self.magic_gate_riddle.papirus_text.render(self.magic_gate_riddle.papirus.get_cur_frame().get_text_surface())
                self.magic_gate_riddle.render_script(self.magic_gate_riddle.papirus.get_cur_frame().get_text_surface())

                for event in game_events:
                    self.magic_gate_riddle.papirus_text.handle_event(event)
                    self.magic_gate_riddle.papirus_text.update_text_surface()

            self.magic_gate_riddle.is_player_close_on_click(mouse_image, game_events)

            # print(self.magic_gate_riddle.papirus_text.text) # test to see if the code is being written correctly

    def change_active_state(self):
        if self.menu.background.get_active_state() != self.old_menu_state:
            self.map.change_active_state()

            self.player.change_active_state()

            for monster in self.monsters:
                monster.change_active_state()

            if not (self.MK is None):
                self.MK.change_active_state()

            for box in self.info_boxes:
                box.change_active_state()

            self.magic_gate_riddle.change_active_state()

            for coin in self.coins:
                coin.change_active_state()

            self.old_menu_state = self.menu.background.get_active_state()
    
    def set_level_camera_pos(self, pos):
        self.camera_pos = pos

    def remove_from_all_objects(self):
        self.map.remove_from_all_objects()

        self.player.remove_from_all_objects()

        for monster in self.monsters:
            monster.remove_from_all_objects()

        if not (self.MK is None):
            self.MK.remove_from_all_objects()

        for box in self.info_boxes:
            box.remove_from_all_objects()

        self.magic_gate_riddle.remove_from_all_objects()

        for coin in self.coins:
            coin.remove_from_all_objects()

