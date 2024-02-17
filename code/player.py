import pygame


class Player(pygame.sprite.Sprite):
    """
    Player class representing the main character sprite in the level state of the game.

    Attributes:
        image (Surface): The image representing the player sprite.
        rect (Rect): The rectangular area occupied by the player sprite.
    """

    def __init__(self, player_pos):
        """
        Initialize the Player object.

        Args:
            player_pos (tuple): The initial position of the player sprite (x, y).
        """
        super().__init__()

        self.image = pygame.image.load('graphics/player.png')
        self.rect = self.image.get_rect(center = player_pos)

    def focus_camera(self, screen, all_sprites):
        """
        Adjust the camera based on the player's position.

        Args:
            screen (Surface): The game screen surface.
            all_sprites (Group): A group containing all sprites to adjust.
        """
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
    """
    Control the camera movement based on keyboard input in the level state of the game.

    Args:
        all_sprites (Group): A group containing all sprites to adjust.
    """
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