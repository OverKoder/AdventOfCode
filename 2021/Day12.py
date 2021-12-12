def is_feasible_part1(cave_map, path, cave):
    # Condition to expand the path 
    if cave.isupper():
        return True
    else:
        return cave not in path


def is_complete_part1(cave_map, path,paths):

    # If we got the end or not
    if path[-1] == "end":
        paths.append(path)
        return True
    
    return False


def solve_part1(cave_map, path,paths):
    
    for cave in cave_map[ path[-1] ]:

        if is_complete_part1(cave_map,path,paths):
            return paths

        if is_feasible_part1(cave_map,path,cave):
            paths = solve_part1(cave_map, path + [cave],paths)
        


    return paths


def is_feasible_part2(cave_map, path, cave):
    
    # Condition to expand the path 
    if cave.isupper():
        return True
    else:

        if cave == 'start' and cave in path:
            return False

        if cave not in path:
            return True

        aux = path + [cave]
        # Small caves can be visited twice (but only one)
        lower = list( {}.fromkeys([c for c in aux if c.islower()]).keys() )

        aux = [c for c in [aux.count(elem) for elem in lower] if c >= 2]
        return len(aux) == 1 and aux[0] <= 2


def is_complete_part2(cave_map, path,paths):
    # If we got the end or not (same as part 1)
    if path[-1] == "end":
        paths.append(path)
        return True
    
    return False

def solve_part2(cave_map, path,paths):
    
    for cave in cave_map[ path[-1] ]:

        if is_complete_part2(cave_map,path,paths):
            return paths

        if is_feasible_part2(cave_map,path,cave):
            paths = solve_part2(cave_map, path + [cave],paths)
        


    return paths


# Get input
paths = []
cave_map = {}
with open("Day12_input.txt",'r') as inputfile:
    for line in inputfile:
        line = line.split("-")
        if line[0] not in cave_map:
            cave_map[ line[0] ] = [line[1] [:-1]]
        else:
            cave_map[ line[0] ].append(line[1][:-1])
        
        if line[1] [:-1] not in cave_map:
            cave_map[ line[1] [:-1] ] = [ line[0] ]
        else:
            cave_map[ line[1] [:-1] ].append(line[0])

# Solved with recursively with backtracking, although it takes some time to execute...
part1_sol = solve_part1(cave_map,["start"],paths)
print("Part 1 solution:", len(part1_sol))

paths = []
part2_sol = solve_part2(cave_map,["start"],paths)
print("Part 2 solution:", len(part2_sol))