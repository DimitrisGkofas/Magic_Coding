import pygame

class Text:
    def __init__(self, x, y, font_type, font_size,color=(0, 0, 31), initial_text="", min_text=0, max_text=10000):
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.Font(font_type, font_size)
        self.text = initial_text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.topleft = (self.x, self.y)
        self.min_text = min_text
        self.max_text = max_text

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Detect Enter (Return) key press and add "\n" to the text.
                self.text += '\n'
            elif event.key == pygame.K_BACKSPACE and len(self.text) > self.min_text:
                self.text = self.text[:-1]
            elif len(self.text) < self.max_text:
                self.text += event.unicode
            self.update_text_surface()

    def update_text_surface(self):
        self.text_surface = self.font.render(self.text, True, self.color)

    def render(self, surface):
        surface.blit(self.text_surface, self.text_rect)