import pygame
import sys
from settings import *
from game_setup import *
from player import keyboard_camera_control

probability_threshold = 0.15


class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hero's Journey")

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.game_canvas = pygame.Surface((screen_width, screen_height))
        self.clock = pygame.time.Clock()

        self.game_state_manager = GameStateManager('start')
        self.start = Start(self.screen, self.game_state_manager)
        self.level = LevelState(self.screen, self.game_state_manager)
        self.battle = BattleState(self.screen, self.game_state_manager)

        self.states = {'start': self.start, 'level': self.level, 'battle': self.battle}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.game_state_manager.get_state()].run()

            pygame.display.update()
            self.clock.tick(fps)


class Start:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager
    
    def run(self):
        start_background = pygame.image.load('graphics/start_bg_1.png')
        start_rect = start_background.get_rect(topleft = (0, 0))
        transformed_image = pygame.transform.scale(start_background, (1500, 700))
        self.display.blit(transformed_image, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.game_state_manager.set_state('level')


class LevelState:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager
    
    def run(self):
        keyboard_camera_control(all_sprites)
        
        level.run()
        player_list.draw(self.display)
        collisions = pygame.sprite.spritecollide(player_sprite, all_level_sprites, False)
        for tile in collisions:
            if not tile.is_flipped:
                tile.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for tile in all_level_sprites:
                    if tile.rect.collidepoint(mouse_pos) and tile.is_flipped:
                        player_sprite.rect.center = tile.rect.center
                        random_chance = random.random()
                        if random_chance < probability_threshold:
                            self.game_state_manager.set_state('battle')

        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            self.game_state_manager.set_state('start')


class BattleState:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager
    
    def run(self):
        initiate_battle.run()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game_state_manager.set_state('level')

    def test_run(self):
        ability_cooldown = 0
        ability_wait_time = 90

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            initiate_battle.run()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.game_state_manager.set_state('level')

            for character in characters:
                if character.is_player and character.alive:
                    character.show_turn()
                    ability_cooldown += 1
                    if ability_cooldown >= ability_wait_time:
                        # player.attack(self.selected_target, self.selected_ability)
                        ability_cooldown = 0
                    character.end_turn()
                    
                
            for character in characters:
                if not character.is_player and character.alive:
                    character.show_turn()
                    ability_cooldown += 1
                    if ability_cooldown >= ability_wait_time:
                        # player.attack(self.selected_target, self.selected_ability)
                        ability_cooldown = 0
                    character.end_turn()
                    

            if any(character.is_player and not character.alive for character in characters):
                self.game_state_manager.set_state('start')
            elif all(not character.is_player and not character.alive for character in characters):
                self.game_state_manager.set_state('start')


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        self.current_state = state

if __name__ == '__main__':
    game = Game()
    game.run()