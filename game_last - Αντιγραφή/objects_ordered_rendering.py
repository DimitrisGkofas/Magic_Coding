class OrderedZList:
    def __init__(self, game_surface):
        self.list_not_used = []
        self.list_used = []

        self.game_surface = game_surface
    
    def get_game_surface(self):
        return self.game_surface

    def sort_objects_by_z_pos(self):
        self.list_used = sorted(self.list_used, key=lambda obj: obj.pos_z)

    def render_all(self):
        for obj in self.list_used:
            obj.render(self.game_surface)

    def check_all(self, mouse_pos):
        selected_obj = None

        for obj in self.list_used:
            cur_obj = obj.collision(mouse_pos)
            if cur_obj != None:
                selected_obj = cur_obj

        return selected_obj