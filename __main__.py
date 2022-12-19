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



    def change_direction(new_direction):
        if new_direction=='left':
            if direction!='right':
                direction=new_direction 
        elif new_direction =='right':
            if direction!='left':
                direction=new_direction
        elif new_direction =='up':
            if direction!='down':
                direction=new_direction
        elif new_direction=='right':
            if direction!='left':
                direction=new_direction
        elif new_direction=='up':
            if direction!='down':
                direction=new_direction
        elif new_direction=='down':
            if direction!='up':
                direction=new_direction    


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

                                                   

window=Tk()
window.title('snake game')
score =0
direction='down'
label=Label(window,text='score:{}'.format (score), font=('consolas',4))
label.pack()
canvas=Canvas(window,text,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.packwindow.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x= int((screen_width/2) -(window_width/2))
y= int((screen_height/2) -(window_height/2))
window.geometry(f"({window_width}*{window_height}+{x} +{y}")
window.bind('<left>',lambda event:change_direction('left'))
window.bind('<right>',lambda event:change_direction('right'))
window.bind('<left>',lambda event:change_direction('left'))
window.bind('<right>',lambda event:change_direction('right'))
snake=Snake()
food=Food()
next_turn(snake,food)
window.mainloop()

