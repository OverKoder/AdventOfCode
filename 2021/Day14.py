def solve(polymer, rules,values,steps = 10):

    for step in range(steps):
        new_polymer={}

        # Efficiently this can be done with the idea that we do not need to keep the order,
        # we just need to represent that if NN -> C then #NN == #NC and #NN == #CN
        for key in polymer:
            value = polymer[key]
            try:
                values[rules[key]] += value
            except:
                values[rules[key]] = value

            try:
                new_polymer [key[0] + rules[key]] += value
            except:
                new_polymer [key[0] + rules[key]] = value
            try:
                new_polymer [rules[key] + key[1]] += value
            except:
                new_polymer [rules[key] + key[1]] = value



        polymer = new_polymer
    
    return max(values.values()) - min(values.values())




polymer = "SCSCSKKVVBKVFKSCCSOV"
values = {key: polymer.count(key) for key in set(polymer) }
polymer_dict = {}
for i in range(len(polymer)-1):
    try:
        polymer_dict[polymer[i:i+2]] += 1
    except:
        polymer_dict[polymer[i:i+2]] = 1

rules = {}
with open("Day14_input.txt",'r') as inputfile:
    for line in inputfile:
        line = line.split(" -> ")
        rules[line[0]] = line[1] [:-1]


part1_sol = solve(polymer_dict,rules,values)
print("Part 1 solution: ", part1_sol)


polymer = "SCSCSKKVVBKVFKSCCSOV"
values = {key: polymer.count(key) for key in set(polymer) }
polymer_dict = {}
for i in range(len(polymer)-1):
    try:
        polymer_dict[polymer[i:i+2]] += 1
    except:
        polymer_dict[polymer[i:i+2]] = 1

part2_sol = solve(polymer_dict,rules,values,steps=40)
print("Part 2 solution: ", part2_sol)