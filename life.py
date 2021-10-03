import random, time, os

class Life():
    def __init__(self):
        
        size = os.get_terminal_size()
        self.rows = size.lines-1
        self.cols = size.columns-1
        
        self.state = [[random.randrange(0,2) for y in range(self.cols)] for x in range(self.rows)]
        self.next = [[0 for y in range(self.cols)] for x in range(self.rows)]
    
    def step(self):
        # first count neighbors, add 1 to each neighboring cell
        for x in range(1,self.rows-1):
            for y in range(1,self.cols-1):
                if(self.state[x][y] == 1):
                    self.next[x-1][y-1] += 1
                    self.next[x-1][y] += 1
                    self.next[x-1][y+1] += 1
                    self.next[x][y-1] += 1
                    self.next[x][y+1] += 1
                    self.next[x+1][y-1] += 1
                    self.next[x+1][y] += 1
                    self.next[x+1][y+1] += 1
        
        # apply rules tou neighbour counts
        for x in range(0,self.rows):
            for y in range(0,self.cols):
                cell = self.state[x][y]
                
                # Any live cell with two or three live neighbours survives.
                # Any dead cell with three live neighbours becomes a live cell.
                # All other live cells die in the next generation.
                
                if cell == 1 and self.next[x][y] in [2,3]:
                    self.next[x][y] = 1
                elif cell == 0 and self.next[x][y] == 3:
                    self.next[x][y] = 1
                else:
                    self.next[x][y] = 0
        
        self.state = self.next
        self.next = [[0 for y in range(self.cols)] for x in range(self.rows)]
    
    def draw(self):
        for row in self.state:
            for cell in row:
                print(" " if cell==0 else u"\u2588", end='')
            print(" ")
            
life = Life()
while 1:
    os.system("clear")
    life.draw()
    time.sleep(0.04)
    life.step()