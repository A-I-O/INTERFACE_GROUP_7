import pygame


class Settings:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load("assets/pitch.jpg")
        self.player = pygame.image.load('assets/batter.png')
        self.pitcher = pygame.image.load('assets/pitcher_2.png')
        # bat
        self.bat = pygame.image.load('assets/bat.png')
        self.scaled_bat = pygame.transform.scale(self.bat, (32, 32))
        self.rotated_bat = pygame.transform.rotate(self.scaled_bat, -40)
        self.bat_rect = self.rotated_bat.get_rect(midleft=(388, 552))
        # glove
        self.glove = pygame.image.load('assets/glove.png')
        self.scaled_glove = pygame.transform.scale(self.glove, (64, 64))
        self.glove_rect = self.scaled_glove.get_rect(bottomleft=(300, 122))
        # ball
        self.ball = pygame.image.load('assets/ball.png')
        self.scaled_ball = pygame.transform.scale(self.ball, (12, 12))
        self.ball_rect = self.scaled_ball.get_rect(midright=(415, 253))
        self.glove_speed = 5

        self.score_list_1 = [5]
        self.score_list_2 = []
        self.score = []

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def draw_batter(self):
        scaled_batter = pygame.transform.scale(self.player, (64, 64))
        batter_rect = scaled_batter.get_rect(bottomleft=(326, 600))
        self.screen.blit(scaled_batter, batter_rect)

    def draw_bat(self):
        self.screen.blit(self.rotated_bat, self.bat_rect)

    def draw_pitcher(self):
        scaled_pitcher = pygame.transform.scale(self.pitcher, (64, 64))
        pitcher_rect = scaled_pitcher.get_rect(midbottom=(427, 307))
        self.screen.blit(scaled_pitcher, pitcher_rect)

    def draw_glove_x(self):
        self.screen.blit(self.scaled_glove, self.glove_rect)
        self.glove_rect.x += self.glove_speed
        if self.glove_rect.right >= 590:
            self.glove_speed *= -1
        elif self.glove_rect.left <= 187:
            self.glove_speed *= -1

    def draw_ball(self):
        self.screen.blit(self.scaled_ball, self.ball_rect)

    def draw_score(self):
        font_style_1 = pygame.font.SysFont("Verdana", 30).render(f"score: {self.score_list_1}", False, (255, 255, 255))
        font_style_2 = pygame.font.SysFont("Verdana", 30).render(f"score: {self.score_list_2}", False, (255, 255, 255))
        self.screen.blit(font_style_1, (3, 3))
        self.screen.blit(font_style_2, (3, 40))

    def draw_game_over(self):
        font_style_4 = pygame.font.SysFont("Verdana", 60).render(f"GAME_OVER",
                                                                 False, (255, 0, 0))
        font_style_3 = pygame.font.SysFont("Verdana", 60).render(f"Total_score: {self.score}",
                                                                 False, (255, 255, 255))
        self.screen.blit(font_style_3, (150, 300))
        self.screen.blit(font_style_4, (200, 100))
