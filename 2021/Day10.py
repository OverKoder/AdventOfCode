def solve_part1():
    syntax_dic = {
        ")": "(", 
        "]": "[",
        "}": "{", 
        ">": "<",
    }
    scores = {
        ")":3,
        "]":57,
        "}":1197,
        ">":25137
    }

    stack = []
    score = 0

    with open('Day10_input.txt','r') as inputfile:


        for line in inputfile:

            # Remove "\n"
            line = line[:-1]

            for char in line:
                
                if char in syntax_dic.values():
                    stack.append(char)
                else:
                    if syntax_dic[char] != stack.pop():
                        score += scores[char]
                        break

                        
                  

    
    return score


def solve_part2():
    syntax_dic = {
        ")": "(", 
        "]": "[",
        "}": "{", 
        ">": "<",
    }

    repair_dic = {
        "(": ")", 
        "[": "]",
        "{": "}", 
        "<": ">",
    }

    scores = {
        ")":1,
        "]":2,
        "}":3,
        ">":4
    }

    score_list= []

    with open('Day10_input.txt','r') as inputfile:


        for line in inputfile:

            # Remove "\n"
            line = line[:-1]

            score = 0
            stack = []
            incomplete = True

            for char in line:
                
                if char in syntax_dic.values():
                    stack.append(char)
                else:
                    if syntax_dic[char] != stack.pop():
                        incomplete = False
                        break

            if incomplete:
                stack.reverse()
                for incomplete in stack:
                    score = score * 5 + scores[repair_dic[incomplete]]
                
                
                score_list.append(score)
            

    
    return sorted(score_list) [len(score_list) // 2]



part1_sol = solve_part1()
print("Part 1 sol: ", part1_sol)

part2_sol = solve_part2()
print("Part 2 sol: ", part2_sol)