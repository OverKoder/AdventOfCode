def solve_part1():
    
    # Read input
    input = open("Day5_input.txt",'r',encoding='utf8')

    input = input.readlines()

    i = 0
    while (input[i] != "\n"):
        i += 1
    
    # Each column is represented as stack
    stack_dict = {key:[] for key in [int(elem) for elem in input[i - 1].split()]}

    # Initialize stacks
    for j in range(i - 2, -1, -1):
        
        # Get row of crate j
        crate = input[j]
        idx = 1
        for stack in stack_dict:
            
            # If there is a crate
            if crate[idx] != ' ':
                stack_dict[stack].append(crate[idx])

            idx += 4

    # Get actions
    input = input[i + 1:]

    for action in input:

        # Get number of blocks, source and destination
        _, n_blocks, _, source, _, dest = action.split()

        # Convert to int >:(
        n_blocks, source, dest = int(n_blocks), int(source), int(dest)

        cargo = []
        while n_blocks > 0:
            
            # Pop the top crate and add it to the cargo as a LIFO order.
            cargo.append(stack_dict[source].pop())

            n_blocks -= 1

        # Move it to destination
        stack_dict[dest].extend(cargo)
    
    solution = ''
    for stack in stack_dict:

        solution += stack_dict[stack][-1]
    
    return solution

def solve_part2():
    
    # Read input
    input = open("Day5_input.txt",'r',encoding='utf8')

    input = input.readlines()

    i = 0
    while (input[i] != "\n"):
        i += 1
    
    # Each column is represented as stack
    stack_dict = {key:[] for key in [int(elem) for elem in input[i - 1].split()]}

    # Initialize stacks
    for j in range(i - 2, -1, -1):
        
        # Get row of crate j
        crate = input[j]
        idx = 1
        for stack in stack_dict:
            
            # If there is a crate
            if crate[idx] != ' ':
                stack_dict[stack].append(crate[idx])

            idx += 4

    # Get actions
    input = input[i + 1:]

    for action in input:

        # Get number of blocks, source and destination
        _, n_blocks, _, source, _, dest = action.split()

        # Convert to int >:(
        n_blocks, source, dest = int(n_blocks), int(source), int(dest)
        
        cargo = []
        while n_blocks > 0:
            
            # Pop the top crate and add it to the cargo, but now, we add each element as the first one (FIFO Order)
            # This is the only that changes from both functions
            cargo.insert(0, stack_dict[source].pop())

            n_blocks -= 1

        # Move it to destination
        stack_dict[dest].extend(cargo)
    
    solution = ''
    for stack in stack_dict:

        solution += stack_dict[stack][-1]
    
    return solution
def main():
    """
    This problem in particular was exceptionally well thought, it
    is a great problem for beginner programmers (not me though :) ) who are getting to
    know stacks and queues!
    """
    # Solved with stacks
    print("Part 1 solution = ", solve_part1())

    # Solved with queues
    print("Part 2 solution = ", solve_part2())
if __name__ == "__main__":
    main()