import pygame

import dynamic_object as dy_obj

# player is part of the map class as monster and other things like keys boxes fierballs and other dynamic objects
class Fier:
    def __init__(self, menu, map, master, init_dir, init_pos, all_objects):
        self.master = master
        
        self.image = dy_obj.DynamicObject(menu, map, 'player_fier', init_pos, 0, order_frames = (
            'f_r_0',
            'f_r_1',
            'f_r_u_0',
            'f_r_u_1',
            'f_u_0',
            'f_u_1',
            'f_u_l_0',
            'f_u_l_1',
            'f_l_0',
            'f_l_1',
            'f_l_d_0',
            'f_l_d_1',
            'f_d_0',
            'f_d_1',
            'f_d_r_0',
            'f_d_r_1',
            'fier_expl_small'
            ), order_animations = ((0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15)), order_sounds = ('fier', 'explosion'), all_objects = all_objects)
        if init_dir == (1, 0):
            self.image.set_cur_animation(0)
        elif init_dir == (1, -1):
            self.image.set_cur_animation(1)
        elif init_dir == (0, -1):
            self.image.set_cur_animation(2)
        elif init_dir == (-1, -1):
            self.image.set_cur_animation(3)
        elif init_dir == (-1, 0):
            self.image.set_cur_animation(4)
        elif init_dir == (-1, 1):
            self.image.set_cur_animation(5)
        elif init_dir == (0, 1):
            self.image.set_cur_animation(6)
        elif init_dir == (1, 1):
            self.image.set_cur_animation(7)
        
        self.image.set_frame_time(2)

        self.speed = master.speed * 2

        self.init_dir = init_dir

        self.not_expl = True
        self.explosion_time = 0
        self.max_expl_time = 16

    # every objects logic runs from level!
    # monsters see the fier not the oposite from the player object in the level it is eazier that way!
    def run(self):
        self.image.run()

        if self.not_expl:
            if self.image.set_dir_from_map_col(self.init_dir) != self.init_dir:
                self.not_expl = False
                self.image.render_obj.set_cur_frame_num(16)
                self.image.render_obj.set_cur_sound_num(1)
                self.image.render_obj.play_sound()
                # self.image.remove_from_all_objects()
                # self.master.fiers.remove(self)
            else:
                self.image.play_cur_animation()

                self.image.change_map_rel_pos(self.image.set_dir_from_map_col((self.init_dir[0] * self.speed, self.init_dir[1] * self.speed)))
        else:
            if self.explosion_time == self.max_expl_time:
                self.image.remove_from_all_objects()
                self.master.fiers.remove(self)
            self.image.render_obj.set_alpha(int(256 * (1- self.explosion_time / self.max_expl_time)))
            self.explosion_time += 1
    
    def change_active_state(self):
        self.image.change_active_state()

    def remove_from_all_objects(self):
        self.image.remove_from_all_objects()