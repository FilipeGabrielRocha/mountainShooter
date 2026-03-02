import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        # 1- carrego a imagem
        self.surf = pygame.image.load('./asset/images/MenuBg.png')
        # 2- posiciono a imagem
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # 3- desenha a imagem no retângulo
        self.window.blit(source=self.surf, dest=self.rect)
        # 4- Atualiza para a imagem aparecer
        pygame.display.flip()
        pass