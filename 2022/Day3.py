def solve_part1():

    priority_sum = 0

    for line in open('Day3_input.txt','r',encoding='utf8'):
        
        # Split rucksack
        left, right = set(line[:len(line) // 2]), set(line[len(line) // 2:])

        # Find common item
        common_item = left.intersection(right).pop()

        if common_item.islower():

            # Convert to ascii and substract to get value
            priority_sum += ord(common_item) - 96

        else:

            # Convert to ascii and substract to get value
            priority_sum += ord(common_item) - 38



    return priority_sum

def solve_part2():

    priority_sum = 0

    file = open('Day3_input.txt','r',encoding='utf8')
    
    # Get all input
    input = file.readlines()

    # Split rucksack
    for i in range(0, len(input), 3):

        first, second, third = set(input[i][:-1]), set(input[i + 1][:-1]), set(input[i + 2][:-1])

        # Find common item
        common_item = set.intersection(first, second, third).pop()

        if common_item.islower():

            # Convert to ascii and substract to get value
            priority_sum += ord(common_item) - 96

        else:

            # Convert to ascii and substract to get value
            priority_sum += ord(common_item) - 38



    return priority_sum
def main():

    print("Part 1 solution:", solve_part1())
    print("Part 2 solution:", solve_part2())

    return

if __name__ == "__main__":
    main()