import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, player_pos):
        super().__init__()

        self.image = pygame.image.load('graphics/player.png')
        self.rect = self.image.get_rect(center = player_pos)

    def focus_camera(self, screen, all_sprites):
        offset_x = screen.get_size()[0] // 2 - self.rect.centerx
        offset_y = screen.get_size()[1] // 2 - self.rect.centery

        if self.rect.left < screen.get_size()[0] // 4:
            offset_x = -self.rect.left + screen.get_size()[0] // 4
        elif self.rect.right > 3 * screen.get_size()[0] // 4:
            offset_x = -self.rect.right + 3 * screen.get_size()[0] // 4

        if self.rect.top < screen.get_size()[1] // 4:
            offset_y = -self.rect.top + screen.get_size()[1] // 4
        elif self.rect.bottom > 3 * screen.get_size()[1] // 4:
            offset_y = -self.rect.bottom + 3 * screen.get_size()[1] // 4

        for sprite in all_sprites:
            sprite.rect.x += offset_x
            sprite.rect.y += offset_y
            screen.blit(sprite.image, sprite.rect)


def keyboard_camera_control(all_sprites):
    keys = pygame.key.get_pressed()
    
    speed = 40
    if keys[pygame.K_LSHIFT]:
        speed = 120

    if keys[pygame.K_LEFT]:
        for sprite in all_sprites:
            sprite.rect.x += speed

    if keys[pygame.K_RIGHT]:
        for sprite in all_sprites:
            sprite.rect.x -= speed

    if keys[pygame.K_UP]:
        for sprite in all_sprites:
            sprite.rect.y += speed

    if keys[pygame.K_DOWN]:
        for sprite in all_sprites:
            sprite.rect.y -= speed