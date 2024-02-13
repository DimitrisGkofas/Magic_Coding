import random

import all_maps as all_mp

import object as obj

import maths
# init_pos_z is arbitrary the only constrain is the value comperations between Objects_n.pos_z
# maps objects must also have an active state in this map is the 
# if self.floor in self.floor.all_objects.list_used: as in the menu script

class Map:
    def __init__(self, name, map_num, menu, all_objects):
        self.menu = menu

        self. name = name

        self. map_num = map_num

        # Collisions map for dynamic objects like player monsters fierballs or boxes
        self.collisions = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        for layer_counter, line in enumerate(all_mp.maps[self.map_num]):
            for counter_x_32 in range(len(line)):
                self.collisions[layer_counter].append(False)

        for layer_counter, line in enumerate(all_mp.maps[self.map_num]):
            for counter_x_32, key in enumerate(line):
                if key != '   ':
                    # if key == 'glm':
                        # self.collisions[layer_counter][counter_x_32] = True
                        # self.collisions[layer_counter][counter_x_32 + 3] = True
                    # else:
                    it_colls = all_mp.StaticMapItemsColls[key]
                    # print(it_colls)
                    for x in range(it_colls[0]):
                        for y in range(it_colls[1]):
                            self.collisions[layer_counter - y][counter_x_32 + x] = True
        
        '''
        for y in range(len(self.collisions)):
            for x in range(len(self.collisions[y])):
                if self.collisions[y][x]:
                    print('H', end = ' ')
                else:
                    print(' ', end = ' ')
            print()
        '''
            
        self.floor = obj.Object(name = 'floor', init_pos = (0, 0), init_pos_z = 0.1, order_frames = ('map', 'floor_grass'), order_sounds = ('owl',), all_objects = all_objects)
        self.floor.set_cur_sound_volume(self.menu.sfx_volume)
        self.floor.set_cur_frame_num(1)
        self.floor.get_cur_frame().set_alpha(256 - 32)
        self.floor.set_cur_frame_num(0)
        for grass_counter in range(16):
            grass_x = random.randint(1, 8) * 128
            grass_y = random.randint(0, 7) * 64 + 71
            self.floor.blit((1, 0), (grass_x, grass_y))
        self.floor.change_active_state()

        self.layers = []
        for layer_counter, line in enumerate(all_mp.maps[self.map_num]):
            self.layers.append(obj.Object(name = f"layer_{layer_counter}", init_pos = (0, 0), init_pos_z = maths.linear_interp(layer_counter, 0, 31, 0.2, 0.8), order_frames = ('blank',), all_objects = all_objects))
            last_layer = self.layers[-1]
            last_layer.set_scale((64, 10))
            # print(last_layer.get_cur_frame().get_dims())
            for counter_x_32, key in enumerate(line):
                if key != '   ':
                    last_layer.add_map_frame(key)
                    # print(counter_x_32, ',key:', key)
                    dims = last_layer.order_frames[-1].get_dims()
                    last_layer.blit((-1, 0), (counter_x_32 * 32, 5 * 32 - dims[1]))
            last_layer.change_active_state()

        self.clouds_speed = 1
        self.clouds_pos = 0

        self.clouds_1 = obj.Object(name = 'mist_1', init_pos = (0, 0), init_pos_z = 0.9, order_frames = ('blank', 'mist_1', 'mist_2'), all_objects = all_objects)
        self.clouds_1.set_scale((80, 38))
        # print('Clouds_1 dims:', self.clouds_1.get_cur_frame().get_dims())
        for cloud_counter in range(16):
            cloud_x = random.randint(0, 9) * 128
            cloud_y = random.randint(0, 8) * 64 + 16
            self.clouds_1.blit((random.randint(1, 2), 0), (cloud_x, cloud_y))
        self.clouds_1.change_active_state()
        
        self.clouds_2 = obj.Object(name = 'mist_2', init_pos = (0, 0), init_pos_z = 0.9, all_objects = all_objects)
        self.clouds_2.copy_frame(self.clouds_1)
        self.clouds_2.change_active_state()
    
    def get_num(self):
        return self.map_num

    def animate_clouds(self):
        self.clouds_pos -= self.clouds_speed
        if self.clouds_pos < -1280:
            self.clouds_pos = 0

    def connect_all_to_floor(self):
        floor_pos = self.floor.get_pos()
        # Clouds connection
        self.clouds_1.set_pos((floor_pos[0] + self.clouds_pos, floor_pos[1]))
        self.clouds_2.set_pos((floor_pos[0] + self.clouds_pos + 1280, floor_pos[1]))
        # Static Items connection
        for layer_counter, layer in enumerate(self.layers):
            layer.set_pos((floor_pos[0] + 128, floor_pos[1] + layer_counter * 16 - 73))
    
    def set_map_pos(self, pos):
        self.floor.set_pos((pos[0], pos[1]))
        self.animate_clouds()
        self.connect_all_to_floor()
    
    def get_map_pos(self):
        return self.floor.get_pos()
    
    def play_random_spooky_sound(self):
        if random.random() > 0.99609375:
            self.floor.play_sound()

    def stop_spooky_sound(self):
        self.floor.stop_sound()
    
    def set_sfx_volume(self):
        self.floor.set_cur_sound_volume(self.menu.sfx_volume)
    
    def run(self, pos): # pos is needed for now
        # if self.map_num == self.menu.selected_level - 1:
        # if not self.menu.background.get_active_state():
        self.set_map_pos(pos)
        self.play_random_spooky_sound()

            # self.change_active_state()

    def change_active_state(self):
        # if self.menu.background.get_active_state() != self.old_menu_state:
        self.floor.change_active_state()

        for layer in self.layers:
            layer.change_active_state()

        self.clouds_1.change_active_state()
        self.clouds_2.change_active_state()

        self.stop_spooky_sound()

        self.set_sfx_volume()
    
    def remove_from_all_objects(self):
        self.floor.remove_from_all_objects()

        for layer in self.layers:
            layer.remove_from_all_objects()

        self.clouds_1.remove_from_all_objects()
        self.clouds_2.remove_from_all_objects()
