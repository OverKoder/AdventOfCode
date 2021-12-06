def solve(input, days):
    # Lanternfish with internal timer t are the number of lanternfish with timer t+1 after a day
    for day in range(days):
        aux = input[0]
        input[0] = input[1]
        input[1] = input[2]
        input[2] = input[3]
        input[3] = input[4]
        input[4] = input[5]
        input[5] = input[6]

        # Lantern fish with interal timer 0 replicate, but they have to be added to those lanternfish that have 
        # a timer equal to 7
        input[6] = input[7] + aux

        
        input[7] = input[8]
        input[8] = aux
    
    return sum([input[key] for key in input])

# Get input and transform to my chosen data structure
with open('Day6_input.txt','r') as inputfile:
    input = inputfile.read().split(",")

input = [int(element) for element in input]

# Lanterfish dictionary where the key represents their internal timer, and the value how many lanternfish
# with that internal timer are alive right now
input = {
    0: input.count(0),
    1: input.count(1),
    2: input.count(2),
    3: input.count(3),
    4: input.count(4),
    5: input.count(5),
    6: input.count(6),
    7: input.count(7),
    8: input.count(8)
}
part1_sol = solve(input,80)
print("Part 1 solution: ",part1_sol)

# 80 days have already been calculated, we take advantage of it
part2_sol = solve(input,256 - 80)
print("Part 2 solution: ",part2_sol)