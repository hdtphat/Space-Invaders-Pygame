import pygame
import random
window_width = 1200
window_height = 750
pygame.init()
pygame.mixer.init()
pygame.font.init()
# creating window
playing_screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")
# text fonts
name_font  = pygame.font.SysFont("verdena", 120, "bold")
title_font = pygame.font.SysFont("verdena", 60)
guide_font = pygame.font.SysFont("verdena", 30)
credit_font = pygame.font.SysFont("verdena", 20)
score_font = pygame.font.SysFont("freesansbold", 60)
level_lives_font = pygame.font.SysFont("verdena", 50)
level_up_font = pygame.font.SysFont("verdena", 120, "bold")
loss_font = pygame.font.SysFont("verdena", 130, "bold")
# spaceship images
red_ship_img   = pygame.image.load("my_images/red_ship.png")
green_ship_img = pygame.image.load("my_images/green_ship.png")
blue_ship_img  = pygame.image.load("my_images/blue_ship.png")
player_ship_img = pygame.image.load("my_images/player_ship.png")
boss_ship_img =  pygame.image.load("my_images/boss_img.png")
# bullet images
red_lazer_img = pygame.image.load("my_images/red_lazer.png")
green_lazer_img = pygame.image.load("my_images/green_lazer.png")
blue_lazer_img = pygame.image.load("my_images/blue_lazer.png")
player_lazer_img = pygame.image.load("my_images/player_lazer.png")
player_lv2_lazer_img = pygame.image.load("my_images/lv2_laser.png")
player_lv3_lazer_img = pygame.image.load("my_images/lv3_laser.png")
boss_lazer_img = pygame.image.load("my_images/boss_lazer.png")
# buff item images 
buff_health_img = pygame.image.load("my_images/buff_health.png")
buff_mana_img = pygame.image.load("my_images/buff_mana.png")
buff_damage_img = pygame.image.load("my_images/buff_damage.png")
buff_speed_img = pygame.image.load("my_images/buff_speed.png")
buff_live_img = pygame.image.load("my_images/buff_live.png")
buff_shield_img = pygame.image.load("my_images/buff_shield.png")
buff_fire_img = pygame.image.load("my_images/buff_fire_rate.png")
buff_devil_img = pygame.image.load("my_images/buff_devil.png")
# special skill images
shield_img = pygame.image.load("my_images/force_shield.png")
super_attack_img = pygame.image.load("my_images/super_attack.png")
portal_red = pygame.image.load("my_images/portal_red.png")
portal_green = pygame.image.load("my_images/portal_green.png")
portal_blue = pygame.image.load("my_images/portal_blue.png")
portal_purple = pygame.image.load("my_images/portal_purple.png")
# explsion images
explosion1_img = pygame.image.load("my_images/explosion_1.png")
explosion2_img = pygame.image.load("my_images/explosion_2.png")
explosion3_img = pygame.image.load("my_images/explosion_3.png")
explosion4_img = pygame.image.load("my_images/explosion_4.png")
# load and scale background image
background_img = pygame.image.load("my_images/background.png")
background_img = pygame.transform.scale(background_img, (window_width, window_height))
# spaceships got hit sound
player_hit_enermy = pygame.mixer.Sound('my_sound_tracks/explosion_1.mp3')
player_hit_enermy.set_volume(1)
enermy_hit_player = pygame.mixer.Sound('my_sound_tracks/explosion_2.mp3')
enermy_hit_player.set_volume(1)
# special skill sound
super_attack_sound = pygame.mixer.Sound('my_sound_tracks/super_attack.mp3')
super_attack_sound.set_volume(0.2)
teleport_sound = pygame.mixer.Sound('my_sound_tracks/teleport-36569.mp3')
teleport_sound.set_volume(1)
# spaceships shooting sound
player_shooting_sound = pygame.mixer.Sound('my_sound_tracks/player_shooting_laser.mp3')
player_shooting_sound.set_volume(0.5)
enermy_shooting_sound = pygame.mixer.Sound('my_sound_tracks/enermy_shooting_laser.mp3')
enermy_shooting_sound.set_volume(0.3)
boss_shooting_sound = pygame.mixer.Sound('my_sound_tracks/boss_shooting_lazer.mp3')
boss_shooting_sound.set_volume(1)
# background sound tracks
shield_sound = pygame.mixer.Sound('my_sound_tracks/shield_sound.mp3')
shield_sound.set_volume(1)
item_sound = pygame.mixer.Sound('my_sound_tracks/buff_item_sound.mp3')
item_sound.set_volume(1)
enermy_got_hit_sound = pygame.mixer.Sound('my_sound_tracks/explosion_1.mp3')
enermy_got_hit_sound.set_volume(1)
player_got_hit_sound = pygame.mixer.Sound('my_sound_tracks/explosion_2.mp3')
player_got_hit_sound.set_volume(1)
boss_spawn_sound = pygame.mixer.Sound('my_sound_tracks/boss_spawn.mp3')
boss_spawn_sound.set_volume(1)
level_up_sound = pygame.mixer.Sound('my_sound_tracks/level_up.mp3')
level_up_sound.set_volume(1)
background_track = pygame.mixer.Sound('my_sound_tracks/background_music.mp3')
background_track.set_volume(0.3)
background_track.play(-1) # play repeatly
# stats dictionary 
stats_dict = {# Name ----- Ship.Img ------ Lazer.Img ------ Health - Damage - Move.S - Lazer.S - Mana - Fire rate
              'red':    (red_ship_img,    red_lazer_img,      2,       3,       2,       4),
              'green':  (green_ship_img,  green_lazer_img,    3,       7,       1,       3),
              'blue':   (blue_ship_img,   blue_lazer_img,     1,       1,       2,       5),
              'boss':   (boss_ship_img,   boss_lazer_img,     100,     9,       1,       10),
              'player': (player_ship_img, player_lazer_img,   20,      1,       4,       10,      10,       40)}
