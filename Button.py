import pygame

class Button():
    def __init__(self, x, y, text, font_size, color, bg_color, scale=1, width=None, height=None, border=0, border_color=None):
        self.font = pygame.font.SysFont(None, font_size)
        self.color = color
        self.bg_color = bg_color
        if width is not None and height is not None:
            self.width = width
            self.height = height
        else:
            self.width = int(font_size * scale) * len(text)
            self.height = int(font_size * scale)
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

        # add border
        self.border = border
        self.border_color = border_color

        
        if self.border > 0 and self.border_color is not None:
            self.image.fill(self.border_color, pygame.Rect(0, 0, self.width, self.height))
            self.image.fill(self.bg_color, pygame.Rect(self.border, self.border, self.width - self.border * 2, self.height - self.border * 2))
        else:
            self.image.fill(self.bg_color)

        # render text
        self.text = self.font.render(str(text), True, self.color, self.bg_color)
        self.text_rect = self.text.get_rect(center=self.image.get_rect().center)

        # blit text onto image
        self.image.blit(self.text, self.text_rect)

    def draw(self, surface):
        action = False

        # mouse pos
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
