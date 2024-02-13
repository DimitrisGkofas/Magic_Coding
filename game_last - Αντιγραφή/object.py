import pygame

import all_textures as all_tx
import static_map_items as st_mp

import all_sounds as all_snd

import texture as tx
import sound as snd

class Object:
    def __init__(self, name, init_pos, init_pos_z, order_frames = None, order_sounds = None, all_objects = None):
        self. name = name

        self.order_frames = []
        self.order_sounds = []

        self.pos = init_pos
        self.pos_z = init_pos_z

        self.scale = (1, 1)

        self.cur_frame_num = 0
        self.cur_sound_num = 0

        self.active = True

        # self.active = True

        # Textures and sounds must be different objects wrong impementation ! (down from here!)
        if order_frames != None:
            for key in order_frames:
                details = all_tx.names[key]
                self.order_frames.append(tx.Texture(details[0], details[1], details[2], details[3], details[4], details[5], details[6]))
            
        if order_sounds != None:
            for key in order_sounds:
                path = all_snd.names[key]
                self.order_sounds.append(snd.SoundPlayer(path))
        
        self.all_objects = None
        if all_objects != None:
            self.all_objects = all_objects
            self.all_objects.list_used.append(self)
    
    def add_frame(self,  key):
        details = all_tx.names[key]
        self.order_frames.append(tx.Texture(details[0], details[1], details[2], details[3], details[4], details[5], details[6]))
    
    def add_map_frame(self,  key):
        details = st_mp.StaticMapItems[key]
        self.order_frames.append(tx.Texture(details[0], details[1], details[2], details[3], details[4], details[5], details[6]))

    def copy_frame(self, other_obj):
        texture = other_obj.get_cur_frame()
        self.order_frames.append(texture)

    # remove frame add sound and remove sound are not a necessity

    # But remove from the render list is mendatory for map objects
    def remove_from_all_objects(self):
        if self in self.all_objects.list_used:
            self.all_objects.list_used.remove(self)
        
        if self in self.all_objects.list_not_used:
            self.all_objects.list_not_used.remove(self)
        
    def render(self, game_surf):
        # if self.active:
        if len(self.order_frames) > 0:
            self.get_cur_frame().render(game_surf, self.pos)
    
    def blit(self, two_order_frames_nums, pos):
        self.order_frames[two_order_frames_nums[0]].blit_on_top(self.order_frames[two_order_frames_nums[1]], pos)

    def set_alpha(self, alpha_value):
        self.get_cur_frame().set_alpha(alpha_value)

    def collision(self, other_pos):
        # if self.active:
        pos_x_start = self.pos[0]
        pos_y_start = self.pos[1]
        dims = self.get_cur_frame().get_dims()
        # print('pos and dims:', self.pos, dims)
        pos_x_end = self.pos[0] + dims[0]
        pos_y_end = self.pos[1] + dims[1]

        if other_pos[0] > pos_x_start and other_pos[0] < pos_x_end and other_pos[1] > pos_y_start and other_pos[1] < pos_y_end:
            return self

    def Scale(self):
        # if self.active:
        self.get_cur_frame().scale(self.scale)

    def set_pos(self, pos):
        self.pos = (pos[0], pos[1])

    def set_pos_z(self, pos_z):
        self.pos_z = pos_z
    
    def get_pos(self):
        return self.pos

    def get_pos_z(self):
        return self.pos_z
    
    def set_scale(self, scale):
        self.scale  = (scale[0], scale[1])
        self.Scale()
    
    def set_cur_frame_num(self, cur_frame_num):
        self.cur_frame_num = cur_frame_num

    def get_cur_frame(self):
        if len(self.order_frames) > 0:
            return self.order_frames[self.cur_frame_num]
        else:
            return None
    
    def set_frame_time(self, frame_time):
        self.frame_time = frame_time
    
    def get_active_state(self):
        return self.active

    def change_active_state(self):
        # self.active = not self.active
        if self in self.all_objects.list_used:
            self.all_objects.list_used.remove(self)
            self.all_objects.list_not_used.append(self)
            self.active = False
        elif self in self.all_objects.list_not_used:
            self.all_objects.list_not_used.remove(self)
            self.all_objects.list_used.append(self)
            self.active = True


    def change_pos(self, d_pos):
        self.pos = (self.pos[0] + d_pos[0], self.pos[1] + d_pos[1])

    def change_pos_z(self, d_pos_z):
        self.pos_z += d_pos_z

    def change_scale(self, d_scale):
        self.scale = (self.scale[0] + d_scale[0], self.scale[1] + d_scale[1])
        self.Scale()
    
    def change_cur_frame_num(self, d_cur_frame_num):
        self.cur_frame_num = (self.cur_frame_num + d_cur_frame_num) % len(self.order_frames)
    
    def play_sound(self): # equal to def play_cur_sound
        if len(self.order_sounds) > 0:
            if self in self.all_objects.list_used:
                self.order_sounds[self.cur_sound_num].play()
    
    def stop_sound(self): # equal to def stop_cur_sound
        if len(self.order_sounds) > 0:
            self.order_sounds[self.cur_sound_num].stop()
    
    def loop_sound(self): # equal to def loop_cur_sound
        if len(self.order_sounds) > 0:
            if self in self.all_objects.list_used:
                self.order_sounds[self.cur_sound_num].loop()

    def set_cur_sound_num(self, cur_sound_num):
        self.cur_sound_num = cur_sound_num

    def get_cur_sound_num(self):
        return self.cur_sound_num

    def change_cur_sound_num(self, d_cur_sound_num):
        self.cur_sound_num = (self.cur_frame_num + d_cur_sound_num) % len(self.order_sounds)
    
    def set_cur_sound_volume(self, volume):
        if len(self.order_sounds) > 0:
            if volume > 1:
                volume = 1
            elif volume < 0:
                volume = 0
            self.order_sounds[self.cur_sound_num].set_volume(volume)