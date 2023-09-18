class Agent:
    def __init__(self, x = 0, y = 0, role = "hider", env = None):
        #Constants
        self.ENV = env
        self.ROLE = role

        if self.ROLE == "hider":
            self.COLOR = (0,255,0)
        else:
            self.COLOR = (255,0,0)

        #variables
        self.x = x
        self.y = y
    
    def move(self, direction):

        #0: UP, 1: RIGHT, 2: DOWN, 3: LEFT

        if direction == 0:
            if self.y != 0:
                self.y-=1
        elif direction == 1:
            if self.x+1 != self.ENV.WIDTH:
                self.x+=1
        elif direction == 2:
            if self.y+1 != self.ENV.HEIGHT:
                self.y+=1
        elif direction == 3:
            if self.x != 0:
                self.x-=1
    
    def set_position(self, x, y):
        self.x = x
        self.y = y