import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SHIP_HEIGHT, SHIP_WIDTH


class Spaceship(Sprite):

    Y_POS = 500
    X_POS = (SCREEN_WIDTH // 2) - 40
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(
            self.image, (SHIP_WIDTH, SHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):

        if user_input[pygame.K_LEFT]:
            self.move_left()

        if user_input[pygame.K_RIGHT]:
            self.move_right()

        if user_input[pygame.K_UP]:
            self.move_up()

        if user_input[pygame.K_DOWN]:
            self.move_down()

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left <= 0:
            self.rect.left = SCREEN_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 61:
            self.rect.y += self.SHIP_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)
