class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]
        for i in range(0,BODY_PARTS):
            self.coordiantes.append([0,0])

        for x,y in self.coordinates:
           square= canvas.create_rectangle(x, y,x+SPACE_SIZE, fill=FOOD_COLOR,tag="snake")
           self.squaresappend(square)    