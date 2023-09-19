class Agent:
    def __init__(self, x = 0, y = 0, role = "hider", env = None):
        #Constants
        self.ENV = env
        self.ROLE = role

        if self.ROLE == "hider":
            self.COLOR = (0,255,0)
            self.speed = 2
        else:
            self.COLOR = (255,0,0)
            self.speed = 1
        #variables
        self.x = x
        self.y = y
    
    def move(self, direction):

        #0: UP, 1: RIGHT, 2: DOWN, 3: LEFT

        if direction == 0:
            self.y-=self.speed
            if self.y < 0:
                self.y = 0

        elif direction == 1:
            self.x+=self.speed
            if self.x+1 > self.ENV.WIDTH:
                self.x = self.ENV.WIDTH - 1

        elif direction == 2:
            self.y+=self.speed
            if self.y+1 > self.ENV.HEIGHT:
                self.y = self.ENV.HEIGHT-1

        elif direction == 3:
            self.x-=self.speed
            if self.x < 0:
                self.x = 0

    
    def set_position(self, x, y):
        self.x = x
        self.y = y