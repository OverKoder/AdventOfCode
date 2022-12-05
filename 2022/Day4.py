def solve_part1():

    with open('Day4_input.txt', 'r', encoding = 'utf8') as input:

        contained = 0
        for line in input:

            left_section, right_section = line.split(',')
            left_section_lower, left_section_higher = [int(elem) for elem in left_section.split('-')]
            right_section_lower, right_section_higher = [int(elem) for elem in right_section.split('-')]

            # Left section is contained in right section OR right section is contained in left section
            if ((left_section_lower >= right_section_lower and left_section_higher <= right_section_higher) or
                (right_section_lower >= left_section_lower and right_section_higher <= left_section_higher)):

                contained += 1

    return contained

def solve_part2():

    with open('Day4_input.txt', 'r', encoding = 'utf8') as input:

        overlapped = 0
        for line in input:

            left_section, right_section = line.split(',')
            left_section_lower, left_section_higher = [int(elem) for elem in left_section.split('-')]
            right_section_lower, right_section_higher = [int(elem) for elem in right_section.split('-')]

            # Left section overlaps right section or right section overlaps left section
            if ((left_section_lower <= right_section_lower and left_section_higher >= right_section_lower) or
                (right_section_lower <= left_section_lower and right_section_higher >= left_section_lower)):

                overlapped += 1

    return overlapped

def main():

    print("Part 1 solution = ", solve_part1())
    print("Part 2 solution = ", solve_part2())

if __name__ == "__main__":
    main()