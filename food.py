class Food:
    def __int__(self):
        x=random.randint(0,GAME_WIDTH/SPACE_SIZE-1)*SPACE_SIZE
        y=random.randint(0,GAME_WIDTH/SPACE_SIZE-1)*SPACE_SIZE
        self.coordinates=[x,y]
        canvas.create_oval(x, y,y+SPACE_SIZE, fill=FOOD_COLOR,tag="food")