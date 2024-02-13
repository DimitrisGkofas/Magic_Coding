import object as obj

import maths

class DynamicObject:
    def __init__(self, menu, map, name, init_pos, init_pos_z, order_frames = None, order_animations = None, order_sounds = None, all_objects = None):
        self.map = map

        self.menu = menu

        self.render_obj = obj.Object(name, init_pos, init_pos_z, order_frames = order_frames, order_sounds = order_sounds, all_objects = all_objects)
        self.render_obj.set_cur_sound_volume(self.menu.sfx_volume)
        self.change_active_state()

        self.rel_pos = init_pos

        self.order_animations = order_animations

        self.cur_animation_num = None

        self.time = 0
        self.frame_time = 8

    def play_cur_animation(self):
        if self.cur_animation_num != None:
            cur_animation_frame_num = int(self.time / self.frame_time) % len(self.order_animations[self.cur_animation_num])
            self.render_obj.set_cur_frame_num(self.order_animations[self.cur_animation_num][cur_animation_frame_num])
            self.time += 1
    
    def set_map_rel_pos(self, rel_pos):
        self.rel_pos = rel_pos

    def get_map_rel_pos(self):
        return self.rel_pos

    def change_map_rel_pos(self, dir):
        self.rel_pos = (self.rel_pos[0] + dir[0], self.rel_pos[1] + dir[1])

    def set_cur_animation(self, animation_num):
        self.cur_animation_num = animation_num
    
    def set_frame_time(self, frame_time):
        self.frame_time = frame_time

    def run(self):
        rel_map_pos = self.map.get_map_pos()
        render_obj_dims = self.render_obj.get_cur_frame().get_dims()
        rel_pos = self.get_map_rel_pos()
        self.render_obj.set_pos((rel_map_pos[0] + rel_pos[0] * 32 + 128, rel_map_pos[1] + rel_pos[1] * 16 - render_obj_dims[1] + 87))
        self.render_obj.set_pos_z(maths.linear_interp(self.rel_pos[1], 0, 32, 0.2, 0.8))

    def get_dynamic_dist(self, other_dyn_obj, bool_dist):
        other_x, other_y = other_dyn_obj.get_map_rel_pos()
        my_x, my_y = self.get_map_rel_pos()
        Dx = other_x - my_x
        Dy = other_y - my_y
        if bool_dist:
            return (Dx * Dx + Dy * Dy) ** 0.5
        else:
            return (Dx, Dy)

    def set_dir_from_map_col(self, dir):
        my_pos = self.get_map_rel_pos()
        my_pos = (my_pos[0] + 0.5, my_pos[1])

        push_value = (abs(dir[0]) + abs(dir[1])) / 16

        if maths.map_state_from_points(self.map, (my_pos[0] + 0.4, my_pos[1] - 0.2)) or maths.map_state_from_points(self.map, (my_pos[0] + 0.4, my_pos[1] + 0.2)):
            dir = (0, dir[1])
            self.change_map_rel_pos((-push_value, 0))
        if maths.map_state_from_points(self.map, (my_pos[0] + 0.2, my_pos[1] + 0.4)) or maths.map_state_from_points(self.map, (my_pos[0] - 0.2, my_pos[1] + 0.4)):
            dir = (dir[0], 0)
            self.change_map_rel_pos((0, -push_value))
        if maths.map_state_from_points(self.map, (my_pos[0] - 0.4, my_pos[1] + 0.2)) or maths.map_state_from_points(self.map, (my_pos[0] - 0.4, my_pos[1] - 0.2)):
            dir = (0, dir[1])
            self.change_map_rel_pos((push_value, 0))
        if maths.map_state_from_points(self.map, (my_pos[0] - 0.2, my_pos[1] - 0.4)) or maths.map_state_from_points(self.map, (my_pos[0] + 0.2, my_pos[1] - 0.4)):
            dir = (dir[0], 0)
            self.change_map_rel_pos((0, push_value))

        return dir

    def change_active_state(self):
        self.render_obj.change_active_state()

        cur_sound_num = self.render_obj.get_cur_sound_num()
        for counter in range(len(self.render_obj.order_sounds)):
            self.render_obj.set_cur_sound_num(counter)
            self.render_obj.stop_sound()
            self.render_obj.set_cur_sound_volume(self.menu.sfx_volume)
        self.render_obj.set_cur_sound_num(cur_sound_num)

        self.time = 0
    
    def remove_from_all_objects(self):
        self.render_obj.remove_from_all_objects()