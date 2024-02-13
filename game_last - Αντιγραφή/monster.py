import pygame

import dynamic_object as dy_obj

import all_maps as all_mp

import magic_key as m_k

import random as rd

import maths

# player is part of the map class as monster and other things like keys boxes fierballs and other dynamic objects
class Monster:
    def __init__(self, menu, level, map, map_num, player, all_objects):
        self.master_level = level

        self.player = player

        self.map_num = map_num

        self.image = dy_obj.DynamicObject(menu, map, 'player_fier', init_pos = (1, 1), init_pos_z = 0, order_frames = (
                            'm_r',
                            'm_r_u',
                            'm_u',
                            'm_u_l',
                            'm_l',
                            'm_l_d',
                            'm_d',
                            'm_d_r'
                            ), order_sounds = ('monster',), all_objects = all_objects)
        
        # for counter in range(len(self.image.render_obj.order_frames)):
            # self.image.render_obj.blit((8, counter), (0, 0))

        self.speed = player.speed * 0.5

        self.magic_key = False

        self.dir = (rd.randint(-1, 1), rd.randint(-1, 1))
        # random init spawn position based on spon map static objects

        # find number of ruptures in this map
        ruptures = 0
        for layer_counter, line in enumerate(all_mp.maps[self.map_num]):
            for counter_x_32, key in enumerate(line):
                if key == 'R42':
                    ruptures += 1
        # chose a random one of those to be spwaned from
        spawn_rupture_num = rd.randint(1, ruptures)

        # actual spawn in that particular paper rupture
        already_spawned = False
        ruptures_counter = 0
        for layer_counter, line in enumerate(all_mp.maps[self.map_num]):
            for counter_x_32, key in enumerate(line):
                if key == 'R42':
                    ruptures_counter +=1
                    if spawn_rupture_num == ruptures_counter and not already_spawned:
                        self.image.set_map_rel_pos((counter_x_32, layer_counter))
                        already_spawned = True

    def get_key(self):
        self.magic_key = True

    def have_key(self):
        return self.magic_key
    
    def give_key(self):
        self.master_level.MK = m_k.MagicKey(self.image.menu, self.image.map, self.player, self.image.get_map_rel_pos(), self.image.render_obj.all_objects)
        self.master_level.MK.change_active_state()
        self.master_level.MK.image.set_cur_animation(0)
        self.master_level.MK.image.render_obj.play_sound()
        self.magic_key = False
    
    def see_player(self, radius):
        pos = self.image.get_map_rel_pos()
        for r in range(int(radius)):
            dx, dy = self.image.get_dynamic_dist(self.player.image, False)
            rad = self.image.get_dynamic_dist(self.player.image, True)
            d_pos = (dx / rad, dy / rad)
            pos = (pos[0] + d_pos[0], pos[1] + d_pos[1])
            if maths.map_state_from_points(self.image.map, pos):
                return False
        return True

    def chase_player(self): # chases player by using image.time to give trigger on whene to set new chase direction
        if self.image.time % self.image.frame_time == 0:
            radius = self.image.get_dynamic_dist(self.player.image, True)
            if radius < 8:
                if self.see_player(radius):
                    dx, dy = self.image.get_dynamic_dist(self.player.image, False)
                    rad = self.image.get_dynamic_dist(self.player.image, True)
                    self.dir = (round(dx / abs(rad)), round(dy / abs(rad)))
                else:
                    self.dir = (rd.randint(-1, 1), rd.randint(-1, 1))
            else:
                self.dir = (rd.randint(-1, 1), rd.randint(-1, 1))

        self.chose_frame_from_dir()
        self.image.time += 1

    def chose_frame_from_dir(self):
        if self.dir == (1, 0):
            self.image.render_obj.set_cur_frame_num(0)
        elif self.dir == (1, 1):
            self.image.render_obj.set_cur_frame_num(7)
        elif self.dir == (0, 1):
            self.image.render_obj.set_cur_frame_num(6)
        elif self.dir == (-1, 1):
            self.image.render_obj.set_cur_frame_num(5)
        elif self.dir == (-1, 0):
            self.image.render_obj.set_cur_frame_num(4)
        elif self.dir == (-1, -1):
            self.image.render_obj.set_cur_frame_num(3)
        elif self.dir == (0, -1):
            self.image.render_obj.set_cur_frame_num(2)
        elif self.dir == (1, -1):
            self.image.render_obj.set_cur_frame_num(1)
    # I am in 2030 lines of code

    def play_random_spooky_sound(self):
        if rd.random() > 0.999:
            self.image.render_obj.play_sound()

    def kill(self): # remove from lavels list and from all_objects!
        if self.image.get_dynamic_dist(self.player.image, True) < 1:
            self.player.minimize_life()
            # print(self.player.life)

    def die(self):
        for fier in self.player.fiers:
            if self.image.get_dynamic_dist(fier.image, True) < 1:
                self.image.render_obj.play_sound()
                self.image.remove_from_all_objects()
                self.master_level.monsters.remove(self)
                if self.have_key():
                    self.give_key()
                break

    # every objects logic runs from level!
    # monsters see the fier not the oposite from the player object in the level it is eazier that way!
    def run(self):
        self.image.run()
        # self.dir = (rd.randint(-1, 1), rd.randint(-1, 1))
        self.chase_player()
        self.kill()
        self.play_random_spooky_sound()
        self.image.change_map_rel_pos(self.image.set_dir_from_map_col((self.dir[0] * self.speed, self.dir[1] * self.speed)))
        # use of level to dispone the monsters from it's list 'levels.monsters'
        # self.image.remove_from_all_objects()
        # self.master_level.monsters.remove(self)
        self.die()

    def change_active_state(self):
        self.image.change_active_state()

    def remove_from_all_objects(self):
        self.image.remove_from_all_objects()