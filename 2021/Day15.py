from copy import deepcopy as deepcopy

def solve_part1(mat):
    back = [0] * len(mat[0])
    front = [0] * len(mat[0])

    for i in range(1,len(mat)):

        front[i] = front[i-1] + mat[i] [0]

    for col in range(1,len(mat)):

        back,front = front,back
        front[0] = back[0] + mat[0] [col]

        for row in range(1,len(mat)):
            front[row] = min(mat[row][col] + front[row-1], mat[row][col] + back[row] )

    return front[-2]

mat = {}
idx = 0
with open("Day15_input.txt",'r') as inputfile:
    input = inputfile.read().split("\n") [:-1]

for idx in range(len(input)):
    mat[idx] = [int(e) for e in input[idx]]




original = deepcopy(mat)

for i in range(len(mat)):
    for exp in range(1,5):
        aux = []

        for e in original[i]:
            if e + exp <= 9:
                aux.append(e + exp)
            else:
                aux.append(e+exp-9)

        mat[i] = mat[i] + aux

original = deepcopy(mat)
for exp in range(1,5):
    aux = deepcopy(mat)
    for idx in range(len(original)):
        mat[exp*(len(original) - 1) + idx + exp] = aux[idx] 
    del aux

for exp in range(1,5):

    for i in range(len(mat[0])):

        for idx in range(exp*(len(original) - 1) + exp, exp*(len(original) - 1) + exp + len(original)):
            if original[idx % len(original)] [i % len(original[0])] + exp <= 9:
                mat[idx] [i] = original[idx % len(original)] [i % len(original[0])] + exp
            else:
                mat[idx] [i] = original[idx % len(original)] [i % len(original[0])] + exp - 9

del original
mat[0] [0] = 0
part1_sol = solve_part1(mat)
print("Part 1 sol:", part1_sol)

