import dynamic_object as dy_obj

# player is part of the map class as monster and other things like keys boxes fierballs and other dynamic objects
class MagicKey:
    def __init__(self, menu, map, player, init_pos, all_objects):

        self.player = player

        self.image = dy_obj.DynamicObject(menu, map, 'player_fier', init_pos = init_pos, init_pos_z = 0, order_frames = (
                            'key_0',
                            'key_1',
                            'key_2',
                            'key_3'
                            ), order_animations = ((0, 1, 2, 3),), order_sounds = ('coin','achievement'), all_objects = all_objects)

    def run(self):
        self.image.run()
        self.image.play_cur_animation()

    def change_active_state(self):
        self.image.change_active_state()

    def remove_from_all_objects(self):
        self.image.remove_from_all_objects()