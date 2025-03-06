import pygame
from color import Color
class Screen:
    def __init__(self, width=800, height=600,background_color = Color.BLACK,font_type="monospace",font_size=35,clock_tick=30):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width,height))
        self.font = pygame.font_sys.Font(font_type,font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick


    def refresh_background(self):
        self.screen.file(self.background_color)


    def draw_enemies(self,enemy_list):
        for enemy in enemy_list:
            enemy.draw(self.screen)

   
    def draw_player(self,player):
        player.draw(self.screen)

    def draw_score_labe(self,score,color=Color.YELLOW):
        text = f"Score: {score}"
        label = self.font.render(text,1,color)
        self.screen.blit(label,(self.width-200,self.height-40))