# item dictionary
item_dict = {# Name  -------  Image  ---------  health  -------------------   mana  --------  damage - speed - live - fire rate
            'health':   (buff_health_img, stats_dict['player'][2],               0,              0,      0,     0,       1),
            'mana':     (buff_mana_img,            0,                stats_dict['player'][6],    0,      0,     0,       1),
            'damage':   (buff_damage_img,          0,                            0,              0.5,    0,     0,       1),
            'speed':    (buff_speed_img,           0,                            0,              0,      1,     0,       1),
            'live':     (buff_live_img,            0,                            0,              0,      0,     1,       1),
            'fire rate':(buff_fire_img,            0,                            0,              0,      0,     0,       0.9),
            'shield':   (buff_shield_img,          0,                            0,              0,      0,     0,       1),
            'devil':    (buff_devil_img,  stats_dict['player'][2],   stats_dict['player'][6],    1,      1,     3,       0.9)}

##################################################################### Object Classes #####################################################################
class level_up_notice():
    def __init__(self):
        self.level_up_banner_counter = 90
    def draw(self):
        level_up = level_up_font.render("LEVEL UP!", 1, (255, 255, 102))
        playing_screen.blit(level_up, (window_width/2 - level_up.get_width()/2, window_height/2 - level_up.get_height()/2))

class item():
    def __init__(self, x, y=-300):
        self.x = x
        self.y = y
        self.move_speed = 2
        buff = random.choice(['health', 'mana', 'damage', 'speed', 'live', 'fire rate', 'shield', 'devil'])
        self.image = item_dict[buff][0]
        self.buff_health = item_dict[buff][1]
        self.buff_mana = item_dict[buff][2]
        self.buff_damage = item_dict[buff][3]
        self.buff_speed = item_dict[buff][4]
        self.buff_live = item_dict[buff][5]
        self.buff_fire_rate = item_dict[buff][6]
        self.mask = pygame.mask.from_surface(self.image)
    def move_and_draw(self):
        self.y+=self.move_speed
        x = self.x-5
        y = self.y-5
        width = self.image.get_width()+10
        height = self.image.get_height()+10
        pygame.draw.rect(playing_screen, (random.randrange(0, 254), random.randrange(0, 254), random.randrange(0, 254)), (x, y, width, height))      
        playing_screen.blit(self.image, (self.x, self.y))

