class sudoku:
    def __init__(self,matrix):
        
        self.grid = matrix
    
    def __str__(self):
        string = ''

        for i in range(9):
            for j in range(9):
                string = string + str(self.grid[i][j])

            string = string + "\n"
        
        return string
    
    def input_num(self,i,j,num):

        self.grid[i][j] = num 

    def return_array(self):

        return self.grid
    
    def RCB_lists(self,x,y):

        row_list = self.grid[x]

        coloum_list = []
        for i in range(9):
            coloum_list.append(self.grid[i][y])

        box_list = []
        mod_r = (x+1) % 3
        mod_c = (y+1) % 3

        if mod_r == 0:
            list_mr = [x, x - 1, x - 2]
        elif mod_r == 1:
            list_mr = [x, x + 1, x + 2]
        else:
            list_mr = [x - 1, x, x + 1]

        if mod_c == 0:
            list_mc = [y, y - 1, y - 2]
        elif mod_c == 1:
            list_mc = [y, y + 1, y + 2]
        else:
            list_mc = [y - 1, y, y + 1]

        for i in list_mr:
            for j in list_mc:
                box_list.append(self.grid[i][j])

        return (row_list,coloum_list,box_list)
        
    def check_num(self,x,y,num):

        if self.grid[x][y] != 0:
            return False
        else:
            list_r, list_c, list_b = self.RCB_lists(x, y)

            if num in list_r:
                return False
            elif num in list_c:
                return False
            elif num in list_b:
                return False
            else:
                return True
            
    def check_grid(self):
        
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    return False
                else:
                    list_r, list_c, list_b = self.create_RCB_lists(x, y)

                    for num in range(1, 10):
                        if num not in list_r:
                            return False
                        if num not in list_c:
                            return False
                        if num not in list_b:
                            return False
            
        return True
    
    def empty_cell(self):

        for i in range(9):
            for j in range(9):

                if self.grid[i][j] == 0:
                    return (i,j)
                
        return None
    
    def is_valid(self): #will return True if sudoku is valid
        
        for i in range(9):
            for j in range(9):
                
                list_r,list_c,list_b = self.RCB_lists(i,j)

                for num in range(1,10):
                    count = 0
                    for x in range(9):
                        if list_r[x] == num:
                            count = count+1
                    
                    if count > 1:
                        return False
                    
                for num in range(1,10):
                    count = 0
                    for x in range(9):
                        if list_c[x] == num:
                            count = count+1
                    
                    if count > 1:
                        return False
                    
                for num in range(1,10):
                    count = 0
                    for x in range(9):
                        if list_b[x] == num:
                            count = count+1
                    
                    if count > 1:
                        return False

        return True            
        

    def solve(self):

        empty_loc = self.empty_cell()

        if not empty_loc:
            return True
        else:
            i,j = empty_loc

            for num in range(1,10):
                if self.check_num(i,j,num):
                    self.input_num(i,j,num)

                    if self.solve():
                        return True
                    
                    self.input_num(i,j,0)

            return False
