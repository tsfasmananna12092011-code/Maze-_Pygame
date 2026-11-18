from pygame import *

window = display.set_mode((700, 500))
display.set_caption('ЛАБИРИНТ')
display.set_icon(image.load('cyborg.png'))
background = transform.scale(image.load('background3.png'),(700,500))


mixer.init()
mixer.music.load('jungles.ogg')
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

count = 0
end = 0

font.init()
font_lose = font.Font(None, 100)
font_lifes = font.Font(None, 100)
font_win = font.Font(None, 70)
lose_text = font_lose.render('YOU LOSE! - 1 LIFE', True, (250,0,0))
win_text = font_win.render('YOU WIN! GOOD JOB!', True, (82, 252, 3))
start_text = font_lose.render('LIFES: 3', True, (252, 186, 3))
start1_text = font_lifes.render('LIFES: 2', True, (252, 186, 3))
start2_text = font_lifes.render('LIFES: 1 ', True, (252, 186, 3))
start3_text = font_lifes.render('LIFES: 0 ', True, (252, 186, 3))
lose2_text = font_lifes.render('YOU LOSE! 0 LIFES LEFT', True, (250,0,0))

clock = time.Clock()
FPS = 50

class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(filename),(width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def appear(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
            
class Enemy(GameSprite):
    direction = 'right'
    def update(self):
        if self.rect.x <= 270:
            self.direction = 'right'
        if self.rect.x >= 510:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
            
w_width= 10
w_color = (252, 186, 3)

player = Player('hero.png', 40, 20, 10, 65, 65)
cyborg = Enemy('cyborg.png', 500, 200, 5, 65, 65 )
prize = GameSprite('treasure.png', 310, 400, 0, 80, 80 )

wall1 = Wall(color= w_color, wall_x= 20, wall_y= 50, wall_width = w_width, wall_height = 240)
wall2 = Wall(color= w_color, wall_x= 120, wall_y= 50, wall_width = w_width, wall_height = 120)
wall3 = Wall(color= w_color, wall_x= 20, wall_y= 280, wall_width = w_width, wall_height = 120)
#wall3 = Wall(color= w_color, wall_x= 20, wall_y= 280, wall_width = 120, wall_height = w_width)
wall4 = Wall(color= w_color, wall_x= 120, wall_y= 50, wall_width = 550, wall_height = w_width)
wall5 = Wall(color= w_color, wall_x= 240, wall_y= 50, wall_width = 120, wall_height = w_width)
wall6 = Wall(color= w_color, wall_x= 240, wall_y= 160, wall_width = 120, wall_height = w_width)
wall7 = Wall(color= w_color, wall_x= 120, wall_y= 280, wall_width = 420, wall_height = w_width)
wall8 = Wall(color= w_color, wall_x= 240, wall_y= 170, wall_width = w_width, wall_height = 120)
wall9 = Wall(color= w_color, wall_x= 20, wall_y= 390, wall_width = 220, wall_height = w_width)
wall10 = Wall(color= w_color, wall_x= 480, wall_y= 160, wall_width = 190, wall_height = w_width)
wall11 = Wall(color= w_color, wall_x= 240, wall_y= 280, wall_width = w_width, wall_height = 120)
wall12 = Wall(color= w_color, wall_x= 660, wall_y= 50, wall_width = w_width, wall_height = 350)
wall13 = Wall(color= w_color, wall_x= 450, wall_y= 390, wall_width = 210, wall_height = w_width)

    





mixer.music.play(-1)
mixer.music.set_volume(0.03)
game = True
finish = False
win, lose = False, False
while game:
    window.blit(background,(0,0))
    player.appear()
    cyborg.appear()
    prize.appear()
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    wall8.draw_wall()
    wall9.draw_wall()
    wall10.draw_wall()
    wall11.draw_wall()
    wall12.draw_wall()
    wall13.draw_wall()
    if count == 0:
        window.blit(start_text, (20, 420))
    if count == 1:
        window.blit(start1_text, (20, 420))
    if count == 2:
        window.blit(start2_text, (20, 420))
    
    


    if not finish:
        player.update()
        cyborg.update()
        if (sprite.collide_rect(player,cyborg)
            or sprite.collide_rect(player, wall1)
            or sprite.collide_rect(player, wall2)
            or sprite.collide_rect(player, wall3)
            or sprite.collide_rect(player, wall4)
            or sprite.collide_rect(player, wall5)
            or sprite.collide_rect(player, wall6)
            or sprite.collide_rect(player, wall7)
            or sprite.collide_rect(player, wall8)
            or sprite.collide_rect(player, wall9)
            or sprite.collide_rect(player, wall10)
            or sprite.collide_rect(player, wall11)
            or sprite.collide_rect(player, wall12)
            or sprite.collide_rect(player, wall13)):
            finish = True
            kick.play()
            lose = True
        if (sprite.collide_rect(player, prize)):
            finish = True
            money.play()
            win = True
        if lose == True and win == False:
            window.blit(lose_text, (700 // 15, 500 // 2))
        #if lose == False and win == True:
            #window.blit(win_text, (700 // 4, 500 // 2))
    else:
        if count < 2 and win == False:
            time.delay(3000)
            finish = False
            lose, win = False, False
            count += 1
            end += 1


            player = Player('hero.png', 40, 20, 10, 65, 65)
            cyborg = Enemy('cyborg.png', 500, 200, 5, 65, 65 )
            prize = GameSprite('treasure.png', 310, 400, 0, 80, 80 )

            wall1 = Wall(color= w_color, wall_x= 20, wall_y= 50, wall_width = w_width, wall_height = 240)
            wall2 = Wall(color= w_color, wall_x= 120, wall_y= 50, wall_width = w_width, wall_height = 120)
            wall3 = Wall(color= w_color, wall_x= 20, wall_y= 280, wall_width = w_width, wall_height = 120)
            #wall3 = Wall(color= w_color, wall_x= 20, wall_y= 280, wall_width = 120, wall_height = w_width)
            wall4 = Wall(color= w_color, wall_x= 120, wall_y= 50, wall_width = 550, wall_height = w_width)
            wall5 = Wall(color= w_color, wall_x= 240, wall_y= 50, wall_width = 120, wall_height = w_width)
            wall6 = Wall(color= w_color, wall_x= 240, wall_y= 160, wall_width = 120, wall_height = w_width)
            wall7 = Wall(color= w_color, wall_x= 120, wall_y= 280, wall_width = 420, wall_height = w_width)
            wall8 = Wall(color= w_color, wall_x= 240, wall_y= 170, wall_width = w_width, wall_height = 120)
            wall9 = Wall(color= w_color, wall_x= 20, wall_y= 390, wall_width = 220, wall_height = w_width)
            wall10 = Wall(color= w_color, wall_x= 480, wall_y= 160, wall_width = 190, wall_height = w_width)
            wall11 = Wall(color= w_color, wall_x= 240, wall_y= 280, wall_width = w_width, wall_height = 120)
            wall12 = Wall(color= w_color, wall_x= 660, wall_y= 50, wall_width = w_width, wall_height = 350)
            wall13 = Wall(color= w_color, wall_x= 450, wall_y= 390, wall_width = 210, wall_height = w_width)
        else:
            if win == False:
                window.blit(lose2_text, (700 // 22, 500 // 2))
                window.blit(start3_text, (20, 420))
            if win == True:
                window.blit(win_text, (700 // 10, 500 // 2))
                
            

            

        



    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)