class force_shield():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.image = shield_img
        self.mask = pygame.mask.from_surface(self.image)
    def draw(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        playing_screen.blit(self.image, (self.x, self.y))


class portal_in():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.portal_remain_counter = 60
    def draw_portal(self):
        portal_img = random.choice([portal_green, portal_blue])
        playing_screen.blit(portal_img, (self.x, self.y))

class portal_out():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.portal_remain_counter = 60
    def draw_portal(self):
        portal_img = random.choice([portal_purple, portal_red])
        playing_screen.blit(portal_img, (self.x, self.y))

class bunch_of_kitty():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = super_attack_img
        self.move_speed = 5
        self.mask = pygame.mask.from_surface(self.image)
    def move_and_draw(self):
        self.y -= self.move_speed
        playing_screen.blit(self.image, (self.x, self.y))
    def get_width(self):
        return self.image.get_width()
    def get_height(self):
        return self.image.get_height()

class explosion():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.explosion_remain_counter = 20
    def draw_explosion(self):
        explosion_img = random.choice([explosion1_img, explosion2_img, explosion3_img, explosion4_img])
        self.explosion_remain_counter -= 1
        playing_screen.blit(explosion_img, (self.x, self.y))

class lazer():
    def __init__(self, x, y, lazer_img, lazer_speed):
        self.x = x
        self.y = y
        self.lazer_img = lazer_img
        self.lazer_speed = lazer_speed
        self.mask = pygame.mask.from_surface(self.lazer_img)
    def move_and_draw_lazer(self):
        self.y += self.lazer_speed
        playing_screen.blit(self.lazer_img, (self.x, self.y))

##################################################################### Spaceship Classes #####################################################################
class player():
    def __init__(self):
        self.x = int(window_width/2 - stats_dict['player'][0].get_width()/2)
        self.y = 600
        self.ship_img = stats_dict['player'][0]
        self.lazer_img = stats_dict['player'][1]
        self.health = stats_dict['player'][2]
        self.damage = stats_dict['player'][3]
        self.move_speed = stats_dict['player'][4]
        self.lazer_speed = stats_dict['player'][5]
        self.mana = stats_dict['player'][6]
        self.fire_rate = stats_dict['player'][7]
        self.shooting_counter = stats_dict['player'][7]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.lazers_shot = []
        self.portal_exist = []
        self.super_attack = []
    def draw_ship(self):
        playing_screen.blit(self.ship_img, (self.x, self.y))
    def draw_health_mana_bar(self):
        # draw rectangle: window, color, (x-cordinate, y-cordinate, width, height), thickness
        max_health = stats_dict['player'][2]
        pygame.draw.rect(playing_screen, (255,69,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 7))                             
        pygame.draw.rect(playing_screen, (69,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/max_health), 7))
        pygame.draw.rect(playing_screen, (0, 0, 0),  (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 7), 1)
        max_mana = stats_dict['player'][6]
        pygame.draw.rect(playing_screen, (255,69,0), (self.x, self.y + self.ship_img.get_height() + 17, self.ship_img.get_width(), 5))                             
        pygame.draw.rect(playing_screen, (69,69,255), (self.x, self.y + self.ship_img.get_height() + 17, self.ship_img.get_width() * (self.mana/max_mana), 5))
        pygame.draw.rect(playing_screen, (0, 0, 0),  (self.x, self.y + self.ship_img.get_height() + 17, self.ship_img.get_width(), 5), 1)
    def get_width(self):
        return self.ship_img.get_width() 
    def get_height(self):
        return self.ship_img.get_width()
    def shoot(self):
        x = self.x + (self.ship_img.get_width() - self.lazer_img.get_width())/2
        new_lazer = lazer(x, self.y-65, self.lazer_img, -self.lazer_speed)
        self.lazers_shot.append(new_lazer)
        player_shooting_sound.play()
    def skill_tele(self):
        new_portal = portal_in(self.x-(portal_blue.get_width()-player_ship_img.get_width())/2, self.y)
        self.portal_exist.append(new_portal)
        tele_distance = 350
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # left
            if self.x-tele_distance > 0:
                self.x -= tele_distance
            else: self.x = 0
        if keys[pygame.K_d]: # right
            if self.x+tele_distance+self.get_width() < window_width:
                self.x += tele_distance
            else: self.x = window_width-self.get_width()
        if keys[pygame.K_w]: # up
            if self.y-tele_distance > 0:
                self.y -= tele_distance
            else: self.y = 0
        if keys[pygame.K_s]: # down
            if self.y+tele_distance+self.get_height()+15 < window_height:
                self.y += tele_distance
            else: self.y = window_height-self.get_height()
        new_portal = portal_out(self.x-(portal_blue.get_width()-player_ship_img.get_width())/2, self.y)
        self.portal_exist.append(new_portal)
        teleport_sound.play()
    def skill_super_attack(self):
        x = self.x - (super_attack_img.get_width() - self.ship_img.get_width())/2
        y = window_height+100
        new_super_attack = bunch_of_kitty(x, y)
        self.super_attack.append(new_super_attack)
        super_attack_sound.play()

