def solve_part1(input):

    unique_lengths = {2:0, 3:0, 4:0, 7:0}
    for key in input:
        
        for output in input[key]:
            try:
                unique_lengths[len(output)] += 1
            except:
                pass
    
    return sum([unique_lengths[idx] for idx in unique_lengths])



input = {}
idx = 0
with open('Day8_input.txt','r') as inputfile:
    
    for line in inputfile:
        input[idx] = line[line.index("|") + 1:].split()
        idx+=1



part1_sol = solve_part1(input)
print("Part 1 solution:", part1_sol)

