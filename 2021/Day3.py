def get_part2_input():

    with open('Day3_input_part2.txt','r') as input_file:
        input = input_file.read().split("\n")

    # There is a "\n" at the end that gives problems, we simply delete it
    del input[-1]
    return input

def solve_part1(input_file):

    with open(input_file,'r') as input:
        
        # Dictionary used to count how many bits appear in each position, we add 1 if we see a zero or add -1 if we see a one
        bits = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}

        for line in input:

            bits[0] += 1 if line[11] == '0' else -1
            bits[1] += 1 if line[10] == '0' else -1
            bits[2] += 1 if line[9] == '0' else -1
            bits[3] += 1 if line[8] == '0' else -1
            bits[4] += 1 if line[7] == '0' else -1
            bits[5] += 1 if line[6] == '0' else -1
            bits[6] += 1 if line[5] == '0' else -1
            bits[7] += 1 if line[4] == '0' else -1
            bits[8] += 1 if line[3] == '0' else -1
            bits[9] += 1 if line[2] == '0' else -1
            bits[10] += 1 if line[1] == '0' else -1
            bits[11] += 1 if line[0] == '0' else -1


    gamma_rate = 0
    epsilon_rate = 0

    # Get decimal value from binary
    for idx in range(11,-1,-1):

        if bits[idx] > 0:
            gamma_rate += 2**idx 
        else:
            epsilon_rate += 2**idx 

    return gamma_rate * epsilon_rate

def solve_part2(input):

    # Two lists, one for the numbers with more zeros, the other one for those that have more ones
    life_support = {0: [], 1:[]}

    # Oxygen generator rating
    bit_idx = 0
    while bit_idx <= 11:

        for line in input:

            if line[bit_idx] == '0':
                life_support[0].append(line)
            else:
                life_support[1].append(line)
        
        if len(life_support[0]) > len(life_support[1]):
            input = life_support[0]
        else:
            input = life_support[1]

        # If there is only 1 binary number, we stop
        if len(input) == 1:
            break

        life_support = {0: [], 1:[]}
        bit_idx += 1

    # Reverse the string to get decimal value from binary
    oxygen_rating = input[0] [::-1]
    oxygen = 0
    for idx in range(11,-1,-1):
        if oxygen_rating[idx] == '1':
            oxygen += 2**idx 

    # We don't need this variable anymore
    del oxygen_rating



    # Reset input
    input = get_part2_input()

    # CO2 scrubber, same loop, but with a different condition
    bit_idx = 0
    while bit_idx <= 11:

        for line in input:

            if line[bit_idx] == '0':
                life_support[0].append(line)
            else:
                life_support[1].append(line)
        
        # This condition changes
        if len(life_support[0]) <= len(life_support[1]):
            input = life_support[0]
        else:
            input = life_support[1]

        # If there is only 1 binary number, we stop
        if len(input) == 1:
            break

        life_support = {0: [], 1:[]}
        bit_idx += 1
    
    # Reverse the string to get decimal value from binary
    co2_scrubber = input[0] [::-1]

    co2 = 0
    for idx in range(11,-1,-1):
        if co2_scrubber[idx] == '1':
            co2 += 2**idx 

    return oxygen * co2


# Get input for part 1
input = 'Day3_input_part1.txt'
part1_sol = solve_part1(input_file= input)
print("Part 1 solution:", part1_sol)

# Get input for part 2
input = get_part2_input()
part2_sol = solve_part2(input)
print("Part 2 solution:", part2_sol)