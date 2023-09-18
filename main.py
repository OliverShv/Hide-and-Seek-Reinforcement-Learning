import environment

env = environment.Environment(True)

while True:
    
    env.step([1, 1])
    env.step([1, 2])

    env.step([0, 0])
    env.step([0, 3])
    

