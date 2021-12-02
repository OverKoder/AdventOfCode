def solve_part1(input):
    horizontal = 0
    depth = 0

    with open(input, 'r') as file:

        # We just check the first letter, no need to check a prefix or the entire line
        for line in file:

            # Forward
            if line [0] == 'f':

                # Since there is a "\n" character at the end, we check this position not -1
                horizontal += int(line[-2])

            # Up
            elif line[0] == 'u':
                depth -= int(line[-2])

            # Down
            else:
                depth += int(line[-2])
    
    return horizontal * depth

def solve_part2(input):
    horizontal = 0
    depth = 0
    aim = 0

    with open(input, 'r') as file:

        # We just check the first letter, no need to check a prefix or the entire line
        for line in file:
            
            # Forward
            if line [0] == 'f':
                horizontal += int(line[-2])
                depth += aim * int(line[-2])

            # Up    
            elif line[0] == 'u':
                aim -= int(line[-2])
            
            # Down
            else:
                aim += int(line[-2])
    
    return horizontal * depth

# Get part 1 input
input_file ='Day2_input_part1.txt'
sol_part1 = solve_part1(input = input_file)
print("Part 1 solution:", sol_part1)

# Get part 2 input
input_file ='Day2_input_part2.txt'
sol_part2 = solve_part2(input = input_file)
print("Part 2 solution:", sol_part2)