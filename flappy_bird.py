import pygame, sys, random
#Tao ham cho game

#Ve nen va san duoi
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))#vi truc x la 432
    
#Tao cac ong
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos)) #Tao hinh chu nhat quanh ong
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos-720))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

#Ve cac ong
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 550 :
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True) # Lap theo truc nao thi de true o truc do
            screen.blit(flip_pipe, pipe)
            
#Kiem tra va cham
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe): #colliderect la mot ham co san trong pygame de kiem tra va cham
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    return True

def score_display():
    score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
    score_rect = score_surface.get_rect(center = (216,100))
    screen.blit(score_surface, score_rect)
    
pygame.mixer.pre_init(frequency=44100, size = -16, channels=2, buffer = 512)  

pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()

game_font = pygame.font.SysFont('04B_19.ttf', 40)

#Tao cac bien
gravity = 0.25 #Trong luc
bird_movement = 0
game_active = True
score = 0
high_score = 0

#Chen background
bg = pygame.image.load('images/background-night.png').convert() # convert giup pygame load anh nhanh hon
bg = pygame.transform.scale2x(bg)

#Chen san
floor  = pygame.image.load('images/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

#Tao chim
bird = pygame.image.load('images/yellowbird-midflap.png').convert_alpha()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,384)) # Tao mot hinh chu nhat quanh con chim

#Tao ong
pipe_surface = pygame.image.load('images/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

#Tao timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1500) # Sau 1.5s lai tao 1 ong moi
pipe_height = [200,300,400]

#Tao man hinh ket thuc
game_over_surface = pygame.transform.scale2x(pygame.image.load('images/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (216,384))

#Chen am thanhh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #Khi co 1 phim dc an xuong
            if event.key == pygame.K_SPACE and game_active: # an phim cach de tao su di chuyen cho chim
                bird_movement = 0 
                bird_movement = -11
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active==False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_movement = 0
                score = 0
        if event.type == spawnpipe:
                pipe_list.extend(create_pipe()) #pipe_list: chua cac ong vua moi tao
                
            
    screen.blit(bg,(0,0)) #(0,0): goc toa do
    if game_active:
        #Chim
        bird_movement +=gravity
        bird_rect.centery +=bird_movement
        screen.blit(bird, bird_rect)
        game_active = check_collision(pipe_list)

        #ong
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score+=0.005
        score_display()
    else:
        score_display()
        screen.blit(game_over_surface,game_over_rect)
        
    #San
    screen.blit(bird,bird_rect)
    floor_x_pos -=1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(120)
    
    
