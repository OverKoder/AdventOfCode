def solve_part1(depth_list):

    increase = 0
    for i in range(1, len(depth_list)):
        # Check if depth increases
        if depth_list[i-1] < depth_list[i]:
            increase += 1
    
    return increase

def solve_part2(depth_list):
    """
    Here we take advantage that sums overlap, and thus, to calculate the next sum of numbers, we can
    use the previous sum substracting the number that is no longer part of the new sum and adding the next number in the list

    For example:
    1.- 199 + 200 + 208 = sum
    2.- 200 + 208 + 210 = ???

    ??? can be calculated as sum - 199 + 210, and thus, needing only 2 operations, not 3.
    """
    increase = 0
    prev_sum = sum(depth_list[0:3])
    for i in range(1, len(depth_list) - 2):
        # Calculate sum
        current_sum = prev_sum - depth_list[i-1] + depth_list[i+2]
        if prev_sum < current_sum:
            increase += 1
        prev_sum = current_sum

    
    return increase

# Get day 1 input (part 1)
with open('Day1_input_part1.txt','r') as input_file:
    input = input_file.read()

input = input.split()
# Convert to int
input = [int(element) for element in input]

part1_sol = solve_part1(input)
print("Part 1 solution:", part1_sol)



# Get day 1 input (part 2)
with open('Day1_input_part2.txt','r') as input_file:
    input = input_file.read()

input = input.split()
# Convert to int
input = [int(element) for element in input]

part2_sol = solve_part2(input)
print("Part 2 solution:", part2_sol)