class minions():
    def __init__(self, x, y, ship_img, lazer_img, health, damage, move_speed, lazer_speed):
        self.x = x
        self.y = y
        self.ship_img = ship_img
        self.lazer_img = lazer_img
        self.health = health
        self.damage = damage
        self.move_speed = move_speed
        self.lazer_speed = lazer_speed
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.lazers_shot = []
        self.minions_go_along = []
    def move_ship(self):
        self.y += self.move_speed
    def draw_ship(self):
        playing_screen.blit(self.ship_img, (self.x, self.y))
    def draw_health_bar(self):
        pass
    def get_width(self):
        return self.ship_img.get_width() 
    def get_height(self):
        return self.ship_img.get_width()  
    def shoot(self):
        if random.randint(0, 130)==1 and self.y>=20:
            x = self.x + (self.ship_img.get_width()-self.lazer_img.get_width())/2    
            y = self.y + self.ship_img.get_height()
            new_lazer = lazer(x, y, self.lazer_img, self.lazer_speed)
            self.lazers_shot.append(new_lazer)
            enermy_shooting_sound.play()

class boss():
    def __init__(self):
        self.x = int(window_width/2 - stats_dict['boss'][0].get_width()/2)
        self.y = -400
        self.ship_img = stats_dict['boss'][0]
        self.lazer_img = stats_dict['boss'][1]
        self.health = stats_dict['boss'][2]
        self.move_speed = stats_dict['boss'][4]
        self.lazer_speed = stats_dict['boss'][5]
        self.damage = stats_dict['boss'][3]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.lazers_shot = []
    def move_ship(self):
        destination = 20
        if self.y <= destination:
            self.y += self.move_speed
    def draw_ship(self):
        playing_screen.blit(self.ship_img, (self.x, self.y))
    def get_width(self):
        return self.ship_img.get_width() 
    def get_height(self):
        return self.ship_img.get_width()
    def draw_health_bar(self):
        # draw rectangle: window, color, (x-cordinate, y-cordinate, width, height), thickness
        max_health = stats_dict['boss'][2]
        pygame.draw.rect(playing_screen, (255,69,0), (self.x, self.y - 10, self.ship_img.get_width(), 7))                             
        pygame.draw.rect(playing_screen, (69,255,0), (self.x, self.y - 10, self.ship_img.get_width() * (self.health/max_health), 7))
        pygame.draw.rect(playing_screen, (0, 0, 0),  (self.x, self.y - 10, self.ship_img.get_width(), 7), 1)
    def shoot(self):
        if random.randint(0, 80)==1 and self.y>=20:    
            y = 100
            x = random.choice([self.x+20, self.x+110, self.x+290, self.x+385])
            new_lazer = lazer(x, y, self.lazer_img, self.lazer_speed)
            self.lazers_shot.append(new_lazer)
            boss_shooting_sound.play()

