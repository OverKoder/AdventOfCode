def solve_part1():

    # Number of calories
    calories = 0

    max_calories = 0

    for line in open('Day1_input.txt','r',encoding='utf8'):

        # End of calories carried by the elf
        if not line == '\n':
            calories += int(line)
        
        else:

            if calories > max_calories:
                max_calories = calories

            calories = 0
    
    return max_calories

def solve_part2():

    # Number of calories
    calories = 0

    max_calories = [0,0,0]

    for line in open('Day1_input.txt','r',encoding='utf8'):

        # End of calories carried by the elf
        if not line == '\n':
            calories += int(line)
        
        else:

            # If this elf carries more calories than everyone, shift the top elves:
            if calories > max_calories[0]:

                max_calories[2] = max_calories[1]
                max_calories[1] = max_calories[0]
                max_calories[0] = calories
            
            # The elf carries more calories than the second and last, but not the first:
            elif calories > max_calories[1]:

                max_calories[2] = max_calories[1]
                max_calories[1] = calories

            # The elf carries more calories than the last, but not the first and second:
            elif calories > max_calories[2]:

                max_calories[2] = calories




            calories = 0
    
    return max_calories
def main():

    print("Part 1 solution = ", solve_part1())
    print("Part 2 solution = ", sum(solve_part2()))

if __name__ == "__main__":
    main()
