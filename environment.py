import pygame
import sys
from agent import Agent

class Environment:
    #TODO have map to all positions of agents so we can check if an agent colliides when it enters a square instead of comapring the positions of all agents
    def __init__(self, render = False):
        self.render = render

        # Constants
        self.SCALE = 50
        self.WIDTH, self.HEIGHT = 10, 10
        self.BACKGROUND_COLOR = (0, 0, 0)       # Black
        self.GRID_COLOR = (25, 25, 25)       # Light Grey

        self.SEEKER_COLOR = (255,0,0)        # Red
        self.HIDER_COLOR = (0,255,0)        # Green

        # Variables
        self.hider = Agent(9,9,"hider",self)
        self.seeker = Agent(0,0,"seeker",self)

        self.agents = [self.hider, self.seeker]

        if self.render:
            # Initialize Pygame
            self.clock = pygame.time.Clock()
            pygame.init()

            # Create the Pygame window
            self.screen = pygame.display.set_mode((self.WIDTH*self.SCALE, self.HEIGHT*self.SCALE))
            pygame.display.set_caption("Hide and Seek")

    def step(self, action, player):
        done = False
        self.agents[player].move(action)
        
        if self.render:
            # Clear the screen
            self.screen.fill(self.BACKGROUND_COLOR)

            # Draw agents
            for agent in self.agents:
                pygame.draw.rect(self.screen, agent.COLOR, (agent.x*self.SCALE,agent.y*self.SCALE,self.SCALE,self.SCALE))
            
            # Draw the grid
            for x in range(0, self.WIDTH, self.SCALE):
                pygame.draw.line(self.screen, self.GRID_COLOR, (x, 0), (x, self.HEIGHT), 1)
            for y in range(0, self.HEIGHT, self.SCALE):
                pygame.draw.line(self.screen, self.GRID_COLOR, (0, y), (self.WIDTH, y), 1)

            # Update the screen
            pygame.display.flip()

            # Limit the frame rate to the target FPS
            self.clock.tick(5)
        
        if self.agents[0].x==self.agents[1].x and self.agents[0].y==self.agents[1].y:
            done = True

        reward = self.distance_inverse()

        if player == 0:
            reward = -reward

        state = [self.hider.x,self.hider.y,self.seeker.x,self.seeker.y]

        print([player, state, reward, done])
        return state, reward, done
    
    def distance_inverse(self):
        return 1/max((((self.hider.x-self.seeker.x)**2+(self.hider.y-self.seeker.y)**2)**0.5),0.1)

    def reset(self):
        self.seeker.set_position(0,0)
        self.hider.set_position(9,9)

    def quit(self):
        # Quit Pygame
        pygame.quit()
        sys.exit()