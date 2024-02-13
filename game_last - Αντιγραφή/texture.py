import pygame

class Texture:
    def __init__(self, crop_x, crop_y, crop_dim_x, crop_dim_y, init_scale_x, init_scale_y, path):
        cropping_rect = pygame.Rect(crop_x, crop_y, crop_dim_x, crop_dim_y)
        image = pygame.image.load(path)
        self.subimage = image.subsurface(cropping_rect)

        # Apply scaling to the cropped image
        scaled_dim_x = int(crop_dim_x * init_scale_x)
        scaled_dim_y = int(crop_dim_y * init_scale_y)
        self.scaled_subimage = pygame.transform.scale(self.subimage, (scaled_dim_x, scaled_dim_y))
        # also basic text surface
        self.text = False
        self.text_surface = pygame.Surface((512, 512), pygame.SRCALPHA)
        self.text_surface.fill((0, 0, 0, 0))  # Fill it blank
    
    def render(self, game_surf, pos):
        game_surf.blit(self.scaled_subimage, pos)  # Adjust the coordinates as needed
        if self.text:
            game_surf.blit(self.text_surface, (0, 0))

    def clear_text(self):
        # clear text_surface
        self.text_surface.fill((0, 0, 0, 0))  # Fill it blank

    def blit_on_top(self, other_texture, pos):
        other_texture.scaled_subimage.blit(self.scaled_subimage, pos) # Adjust the coordinates as needed

    def clear_texture(self):
        self.scaled_subimage.fill((0, 0, 0, 0))

    def scale(self, scale):
        # Apply scaling to the cropped image
        scaled_dim_x = int(self.subimage.get_width() * scale[0])
        scaled_dim_y = int(self.subimage.get_height() * scale[1])
        self.scaled_subimage = pygame.transform.scale(self.subimage, (scaled_dim_x, scaled_dim_y))

    def set_alpha(self, alpha_value):
        self.scaled_subimage.set_alpha(alpha_value)
    
    def get_dims(self):
        return (self.scaled_subimage.get_width(), self.scaled_subimage.get_height())
    # to write text on top
    def get_text_surface(self):
        return self.text_surface
    
    def set_text(self, boolean_value):
        self.text = boolean_value
    