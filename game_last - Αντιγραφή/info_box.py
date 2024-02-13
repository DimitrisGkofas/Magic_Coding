import dynamic_object as dy_obj

# player is part of the map class as monster and other things like keys boxes fierballs and other dynamic objects
class InfoBox:
    def __init__(self, menu, map, player, unlock_order, info_name, init_pos, all_objects):
        self.player = player

        self.image = dy_obj.DynamicObject(menu, map, 'info_box', init_pos = init_pos, init_pos_z = 0, order_frames = (
                            'box_closed',
                            'box_opened',
                            info_name
                            ), order_sounds = ('box_unlock', 'paper', 'achievement'), all_objects = all_objects)
        
        self.image.render_obj.blit((1, 2), (0, 320 - 32))
        
        self.locked = True

        self.unlock_order = unlock_order

    def is_locked(self):
        return self.locked
    
    def get_unlock_num(self):
        return self.unlock_order
    
    def unlock(self):
        self.locked = False

    def run(self):
        self.image.run()

    def change_active_state(self):
        self.image.change_active_state()

    def remove_from_all_objects(self):
        self.image.remove_from_all_objects()