from random import randint

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

PLAYING = 0
GAME_OVER = 1
GAME_WON = 2


class SnakeGame:
    def __init__(self, width, height, food=None, snake=None, direction=UP):
        """Object initialization logic"""
        self.width = width
        self.height = height
        self.food = food
        self.direction = direction
        self.snake = snake or [(width // 2, height // 2)]

    def move_snake(self):
        x = self.snake[0][0]
        y = self.snake[0][1]
        if self.direction == UP:
            self.snake = [(x, y-1)]
        if self.direction == DOWN:
            self.snake = [(x, y+1)]
        if self.direction == LEFT:
            self.snake = [(x-1, y)]
        if self.direction == RIGHT:
            self.snake = [(x+1, y)]
    
    def tick(self):
        self.move_snake()
    
    def change_direction(self, new_direction): 
        if self.even(self.direction) != self.even(new_direction):
            self.direction = new_direction

    def even(self, m):
        return m % 2 == 0