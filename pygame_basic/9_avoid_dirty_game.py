import pygame
import random

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width =480
screen_height =640
screen = pygame.display.set_mode((screen_width, screen_height)) 
 
# 화면 타이틀 설정
pygame.display.set_caption("funny Game") #게임이름 

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/82102/Desktop/PythonWorkspace/pygame_basic/ground.jpg")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/82102/Desktop/PythonWorkspace/pygame_basic/timo.jpg")
character_size = character.get_rect().size # 이미지의 크기를 구해옴 
character_width = character_size[0]  #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2 ) - (character_width / 2)#화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height- character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

#FPS 초당 프레임 변수 설정
clock = pygame.time.Clock()

# 이동 속도
character_speed = 10

#적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/82102/Desktop/PythonWorkspace/pygame_basic/honey.jpg")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴 
enemy_width = enemy_size[0]  #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로 크기
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10


#이동할 좌표
to_x = 0

#폰트 정의 
game_font = pygame.font.Font('Maplestory Bold.ttf', 40) #폰트 객체 생성(폰트, 크기)

#총 시간 
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

#이벤트 루프
running = True  #게임이 진행중인가? 
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는지
         running = False #게임이 진행중이 아님
 
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
           if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed #to_x = to_x -5
           elif event.key == pygame.K_RIGHT:  #캐틱터를 오른쪽으로
                to_x += character_speed
         
                
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤 
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0 
       

    character_x_pos += to_x
    enemy_y_pos +=  enemy_speed 
 

    #가로 경계값 처리 
    if character_x_pos < 0:
         character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
         character_x_pos = screen_width - character_width
    
    if enemy_y_pos > screen_height:
       enemy_y_pos = 0
       enemy_x_pos = random.randint(0, screen_width - enemy_width)
       

    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos 
    
    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했음")
        running=False

    screen.blit(background, (0,0))   #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() -start_ticks) / 1000
    #경과 시간(ms)을 1000으로 나누어서 초 단위로 표시 

    str1= "제한 시간:"
    timer = game_font.render(str1+str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer,(10,10))

    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time < 0 :
        print("타임 아웃")
        running = False
    pygame.display.update() #게임 화면을 다시그리기!

   #pygame 종료    
pygame.quit()

