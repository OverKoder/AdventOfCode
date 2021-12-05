def prepare(input, equal = False):

    coords_pair = {}
    idx = 0
    for coords in input:
        aux = coords.split(" -> ")
        start = aux[0].split(',')
        end = aux[1].split(',')
        # In part 1 we only need to consider the coordinates x1,y1 and x2,y2 where x1 = x2 or y1 = y2
        if equal and ( start[0] == end[0] or start[1] == end[1]):
            coords_pair[idx] = [int (e) for e in start] + [int (e) for e in end]
            idx += 1
        elif not equal:
            coords_pair[idx] = [int (e) for e in start] + [int (e) for e in end]
            idx += 1

    return coords_pair


    

def solve_part1(input):
    diagram = {}.fromkeys([(x,y) for x in range(1000) for y in range(1000)],0)

    for coord in input:

        coord = input[coord]
        # Same x component
        if coord[0] == coord[2]:

            if coord[1] <= coord[3]:

                for i in range(coord[1],coord[3] + 1):
                    diagram[coord[0],i] += 1
            
            else:

                for i in range(coord[1],coord[3] - 1, -1):
                    diagram[coord[0],i] += 1


        # Same y component
        if coord[1] == coord[3]:

            if coord[0] <= coord[2]:

                for i in range(coord[0],coord[2] + 1):
                    diagram[i,coord[1]] += 1
            
            else:

                for i in range(coord[0],coord[2] - 1, -1):
                    diagram[i,coord[1]] += 1

    # Sum every point that is crossed by 2 or more lines
    return sum([1 for key in diagram if diagram[key] >= 2])



def solve_part2(input):
    diagram = {}.fromkeys([(x,y) for x in range(1000) for y in range(1000)],0)

    for coord in input:

        coord = input[coord]

        # Same x component
        if coord[0] == coord[2]:

            if coord[1] <= coord[3]:

                for i in range(coord[1],coord[3] + 1):
                    diagram[coord[0],i] += 1
            
            else:

                for i in range(coord[1],coord[3] - 1, -1):
                    diagram[coord[0],i] += 1


        # Same y component
        elif coord[1] == coord[3]:

            if coord[0] <= coord[2]:

                for i in range(coord[0],coord[2] + 1):
                    diagram[i,coord[1]] += 1
            
            else:

                for i in range(coord[0],coord[2] - 1, -1):
                    diagram[i,coord[1]] += 1

        elif coord[0] > coord[2]:

            if coord[1] <= coord[3]:
                diag = 0
                for i in range(coord[1],coord[3] + 1):
                    diagram[coord[0] - diag, i] += 1
                    diag += 1
            
            else:
                diag = 0
                for i in range(coord[1],coord[3] - 1, -1):
                    diagram[coord[0] - diag ,i] += 1
                    diag += 1

        elif coord[0] < coord[2]:

            if coord[1] <= coord[3]:
                diag = 0
                for i in range(coord[1],coord[3] + 1):
                    diagram[coord[0] + diag, i] += 1
                    diag += 1
            
            else:
                diag = 0
                for i in range(coord[1],coord[3] - 1, -1):
                    diagram[coord[0] + diag ,i] += 1
                    diag += 1

        elif coord[1] > coord[3]:

            if coord[0] <= coord[2]:
                diag = 0
                for i in range(coord[0],coord[2] + 1):
                    diagram[i,coord[1] - diag] += 1
                    diag += 1
            
            else:
                diag = 0
                for i in range(coord[0],coord[2] - 1, -1):
                    diagram[i,coord[1] - diag] += 1
                    diag += 1

        elif coord[1] < coord[3]:

            if coord[0] <= coord[2]:
                diag = 0
                for i in range(coord[0],coord[2] + 1):
                    diagram[i,coord[1] - diag] += 1
                    diag += 1
            
            else:
                diag = 0
                for i in range(coord[0],coord[2] - 1, -1):
                    diagram[i,coord[1] - diag] += 1
                    diag += 1



    # Sum every point that is crossed by 2 or more lines
    return sum([1 for key in diagram if diagram[key] >= 2])

# Get input
with open('Day5_input.txt', 'r') as input_file:
    input = input_file.read().split("\n")
    del input [-1]

input = prepare(input, equal=True)
part1_sol = solve_part1(input)
print("Part 1 solution: ",part1_sol)

# Get input (again)
with open('Day5_input.txt', 'r') as input_file:
    input = input_file.read().split("\n")
    del input [-1]

input = prepare(input, equal=False)
part2_sol = solve_part2(input)
print("Part 2 solution: ",part2_sol)