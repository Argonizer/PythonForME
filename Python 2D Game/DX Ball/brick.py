import pygame

class brick():
    def _init_(self, x, y, img):
       self.x = x
       self.y = y
       self.img = img
       self.width = img.get_size()[0]
       self.height = img.get_size()[1]
       self.collision_count = 0

    def increment_collision_count(self):
        self.collision_count += 1

    def draw_brick(self, surface):
        surface.blit(self.img, (self.x, self.y))

    def brick_collision(self, ball_x, ball_y, ball_width, ball_height):
        inversion_x = False
        inversion_y = False

        brick_horizontal_start = self.x
        brick_horizontal_end = self.x + self.width
        brick_vertical_start = self.y
        brick_vertical_end = self.y + self.height
        ball_horizontal_start = ball_x
        ball_horizontal_end = ball_x + ball_width
        ball_horizontal_centre = ball_x + ball_width/2
        ball_vertical_start = ball_y
        ball_vertical_end = ball_y + ball_height
        ball_vertical_centre = ball_x + ball_height / 2

        if (ball_horizontal_start > brick_horizontal_start and ball_horizontal_end < brick_horizontal_end) and (
                ball_vertical_end > brick_vertical_start and ball_vertical_start < brick_vertical_end):
            inversion_y = True
        if (ball_vertical_start > brick_vertical_start and ball_vertical_end < brick_vertical_end) and (
                ball_horizontal_end > brick_horizontal_start and ball_horizontal_start <= brick_horizontal_end):
            inversion_x = True

        return (inversion_x, inversion_y)