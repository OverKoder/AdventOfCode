def solve_part1(window_size: int = 4) -> int:

    input = open('Day6_input.txt','r',encoding="utf8").readlines() [0] [:-1]

    idx = 0

    while idx + window_size < len(input):

        # Dictionary of key: char, value: int (the index in the substring)
        visited_characters = {}

        for i in range(0, window_size):
            

            # If the current character in the window exists already in the substring, skip
            # an amount of position equal to the distance to the beginning of the substring
            try:

                # Check if character is already on substring
                visited_characters[input[idx + i]]
                idx += visited_characters[input[idx + i]]
                break

            except:
                
                # Add to visited characters
                visited_characters[input[idx + i]] = i + 1
        
        if len(visited_characters.keys()) == window_size:
            return idx + window_size


    return -1

def solve_part2(window_size: int = 14) -> int:
    # Same problem as before, but with larger window size
    input = open('Day6_input.txt','r',encoding="utf8").readlines() [0] [:-1]

    idx = 0

    while idx + window_size < len(input):
        
        # Dictionary of key: char, value: int (the index in the substring)
        visited_characters = {}

        for i in range(0, window_size):
            

            # If the current character in the window exists already in the substring, skip
            # an amount of position equal to the distance to the beginning of the substring
            try:

                # Check if character is already on substring
                visited_characters[input[idx + i]]
                idx += visited_characters[input[idx + i]]
                break

            except:
                
                # Add to visited characters
                visited_characters[input[idx + i]] = i + 1
        
        if len(visited_characters.keys()) == window_size:
            return idx + window_size


    return -1

def main():

    print("Part 1 solution = ", solve_part1(window_size=4))

    print("Part 2 solution = ", solve_part2(window_size=14))

    return

if __name__ == "__main__":
    main()