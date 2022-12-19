from tkinter import *
GAME_WIDTH =700
GAME HEIGHT=700
SPEED =50
SPACE_SIZE =50
BODY_PARTS=3
SNAKE_COLOR="#00FF00"
FOOD_COLOR="#FF0000"
BACKGROUND_COLOR="#000000"

def next_turn(snake,food):
    x,y=snake.coordinates[0]
    if direction ="up":
        y-=SPACE_SIZE
    elif direction =="down":
        y+=SPACE_SIZE
    elif direction == "left":
        x-=SPACE_SIZE
    elif direction=="right":
        x+=SPACE_SIZE
        square= canvas.create_rectangle(x,y, x+SPACE_SIZE,y+ SPACE_SIZE,fill=SNAKE_COLOR)
        snake.squares.insert(0,square)
    if x == food.coordinates[0] and y==food.coordinates[1]:
        del snake.squares[-1] 
        canvas.delete(snake(snake.squares[-1]))
        del.snake.squares[-1]
        global_score
        score+=1
        label.config(text="Score:".format(score))
        canvas.delete("food")    
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1]) 
        food=Food()

    def check_collisions(snake):
        x,y= snake.coordinates[0]
        if x< 0 or x> = GAME_WIDTH:

        elif y<0 or y>= GAME_HEIGHT:
            return True
    for body_part in snake.coordinates[1:]:
        if x== body_part[0]and y==body-part[1]:
            print('GAME OVER')
            return TRUE
        return False


    def change_direction(new_direction):
        if new_direction=='left':
            if direction!='right':
                direction=new_direction                

