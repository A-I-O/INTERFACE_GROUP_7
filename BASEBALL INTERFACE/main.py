import pygame
from setting import Settings

settings = Settings()


def game_time():
    font_style_4 = pygame.font.SysFont("Verdana", 30).render(f"Time: {time}", False, (255, 255, 255))
    settings.screen.blit(font_style_4, (650, 550))


def draw():
    settings.draw_background()
    settings.draw_batter()
    settings.draw_bat()
    settings.draw_pitcher()
    settings.draw_glove_x()
    settings.draw_ball()
    settings.draw_score()


pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("BASEBALL")
icon = pygame.image.load("assets/player_1.png")
pygame.display.set_icon(icon)
chances = 0
collide_count = 0

ball_state = False
ball_speed = 0

pygame.mixer.music.load("assets/sound.mp3")
pygame.mixer.music.play(-1)

running = True
while running:
    time = int(pygame.time.get_ticks() / 1000)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and ball_state is False:
                ball_speed = 10
                ball_state = True
                chances += 1
                if chances > 7 and collide_count == 0:
                    result_1 = settings.score_list_1[len(settings.score_list_1) - 1]
                    settings.score_list_1.append(result_1 + 2)
                    chances = 0

    settings.ball_rect.y += ball_speed
    if settings.ball_rect.colliderect(settings.bat_rect):
        ball_speed *= -1
    if settings.ball_rect.bottom <= 0:
        ball_state = False
        settings.ball_rect = settings.scaled_ball.get_rect(midright=(415, 250))
        ball_speed = 0

    if settings.ball_rect.colliderect(settings.glove_rect):
        ball_state = False
        settings.ball_rect = settings.scaled_ball.get_rect(midright=(415, 250))
        ball_speed = 0
        settings.score_list_2.append("C")
        results = settings.score_list_1[len(settings.score_list_1) - 1]
        settings.score_list_1.append(results - 2)
        collide_count += 1
        print("catch")

        if chances == 4 and collide_count == 0:
            result_2 = settings.score_list_1[len(settings.score_list_1) - 1]
            settings.score_list_1.append(result_2 * 2)
            print("Home run")
            chances = 0

        if collide_count == 0 and settings.ball_rect.y < 0:
            print("missed")
        collide_count = 0

    if time % 10 == 0 and time > 0:
        settings.screen.fill((0, 0, 255))
        settings.draw_game_over()
        settings.score.append(sum(settings.score_list_1))
        settings.score = []
        settings.score_list_1 = [5]
        settings.score_list_2 = []

    pygame.display.update()
    clock.tick(60)
