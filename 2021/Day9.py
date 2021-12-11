

def solve_part1(input):
    low_points = []

    if input[0] [0] <  input[0] [1] and input[0] [0] <  input[1] [0]:
        low_points.append(input[0] [0])

    if input[0] [-1] <  input[0] [-2] and input[0] [-1] <  input[1] [-1]:
        low_points.append(input[0] [-1])

    for idx in range (1,len(input[0])-1):
        if input[0] [idx] <  input[0] [idx+1] and input[0] [idx] <  input[0] [idx-1] and input[0] [idx] < input[1] [idx]:
            low_points.append(input[0] [idx])

    for key in list(input.keys())[1:-1]:
        if input[key] [0] <  input[key] [1] and input[key] [0] <  input[key+1] [0] and input[key] [0] <  input[key-1] [0]:
            low_points.append(input[key] [0])

        if input[key] [-1] <  input[key] [-2] and input[key] [-1] <  input[key+1] [-1] and input[key] [-1] <  input[key-1] [-1]:
            low_points.append(input[key] [-1])

        for idx in range(1,len(input[key])-1):
            if input[key] [idx] < input[key] [idx+1] and input[key] [idx] < input[key] [idx-1] and input[key] [idx] < input[key+1] [idx] and input[key] [idx] < input[key-1] [idx]:
                low_points.append(input[key] [idx])

    last = list(input.keys())[-1]
    if input[last] [0] <  input[last] [1] and input[last] [0] <  input[last-1] [0]:
        low_points.append(input[last] [0])

    if input[last] [-1] <  input[last] [-2] and input[last] [-1] <  input[last-1] [-1]:
        low_points.append(input[last] [-1])

    for idx in range(1,len(input[last])-1):
        if input[last] [idx] <  input[last] [idx+1] and input[last] [idx] <  input[last] [idx-1] and input[last] [idx] < input[last-1] [idx]:
            low_points.append(input[last] [idx])


    return sum([1+e for e in low_points])

# Recursively search basins
def search_basin(input,x,y,basin_coords = {}, pos = 0):
    try:
        basin_coords[(x,y)]

        return basin_coords
    except:
        if input[x][y] < 9:
            basin_coords[(x,y)] = input[x][y]
        else:
            return basin_coords

        if x - 1 >= 0:
            search_basin(input,x-1,y,basin_coords, pos + 1)
        
        if x + 1 < len(input):
            search_basin(input,x+1,y,basin_coords, pos + 1)

        if y - 1 >= 0:
            search_basin(input,x,y-1,basin_coords, pos + 1)
        
        if y + 1 < len(input[x]):
            search_basin(input,x,y+1,basin_coords, pos + 1)
        
        return basin_coords

def solve_part2(input):
    low_points = []
    basins = []
    if input[0] [0] <  input[0] [1] and input[0] [0] <  input[1] [0]:
        low_points.append(input[0] [0])
        basins.append(len(search_basin(input,0,0,{})))

    if input[0] [-1] <  input[0] [-2] and input[0] [-1] <  input[1] [-1]:
        low_points.append(input[0] [-1])
        basins.append(len(search_basin(input,0,len(input[0]) - 1,{})))

    for idx in range (1,len(input[0])-1):
        if input[0] [idx] <  input[0] [idx+1] and input[0] [idx] <  input[0] [idx-1] and input[0] [idx] < input[1] [idx]:
            low_points.append(input[0] [idx])
            basins.append(len(search_basin(input,0,idx,{})))

    for key in list(input.keys())[1:-1]:
        if input[key] [0] <  input[key] [1] and input[key] [0] <  input[key+1] [0] and input[key] [0] <  input[key-1] [0]:
            low_points.append(input[key] [0])
            basins.append(len(search_basin(input,key,0,{})))

        if input[key] [-1] <  input[key] [-2] and input[key] [-1] <  input[key+1] [-1] and input[key] [-1] <  input[key-1] [-1]:
            low_points.append(input[key] [-1])
            basins.append(len(search_basin(input,key,len(input[0]) - 1,{})))

        for idx in range(1,len(input[key])-1):
            if input[key] [idx] < input[key] [idx+1] and input[key] [idx] < input[key] [idx-1] and input[key] [idx] < input[key+1] [idx] and input[key] [idx] < input[key-1] [idx]:
                low_points.append(input[key] [idx])
                basins.append(len(search_basin(input,key,idx,{})))

    last = list(input.keys())[-1]
    if input[last] [0] <  input[last] [1] and input[last] [0] <  input[last-1] [0]:
        low_points.append(input[last] [0])
        basins.append(len(search_basin(input,last,0,{})))

    if input[last] [-1] <  input[last] [-2] and input[last] [-1] <  input[last-1] [-1]:
        low_points.append(input[last] [-1])
        basins.append(len(search_basin(input,last,len(input[0]) - 1),{}))

    for idx in range(1,len(input[last])-1):
        if input[last] [idx] <  input[last] [idx+1] and input[last] [idx] <  input[last] [idx-1] and input[last] [idx] < input[last-1] [idx]:
            low_points.append(input[last] [idx])
            basins.append(len(search_basin(input,last,idx,{})))

    return sorted(basins,reverse=True)[0:3]

input = {}
idx = 0
with open('Day9_input.txt','r') as inputfile:
    for line in inputfile:
        input[idx] = []
        for digit in line[:-1]:
            input[idx].append(int(digit))
        idx += 1

part1_sol = solve_part1(input)
print("Part 1 solution:", part1_sol)


input = {}
idx = 0
with open('Day9_input.txt','r') as inputfile:
    for line in inputfile:
        input[idx] = []
        for digit in line[:-1]:
            input[idx].append(int(digit))
        idx += 1


part2_sol = solve_part2(input)
part2_sol = part2_sol[0] * part2_sol[1] * part2_sol[2]
print("Part 2 solution:", part2_sol)