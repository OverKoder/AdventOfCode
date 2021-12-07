def solve_part1(input,max_pos):

    min_pos = 0
    min_fuel = 2**31

    for pos in range(max_pos):
        fuel_count = 0

        # Count how much fuel to align to position pos
        for crab_pos in range(len(input)):
            fuel_count += abs(input[crab_pos] - pos)

        if fuel_count < min_fuel:
            min_pos = pos
            min_fuel = fuel_count
    
    return min_pos, min_fuel

def solve_part2(input,max_pos):
    min_pos = 0
    min_fuel = 2**31

    for pos in range(max_pos):
        fuel_count = 0

        # Count how much fuel to align to position pos
        for crab_pos in range(len(input)):
            n = abs(input[crab_pos] - pos)
            # Each fuel position cost 1 more fuel than the last, the total sum is the sum of the 
            # (input[crab_pos] - pos) natural numbers => (n^2 + n) // 2
            fuel_count += (n*n + n ) // 2

        if fuel_count < min_fuel:
            min_pos = pos
            min_fuel = fuel_count
    
    return min_pos, min_fuel    






with open('Day7_input.txt','r') as inputfile:
    input = inputfile.read().split(",")

input = [int(element) for element in input]
max_pos = max(input)

pos, fuel = solve_part1(input,max_pos)
print("Part 1: Position: ", pos , "Fuel: ", fuel)

pos, fuel = solve_part2(input,max_pos)
print("Part 2: Position: ", pos , "Fuel: ", fuel)

