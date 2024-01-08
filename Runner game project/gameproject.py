import pygame
from sys import exit
from random import randint, choice

pygame.init()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('ele.png').convert_alpha()
        player_walk_2 = pygame.image.load('Picture 2.png').convert_alpha()
        self.player_index = 0
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_jump = pygame.image.load('ele.png').convert_alpha()
        self.player_jump_effect = pygame.mixer.Sound('jump.mp3')
        self.player_jump_effect.set_volume(0.05)


        self.image = pygame.image.load('ele.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(80, 450))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 450:
           self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 450:
            self.rect.bottom = 450

    def animation(self):
        if self.rect.bottom < 450:
            self.image = self.player_jump
            self.player_jump_effect.play()
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()


class Obstacles(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'bird':
            self.image = pygame.image.load('Picture 1.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom=(randint(900,1100), 415))
        else:
            self.image = pygame.image.load('cactus.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom=(randint(900,1100), 450))

    def update(self):
        self.rect.x -= 5

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_display = font1.render(f'Score: {current_time}', True, 'Black')
    time_rect = time_display.get_rect(center=(400, 100))
    screen.blit(time_display, time_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


screen = pygame.display.set_mode((800, 600))  # screen settings

pygame.display.set_caption('My game!')  # Name of window

player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()
bg_music = pygame.mixer.Sound('music.mp3')
bg_music.set_volume(0.3)
bg_music.play(loops = -1)




clock = pygame.time.Clock()  # frame rate clock

font1 = pygame.font.Font('OpenMine.ttf', 50)  # fonts for game title
font2 = pygame.font.Font('OpenMine.ttf', 80)
font3 = pygame.font.Font('OpenMine.ttf', 30)

# key variables
start_time = 0
final_score = 0


game_active = False


sky_surface = pygame.image.load('Sky 15.25.22.png').convert()

ground_surface = pygame.image.load('ground2.png').convert()
ground_rect = ground_surface.get_rect(topleft=(0,450))


game_over_image = pygame.image.load('final_ele 15.25.22.png').convert_alpha()
game_over_image_rect = game_over_image.get_rect(center=(400,300))

instruction_text = font1.render('Press SPACE to start.', True, 'Grey')
instruction_text_rect = instruction_text.get_rect(center=(400,450))

tribute_text = font3.render('Developed by adnannextdoor', True, 'Black')
tribute_text_rect = tribute_text.get_rect(bottomright=(795,595))

game_over_text = font2.render('Dodging Dumbo', True, 'Blue')
game_over_rect = game_over_text.get_rect(center=(400,150))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == obstacle_timer:
            obstacle_group.add(Obstacles(choice(['bird', 'cactus', 'cactus', 'cactus'])))

        if game_active == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)



    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, ground_rect)
        display_score()
        final_score = display_score()
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        game_active = collision_sprite()



        final_score_text = font1.render('Final score: ' + str(final_score), True, 'Black')
        final_score_rect = final_score_text.get_rect(topright=(795, 5))

    else:
        obstacle_speed = 5
        screen.fill('Light green')
        screen.blit(game_over_text, game_over_rect)
        screen.blit(game_over_image, game_over_image_rect)
        screen.blit(instruction_text, instruction_text_rect)
        screen.blit(tribute_text, tribute_text_rect)

        if final_score == 0:
            pass
        else:
            screen.blit(final_score_text, final_score_rect)

    pygame.display.update()
    clock.tick(60)