##################################################################### Main function #####################################################################
def main():
    global lives
    global current_score
    game_is_running = True
    game_loss = False
    loss_screen_counter = 90
    FPS = 60
    level = 0
    lives = 5
    current_score = -75
    wave_lenght = 2
    max_wave_lenght = 20
    enermy_exist = []
    item_exist = []
    global explosion_exist
    explosion_exist = []
    shield_exist = []
    health_regen_counter = 300 # gain 1 health point every 300 frames (5 sec)
    mana_regen_counter = 120 # gain 1 mana point every 120 frames (2 sec)
    skill_tele_counter = 60 # perform special skill 'teleport' once every 60 frames (1 sec)
    skill_super_counter = 300 # perform special skill 'super attack' once every 300 frames (5 sec)
    clock = pygame.time.Clock()
    level_up_banner = level_up_notice()
    show_level_up_banner = False
    player_spaceship = player()

    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def move_and_draw_player():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_spaceship.x - player_spaceship.move_speed > 0: # left
            player_spaceship.x -= player_spaceship.move_speed
        if keys[pygame.K_d] and player_spaceship.x + player_spaceship.move_speed + player_spaceship.get_width() < window_width: # right
            player_spaceship.x += player_spaceship.move_speed
        if keys[pygame.K_w] and player_spaceship.y - player_spaceship.move_speed > 0: # up
            player_spaceship.y -= player_spaceship.move_speed
        if keys[pygame.K_s] and player_spaceship.y + player_spaceship.move_speed + player_spaceship.get_height() + 15 < window_height: # down
            player_spaceship.y += player_spaceship.move_speed
        player_spaceship.draw_ship()
        player_spaceship.draw_health_mana_bar()

    def draw_player_lazers():
        for lazer in player_spaceship.lazers_shot:
            lazer.move_and_draw_lazer()
            if lazer.y <= -200:
                player_spaceship.lazers_shot.remove(lazer)

    def move_and_draw_enermies():
        global lives
        global current_score
        for item in enermy_exist:
            item.move_ship()
            item.draw_ship()
            item.draw_health_bar() # boss only
            if item.y >= window_height:
                enermy_exist.remove(item)
                current_score -= 30
                lives -= 1
                if current_score<=0:
                    current_score=0
                if lives<=0:
                    lives=0

    def draw_enermy_lazer():
        for enermy in enermy_exist:
            for lazer in enermy.lazers_shot:
                lazer.move_and_draw_lazer()
                if lazer.y >= window_height:
                    enermy.lazers_shot.remove(lazer)

    def draw_portal():
        for portal in player_spaceship.portal_exist:
            portal.draw_portal()
            portal.portal_remain_counter -= 1
            if portal.portal_remain_counter<=0:
                player_spaceship.portal_exist.remove(portal)

    def spawn_item():
        x = random.randint(0, window_width - buff_mana_img.get_width())
        new_buff_item = item(x)
        item_exist.append(new_buff_item)

    def spawn_explsion(enermy):
        global explosion_exist
        x_spawn_item = enermy.x + (enermy.get_width() - (buff_damage_img.get_width()+5))/2
        y_spawn_item = enermy.y + enermy.get_height()/2
        new_explosion = explosion(x_spawn_item, y_spawn_item)
        explosion_exist.append(new_explosion)

    def spawn_enermy():
        # spawn boss
        if level%5==0:
            new_enermy = boss()
            enermy_exist.append(new_enermy)
            boss_spawn_sound.play()
        # spawn minions
        else:
            for i in range(wave_lenght):
                x = random.randint(0, 1000)
                y = random.randint(-1600, -400)
                color = random.choice(['red', 'blue', 'green'])
                ship_img = stats_dict[color][0]
                lazer_img = stats_dict[color][1]
                health = stats_dict[color][2]
                damage =  stats_dict[color][3]
                move_speed =  stats_dict[color][4]
                lazer_speed =  stats_dict[color][5]
                new_enermy = minions(x, y, ship_img, lazer_img, health, damage, move_speed, lazer_speed)
                enermy_exist.append(new_enermy)

    def redraw_window():
        # refresh window (delete everythings)
        pygame.display.update()
        # draw background
        playing_screen.blit(background_img, (0,0))
        # draw super attack
        for attack in player_spaceship.super_attack:
            attack.move_and_draw()
            if attack.y <= -attack.get_height():
                player_spaceship.super_attack.remove(attack)
        # draw buff items
        for buff_item in item_exist:
            buff_item.move_and_draw()
            if buff_item.y >= window_height:
                item_exist.remove(buff_item)
        # draw explosions
        for explosion in explosion_exist:
            explosion.draw_explosion()
            if explosion.explosion_remain_counter<=0:
                explosion_exist.remove(explosion)
        # draw portals
        draw_portal()
        # draw enermies lazers
        draw_enermy_lazer()
        # draw enermies
        move_and_draw_enermies()
        # draw force shield
        for shield in shield_exist:
            shield.draw(player_spaceship.x - (shield_img.get_width() - player_ship_img.get_width())/2,
                        player_spaceship.y - (shield_img.get_height() - player_ship_img.get_height())/2)
        # draw player
        move_and_draw_player()
        # draw player's lazers
        draw_player_lazers()
        # draw texts on upper screen
        lives_label = level_lives_font.render(f"Lives: {lives}", 1, (255, 255, 160))
        level_label = level_lives_font.render(f"Level: {level}", 1, (255, 255, 160))
        score_label = score_font.render(f"Score: {current_score}", 1, (255, 255, 102))
        playing_screen.blit(lives_label, (20, 20))
        playing_screen.blit(level_label, (window_width - level_label.get_width() - 20, 20))
        playing_screen.blit(score_label, (window_width/2 - score_label.get_width()/2, 20))

    # main loop
    while game_is_running==True:
        clock.tick(FPS)
        # create new frame
        redraw_window()
        # check for player action
        keys = pygame.key.get_pressed()
        skill_tele_counter -= 1
        if keys[pygame.K_o] and player_spaceship.mana>=1 and skill_tele_counter<=0:
            player_spaceship.skill_tele()
            player_spaceship.mana -= 1
            if skill_tele_counter<=0:
                skill_tele_counter=60
        skill_super_counter -= 1
        if keys[pygame.K_p] and player_spaceship.mana>=7 and skill_super_counter<=0:
            player_spaceship.mana -= 7
            player_spaceship.skill_super_attack()
            if skill_super_counter<=0:
                skill_super_counter=40
        player_spaceship.shooting_counter -= 1
        if keys[pygame.K_k] and player_spaceship.shooting_counter<=0:
            player_spaceship.shoot()
            if player_spaceship.shooting_counter<=0:
                player_spaceship.shooting_counter = player_spaceship.fire_rate
        # player collides with items
        for buff_item in item_exist:
            if collide(player_spaceship, buff_item):
                item_sound.play()
                player_spaceship.health += buff_item.buff_health
                player_spaceship.mana += buff_item.buff_mana
                player_spaceship.damage += buff_item.buff_damage
                player_spaceship.move_speed += buff_item.buff_speed
                player_spaceship.fire_rate = int(player_spaceship.fire_rate * buff_item.buff_fire_rate)
                lives += buff_item.buff_live
                if buff_item.image == buff_devil_img and level%5!=0:
                    devil = boss()
                    enermy_exist.append(devil)
                if buff_item.image == buff_shield_img and len(shield_exist) == 0:
                    shield = force_shield()
                    shield_exist.append(shield)
                    shield_sound.play(-1)
                item_exist.remove(buff_item)
                if player_spaceship.health >= stats_dict['player'][2]:
                    player_spaceship.health = stats_dict['player'][2]
                if player_spaceship.mana >= stats_dict['player'][6]:
                    player_spaceship.mana = stats_dict['player'][6]
                if player_spaceship.fire_rate <= 20:
                    player_spaceship.fire_rate = 20
                if 2 <= player_spaceship.damage < 3:         
                    player_spaceship.lazer_img = player_lv2_lazer_img
                    player_spaceship.lazer_speed = 15
                elif player_spaceship.damage >= 3:
                    player_spaceship.lazer_img = player_lv3_lazer_img
                    player_spaceship.lazer_speed = 20
        # super attack collides with enermy (not boss)
        for enermy in enermy_exist:
            for supper_attack in player_spaceship.super_attack:
                if collide(enermy, supper_attack)  and isinstance(enermy, boss)==False:
                    enermy.health -= 3
                    if enermy.health <= 0:
                        enermy_got_hit_sound.play()
                        enermy_exist.remove(enermy)
                        spawn_explsion(enermy)
                        current_score += 15
        # player collides with enermy
        for enermy in enermy_exist:
            if collide(enermy, player_spaceship) and isinstance(enermy, boss)==False:
                player_spaceship.health -= enermy.health
                current_score -= 20
                if current_score<=0:
                    current_score=0
                enermy_exist.remove(enermy) 
                spawn_explsion(enermy)         
                player_got_hit_sound.play()
        # player's laser collides with enermy
        for laser in player_spaceship.lazers_shot:
            for enermy in enermy_exist:
                if collide(laser, enermy):
                    enermy.health -= player_spaceship.damage
                    enermy_got_hit_sound.play()
                    player_spaceship.lazers_shot.remove(laser)
                    if enermy.health <= 0:
                        x_spawn_item = enermy.x + (enermy.get_width() - (buff_damage_img.get_width()+5))/2
                        y_spawn_item = enermy.y + enermy.get_height()/2
                        enermy_exist.remove(enermy)
                        spawn_explsion(enermy)
                        current_score += 20
                        if random.randint(0,4)==0:      # (20% * 6/8) = 15% chance to drop item
                            new_buff_item = item(x_spawn_item, y_spawn_item)
                            if new_buff_item.image not in [buff_devil_img, buff_live_img]:
                                item_exist.append(new_buff_item)
        # enermies and lasers collide with player's shield
        if len(shield_exist) > 1:                            # chỉ để lại 1 shield để tránh lỗi
            for i in range(len(shield_exist)-1):             # enermy_exist.remove(enermy)
                shield_exist.remove(shield_exist[0])         # ValueError: list.remove(x): x not in list
        for enermy in enermy_exist:                          # nguyên nhân có thể do khi ng chơi có nhiều hơn 1 shield (ví dụ là 2)
            for laser in enermy.lazers_shot:                 # khi tất cả shield đó va chạm vs địch hoặc đạn thì tất cả 2 shield sẽ remove
                for shield in shield_exist:                  # nhưng địch chỉ có 1 và k thể remove 2 lần như shield dẫn đến lỗi
                    if collide(laser, shield):
                        shield_exist = []
                        enermy.lazers_shot.remove(laser)
                        player_got_hit_sound.play()
                        shield_sound.stop()
        for enermy in enermy_exist:
            for shield in shield_exist:
                if collide(enermy, shield):
                    shield_exist = []
                    enermy_exist.remove(enermy)
                    spawn_explsion(enermy)
                    player_got_hit_sound.play()
                    shield_sound.stop()
        # enermies shoot randomly and check for laser hit player
        for enermy in enermy_exist:
            enermy.shoot()
            for lazer in enermy.lazers_shot:
                if collide(lazer, player_spaceship):
                    player_got_hit_sound.play()
                    player_spaceship.health -= enermy.damage
                    enermy.lazers_shot.remove(lazer)
                    current_score -= 20
                    if current_score<=0:
                        current_score=0
                    if player_spaceship.health<=0:
                        player_spaceship.health=0
        # check for level up => spawn buff item and spawn new enermies
        if enermy_exist==[]:
            show_level_up_banner = True
            level+=1
            current_score+=75
            wave_lenght+=2
            if wave_lenght >= max_wave_lenght:
                wave_lenght = max_wave_lenght
            spawn_enermy()
            spawn_item()
            if level!=1:
                level_up_sound.play()
        if show_level_up_banner==True and level!=1 and game_loss==False:
            level_up_banner.draw()
            level_up_banner.level_up_banner_counter-=1
            if level_up_banner.level_up_banner_counter<=0:
                show_level_up_banner=False
                level_up_banner.level_up_banner_counter=90
        # spawn minions go along the boss
        if len(enermy_exist)==1 and isinstance(enermy_exist[0], boss): # if enermy_exist only contain boss
            for i in range(int(level/5)):
                x_is_not_valid = True
                while x_is_not_valid == True:           # cho nó spawn 2 bên vì nếu spawn đè lên boss sẽ gặp lỗi
                    number = random.randint(0, 1100)    # player_spaceship.lazers_shot.remove(laser)
                    if not (250 <= number <= 850):      # ValueError: list.remove(x): x not in list
                        x = number                      # có thể do laser đụng trúng boss vs minion cùng lúc, laser bị remove 2 lần
                        x_is_not_valid = False          # lần 1 thành công, lần 2 thì không thể do đã bị remove ở lần 1
                y = random.randint(-1600, -800)
                ship_img = stats_dict['blue'][0]
                lazer_img = stats_dict['blue'][1]
                health = stats_dict['blue'][2]
                damage =  stats_dict['blue'][3]
                move_speed =  stats_dict['blue'][4]
                lazer_speed =  stats_dict['blue'][5]
                new_minion_go_along_boss = minions(x, y, ship_img, lazer_img, health, damage, move_speed, lazer_speed)
                enermy_exist.append(new_minion_go_along_boss)
        # health regeneration
        health_regen_counter -= 1
        if health_regen_counter == 0:
            player_spaceship.health += 1
            if player_spaceship.health >= stats_dict['player'][2]:
                player_spaceship.health = stats_dict['player'][2]
        if health_regen_counter <=0:
            health_regen_counter = 300
        # mana regeneration
        mana_regen_counter -= 1
        if mana_regen_counter == 0:
            player_spaceship.mana += 1
            if player_spaceship.mana >= stats_dict['player'][6]:
                player_spaceship.mana = stats_dict['player'][6]
        if mana_regen_counter <=0:
            mana_regen_counter = 120
        # check for quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                game_is_running = False
        # check for loss
        if player_spaceship.health<=0 or lives<=0:
            game_loss = True
        if game_loss==True and loss_screen_counter>0:
            loss_screen_counter -= 1
            loss_label = loss_font.render("YOU LOSS!", 1, (255, 255, 102))
            playing_screen.blit(loss_label, (window_width/2 - loss_label.get_width()/2, window_height/2 - loss_label.get_height()/2))
        if game_loss==True and loss_screen_counter<=0:
            game_is_running = False

def lobby():
    run = True
    while run:
        # redraw lobby screen
        pygame.display.update()
        playing_screen.blit(background_img, (0,0))
        name_label = name_font.render("SPACE INVADERS", 1, (255, 255, 102))
        playing_screen.blit(name_label, (window_width/2 - name_label.get_width()/2, 270))
        blink_color = random.choice([(255, 255, 102), (125, 125, 125)])
        title_label = title_font.render("Press any key to start!", 1, blink_color)
        playing_screen.blit(title_label, (window_width/2 - title_label.get_width()/2, 360))
        guide_label = guide_font.render("WASD to move KOP to fight.", 1, blink_color)
        playing_screen.blit(guide_label, (window_width/2 - guide_label.get_width()/2, 415))
        credit_label = credit_font.render("@hdtphat", 1, (255, 255, 150))
        playing_screen.blit(credit_label, (window_width - credit_label.get_width() - 10, window_height - credit_label.get_height() - 10))
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()

lobby()