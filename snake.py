import pygame
import random
import os

# applying Music
pygame.mixer.init()

pygame.init()

# colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,200,0)
grey = (80, 80, 80)




s_height = 700 
s_width = 600

gamewindow = pygame.display.set_mode((s_height,s_width))

pygame.display.set_caption("Snake")
pygame.display.update()


clock = pygame.time.Clock()

font = pygame.font.SysFont(None,30) 

def text_screen(text, color, x, y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

# Create an empty list to store snake body positions


def plot_snake(gamewindow,color,snk_list,snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gamewindow, color,[x,y,snake_size,snake_size] )


def gameloop():
    
    exit_game  = False
    game_over = False
    # snake
    snake_x = 45
    snake_y = 100
    snake_size = 10
    # velocity
    velocity_x = 0
    velocity_y = 0
    int_vel = 5
    # food => apple
    food_x = random.randint(0,s_height)
    food_y = random.randint(0,s_width-30)
    food_radius = 5
    # score position
    score_x = 5
    score_y = 5

    snk_list = []
    snk_length = 1

    score = 0
    fps = 60

    while not exit_game:
        if game_over:
            gamewindow.fill("white")
            text_screen("Game Over! Press Enter to continue",red,x = s_height/4, y = s_width/3)   # text_screen => to print


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.key == pygame.K_RETURN:
                    gameloop()    

        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = int_vel
                        velocity_y = 0
                        # snake_x = snake_x + 30

                    if event.key == pygame.K_LEFT:
                        velocity_x = -int_vel
                        velocity_y = 0
                        # snake_x = snake_x - 30  

                    if event.key == pygame.K_UP:
                        velocity_x =0
                        velocity_y = -int_vel
                        # snake_y = snake_y - 30  

                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = int_vel
                        # snake_y = snake_y + 30
            if not os.path.exists("hiscore.txt"):
                with open("hiscore.txt","w") as f:
                    f.write("0")

            with open("hiscore.txt","r") as f:
                hiscore = f.read()

            # Snake eat apple and new position for the apple   
            if abs(snake_x-food_x)<12 and abs(snake_y-food_y)<12:  # agr snake or apple ki axis mei max 6unit ka fark bhi ho toh wo 1 point ho jaega
                score += 10
                food_x = random.randint(0,s_height)
                food_y = random.randint(0,s_width)
                snk_length += 5
                # sound effect
                pygame.mixer.music.load('snake\music\Beep Short .mp3')
                pygame.mixer.music.play()

                # increse high score when the score id greater than hs
                if score > int(hiscore):
                    new_content = hiscore.replace(hiscore,str(int(hiscore)+10))
                    with open("hiscore.txt", 'w') as file:
                        file.write(new_content)      

            # Condition for game over
            if(snake_x > s_height or snake_x < 0 or snake_y > s_width or snake_y<0):
                game_over = True
                pygame.mixer.music.load('snake\music\game-over-arcade-6435.mp3')
                pygame.mixer.music.play()
                
                
            # increase the velocity of snake  
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            gamewindow.fill(white)    ## fill the color to the window
            text_screen("Score: "+ str(score),red,score_x,score_y)
            text_screen("High Score:"+ hiscore,grey,score_x+120,score_y)

            # initially defining the snake head
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if(len(snk_list)>snk_length):
                snk_list.pop(0)

            # game over when snake bite itself
            if(len(snk_list)>1):
                for ele in range(1,len(snk_list)):
                    if snk_list[0] == snk_list[ele]:
                        game_over = True
                        pygame.mixer.music.load('snake\music\game-over-arcade-6435.mp3')
                        pygame.mixer.music.play()


            # pygame.draw.rect(gamewindow, black,[snake_x,snake_y,snake_size,snake_size] )
            plot_snake(gamewindow,black,snk_list,snake_size)
            pygame.draw.circle(gamewindow, green,[food_x,food_y,],radius=food_radius)

        pygame.display.update()    # any change can be done to the window after the update    
        clock.tick(fps)

gameloop()
pygame.quit()
quit()            


