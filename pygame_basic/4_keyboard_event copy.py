import pygame

pygame.init()

# screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("MyGame")

# import background image
background = pygame.image.load("C:/Users/eagle/Desktop/PythonWorkspace/background.png")

# import sprite(character)
character = pygame.image.load("C:/Users/eagle/Desktop/PythonWorkspace/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# moving position
to_x = 0
to_y = 0

# event loop
running = True # is the game running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))

    screen.blit(character, (int(character_x_pos), int(character_y_pos)))

    pygame.display.update()

          # exit
    pygame.quit()