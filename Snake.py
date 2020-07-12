import pygame
import time
from SnakeGame import SnakeGame, UP, DOWN, LEFT, RIGHT, PLAYING, GAME_OVER, GAME_WON

WIDTH = 50
HEIGHT = 40
FIELD_SIZE = 12

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (127, 0, 0)
BROWN = (121, 63, 13)
GREEN = (0, 147, 0)

WALL_COLOR = RED
SNAKE_COLOR = BROWN
FOOD_COLOR = GREEN


def draw_walls(display):
    pygame.draw.rect(
        display, WALL_COLOR, (0, 0, (2 + WIDTH) * FIELD_SIZE, FIELD_SIZE))
    pygame.draw.rect(
        display, WALL_COLOR, (0, (1 + HEIGHT) * FIELD_SIZE, (2 + WIDTH) * FIELD_SIZE, FIELD_SIZE))
    pygame.draw.rect(
        display, WALL_COLOR, (0, FIELD_SIZE, FIELD_SIZE, HEIGHT * FIELD_SIZE))
    pygame.draw.rect(
        display, WALL_COLOR, ((1 + WIDTH) * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE, HEIGHT * FIELD_SIZE))


def draw_snake(display, game):
    for (x, y) in game.snake:
        pygame.draw.rect(display, SNAKE_COLOR, ((
            1 + x) * FIELD_SIZE, (1 + y) * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))


def draw_food(display, game):
    for (x, y) in game.food:
        pygame.draw.rect(display, FOOD_COLOR, ((
            1 + x) * FIELD_SIZE, (1 + y) * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))


def draw_arena(display, game):
    display.fill(WHITE)
    draw_walls(display)
    draw_food(display, game)
    draw_snake(display, game)


def draw_text(display, text):
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    text_surface = font.render(text, False, RED)
    x = ((2 + WIDTH) * FIELD_SIZE - text_surface.get_width()) // 2
    y = ((2 + HEIGHT) * FIELD_SIZE - text_surface.get_height()) // 2
    display.blit(text_surface, (x, y))


def main():
    game = SnakeGame(width=WIDTH, height=HEIGHT)
    pygame.init()
    display = pygame.display.set_mode(
        ((2 + WIDTH) * FIELD_SIZE, (2 + HEIGHT) * FIELD_SIZE))
    pygame.display.set_caption('PySnake')
    draw_arena(display, game)
    pygame.display.update()

    last_time = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_direction(UP)
                if event.key == pygame.K_DOWN:
                    game.change_direction(DOWN)
                if event.key == pygame.K_LEFT:
                    game.change_direction(LEFT)
                if event.key == pygame.K_RIGHT:
                    game.change_direction(RIGHT)
                if event.key == pygame.K_y and game.status != PLAYING:
                    game = SnakeGame(width=WIDTH, height=HEIGHT)
                if event.key == pygame.K_n and game.status != PLAYING:
                    return

        current_time = time.time() * 1000
        if current_time - last_time < 100:
            continue

        last_time = current_time
        if game.status == PLAYING:
            game.tick()
            draw_arena(display, game)
        elif game.status == GAME_OVER:
            draw_text(display, 'Game Over. Try again (y/n)?')
        elif game.status == GAME_WON:
            draw_text(display, 'You won! Try again (y/n)?')

        pygame.display.update()


if __name__ == '__main__':
    main()
