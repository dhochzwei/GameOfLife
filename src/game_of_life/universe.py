import numpy as np
import random as rand

class Universe:
    def __init__(self,size = 5):
        self.age = 0
        self.N = size
        self.grid = np.zeros((size,size))
        

    def create(self):
        for i in range(self.N):
            for j in range(self.N):
                self.grid[i,j] = rand.randrange(0,2)
        

    def simulate_step(self):
        index_shift_right =[self.N-1]+ list(range(0,self.N-1))
        index_shift_left =list(range(1,self.N))+[0]
        north = self.grid[index_shift_right]
        northeast = self.grid[:,index_shift_left][index_shift_right]
        east = self.grid[:,index_shift_left]
        southeast = self.grid[:,index_shift_left][index_shift_left]
        south = self.grid[index_shift_left]
        southwest = self.grid[:,index_shift_right][index_shift_right]
        west = self.grid[:,index_shift_right]
        northwest = self.grid[:,index_shift_right][index_shift_left]
        
        neighbors = north + northeast + east + southeast + south + southwest + west+ northwest
        #print(neighbors)

        #if a cell has less than two or more than three neighbors, it will be dead for sure
        self.grid[neighbors<2] = 0
        self.grid[neighbors>3] = 0
        #cells with exactly three neighbors will be alive in the next step
        self.grid[neighbors==3] = 1
        self.age += 1

    def get_grid(self):
        return self.grid

    def set_grid(self,grid):
        self.grid = grid

    def set_grid_value(self,x,y,value):
        pass

    def get_age(self):
        return self.age