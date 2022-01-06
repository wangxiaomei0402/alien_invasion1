import pygame


class Sky:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("blue sky")
        self.bg_color = (0, 0, 255)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    ai = Sky()