import pygame

class component():

    def _init_(self, id, x, y, angle, img):
        self.id = id
        self.pivot_x = x
        self.pivot_y = y
        self.angle = angle
        self.img = img
        self.width = img.get_size()[0]
        self.height = img.get_size()[1]
        self.centre = (self.width/2, self.height/2)
        self.x = self.pivot_x
        self.y = self.pivot_y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_angle(self, angle):
        self.angle = angle


    def rotate_draw(self, surface):
        image_surface = self.img.convert_alpha()
        self.set_x(self.pivot_x + self.centre[0])
        self.set_y(self.pivot_y + self.centre[1])
        rot_img = pygame.transform.rotate(image_surface, self.angle)
        self.set_x(self.x - rot_img.get_size()[0]/2)
        self.set_y(self.y - rot_img.get_size()[1]/2)
        surface.blit(rot_img, (self.x, self.y))

    def linear_draw(self, surface):
        surface.blit(self.img, (self.x, self.y))

    def linear_rotate_draw(self, surface):
        image_surface = self.img.convert_alpha()
        self.set_x(self.pivot_x + self.centre[0])
        self.set_y(self.y + self.centre[1])
        rot_img = pygame.transform.rotate(image_surface, self.angle)
        self.set_x(self.x - rot_img.get_size()[0] / 2)
        self.set_y(self.y - rot_img.get_size()[1] / 2)
        surface.blit(rot_img, (self.x, self.y))

