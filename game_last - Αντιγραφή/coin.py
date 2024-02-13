import pygame

import dynamic_object as dy_obj

# player is part of the map class as monster and other things like keys boxes fierballs and other dynamic objects
class Coin:
    def __init__(self, menu, map, init_pos, all_objects):
        self.image = dy_obj.DynamicObject(menu, map, 'player_fier', init_pos, 0, order_frames = (
            'coin_0',
            'coin_1',
            'coin_2',
            'coin_3'
            ), order_animations = ((0, 1, 2, 3),), order_sounds = ('coin',), all_objects = all_objects)
        self.image.set_cur_animation(0)
        self.image.set_frame_time(8)

    # every objects logic runs from level!
    # monsters see the fier not the oposite from the player object in the level it is eazier that way!
    def run(self):
        self.image.run()
        self.image.play_cur_animation()
    
    def change_active_state(self):
        self.image.change_active_state()

    def remove_from_all_objects(self):
        self.image.remove_from_all_objects()