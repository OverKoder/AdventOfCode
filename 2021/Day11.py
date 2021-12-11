num_flash = 0

def extend_flash(grid, can_flash, x, y):
    global num_flash

    if x - 1 >= 0 and y - 1 >= 0 and can_flash[x - 1][y - 1]:
        grid[x - 1][y - 1] += 1

        if grid[x - 1][y - 1] > 9:
            num_flash += 1
            grid[x - 1][y - 1] = 0
            can_flash[x - 1][y - 1] = False
            extend_flash(grid,can_flash,x-1,y-1)


    if x - 1 >= 0 and can_flash[x - 1][y]:
        grid[x - 1][y] += 1

        if grid[x - 1][y] > 9:
            num_flash += 1
            grid[x - 1][y] = 0
            can_flash[x - 1][y] = False            
            extend_flash(grid,can_flash,x-1,y)                     

    if x - 1 >= 0 and y+1 < len(grid[x]) and can_flash[x - 1][y + 1]:
        grid[x - 1][y + 1] += 1

        if grid[x - 1][y + 1] > 9:

            grid[x - 1][y + 1] = 0         
            num_flash += 1
            can_flash[x- 1][y + 1] = False
            extend_flash(grid,can_flash,x-1,y+1)   

    if y - 1 >= 0 and can_flash[x][y - 1]:

        grid[x][y - 1] += 1

        if grid[x][y - 1] > 9:

            grid[x][y - 1] = 0
            num_flash += 1
            can_flash[x][y - 1] = False            
            extend_flash(grid,can_flash,x,y-1)

    if y - 1 >= 0 and x + 1 < len(grid[x]) and  can_flash[x + 1][y - 1]:
        grid[x + 1][y - 1] += 1

        if grid[x + 1][y - 1] > 9:

            grid[x + 1][y - 1] = 0
            num_flash += 1
            can_flash[x + 1][y - 1] = False
            extend_flash(grid,can_flash,x+1,y-1)

    if x + 1 < len(grid[x]) and can_flash[x + 1][y]:
        grid[x + 1][y] += 1

        if grid[x + 1][y] > 9:

            grid[x + 1][y] = 0
            num_flash += 1
            can_flash[x + 1][y] = False
            extend_flash(grid,can_flash,x+1,y)    

    if y + 1 < len(grid[x]) and can_flash[x][y + 1]:
        grid[x][y + 1] += 1

        if grid[x][y + 1] > 9:
            grid[x][y + 1] = 0
            num_flash += 1
            can_flash[x][y + 1] = False
            extend_flash(grid,can_flash,x,y + 1)    


    if x + 1 < len(grid[x]) and y + 1 < len(grid[x]) and can_flash[x + 1][y + 1]:
        grid[x + 1][y + 1] += 1

        if grid[x + 1][y + 1] > 9:
            grid[x + 1][y + 1] = 0
            num_flash += 1
            can_flash[x + 1][y + 1] = False
            extend_flash(grid,can_flash,x+1,y+1)
    
    return 

def solve_part1(grid, steps):
    global num_flash

    for step in range(steps):
        can_flash = [ [True for i in range(len(grid))] for j in range(len(grid))]
        for x in range(0, len(grid)):

            for y in range(0, len(grid[x])):
                
                if can_flash[x][y]:

                    grid[x][y] += 1

                    if grid[x][y] > 9:
                        num_flash += 1
                        grid[x][y] = 0
                        can_flash[x][y] = False
                        extend_flash(grid,can_flash,x,y)


    return num_flash

def solve_part2(grid):
    global num_flash
    step = 1
    while(True):

        can_flash = [ [True for i in range(len(grid))] for j in range(len(grid))]

        for x in range(0, len(grid)):

            for y in range(0, len(grid[x])):
                
                if can_flash[x][y]:

                    grid[x][y] += 1

                    if grid[x][y] > 9:
                        num_flash += 1
                        grid[x][y] = 0
                        can_flash[x][y] = False
                        extend_flash(grid,can_flash,x,y)

        if all(grid [x][y] == 0 for x in range(len(grid)) for y in range(len(grid))):
            return step

        step += 1




grid = []
with open("Day11_input.txt",'r') as inputfile:
    for line in inputfile:
        grid.append( [int(digit) for digit in line[:-1] ] )

part1_sol = solve_part1(grid, 100)
print("Part 1 sol:", part1_sol)



grid = []
with open("Day11_input.txt",'r') as inputfile:
    for line in inputfile:
        grid.append( [int(digit) for digit in line[:-1] ] )

part2_sol = solve_part2(grid)
print("Part 2 sol:", part2_sol)