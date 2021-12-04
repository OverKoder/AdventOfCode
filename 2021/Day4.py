
def solve_part1(numbers, boards):
    marked = {}.fromkeys(list(boards.keys()))

    for key in marked:  
                       # idx // 5   idx % 5
                       # row        column
        marked[key] = ([0,0,0,0,0],[0,0,0,0,0])


    for number in numbers:

        for board_idx in boards:
            
            try:
                idx = boards[board_idx].index(number)

                # Update rows e.g: (marked[idx] [0] [1]) represents row 1 of board idx
                marked[board_idx] [0] [idx // 5] += 1

                # Update columns e.g: (marked[idx] [1] [2]) represents column 2 of board idx
                marked[board_idx] [1] [idx % 5] += 1

                # Full marked row or column (when there is a 5 in any row or column)
                if 5 in marked[board_idx] [0] or 5 in marked[board_idx] [1]:
                    # This return means: sum each number in the board that is not in the numbers that have been drawn up until now
                    res = sum([n for n in boards[board_idx] if n not in numbers[0: numbers.index(number) + 1]])

                    # Here i return the solution and some parameters that will be useful in part2
                    # Solution,                  current number
                    return res * number, numbers, number,        marked, boards, board_idx
                



            except:
                # Number not in board
                pass




def solve_part2(numbers,number,marked,boards, board_idx):

    # Here we finish what is left of the last iteration from solve_part1()
    completed_boards_list = [0] * len(boards)
    completed_boards_list [board_idx] = 1
    completed_boards = 1
    for board_idx in range(board_idx + 1, len(boards)):
        try:
            idx = boards[board_idx].index(number)

            # Update rows e.g: (marked[idx] [0] [1]) represents row 1 of board idx
            marked[board_idx] [0] [idx // 5] += 1

            # Update columns e.g: (marked[idx] [1] [2]) represents column 2 of board idx
            marked[board_idx] [1] [idx % 5] += 1

            if (5 in marked[board_idx] [0] or 5 in marked[board_idx] [1]) and completed_boards_list[board_idx] == 0:
                    completed_boards_list [board_idx] = 1
                    completed_boards += 1
                
            if completed_boards == len(boards) - 1:
                last = completed_boards_list.index(0)

            elif completed_boards  == len(boards):
                return sum([n for n in boards[last] if n not in numbers[0: numbers.index(number) + 1]]) * number

        except:
            # Number not in board
            pass

    
    for number in numbers[numbers.index(number) + 1:]:

        for board_idx in boards:
            
            try:
                idx = boards[board_idx].index(number)

                # Update rows e.g: (marked[idx] [0] [1]) represents row 1 of board idx
                marked[board_idx] [0] [idx // 5] += 1

                # Update columns e.g: (marked[idx] [1] [2]) represents column 2 of board idx
                marked[board_idx] [1] [idx % 5] += 1

                
                if (5 in marked[board_idx] [0] or 5 in marked[board_idx] [1]) and completed_boards_list[board_idx] == 0:
                    completed_boards_list [board_idx] = 1
                    completed_boards += 1
                
                # If there's only 1 left to win
                if completed_boards == len(boards) - 1:
                    last = completed_boards_list.index(0)
                
                elif completed_boards  == len(boards):
                    return sum([n for n in boards[last] if n not in numbers[0: numbers.index(number) + 1]]) * number
            
            except:
                # Number not in board
                pass


"""
Coder's note: Sometimes is harder to prepare the input than solving the problem...
"""

# Get input for part 1
input_file = open('Day4_input.txt','r')

# Numbers for bingo
numbers = input_file.readline().split(',')

# Last number has a "\n" character attached to it, we eliminate it
numbers[-1] = numbers[-1][:-1]

numbers = [int(num) for num in numbers]
# Skip next "\n" in file
input_file.readline()

boards = {}
board_idx = 0

aux = input_file.read().split("\n")
# Split leaves '' characters, we must filter them
aux = [elem for elem in aux if elem != '']

for i in range(len(aux)//5):
    boards[board_idx] = aux[5*i] + " " + aux[5*i+1] + " " + aux[5*i + 2] + " " + aux[5*i + 3] + " " + aux[5*i + 4] 
    boards[board_idx] = boards[board_idx].split()
    boards[board_idx] = [int(num) for num in boards[board_idx]]
    board_idx +=1

del aux, board_idx

# We return this many variable to take advantage of what we have already calculated
part1_sol, numbers, number, marked, boards, board_idx = solve_part1(numbers, boards)
print("Part 1 solution:",part1_sol)

part2_sol = solve_part2(numbers,number,marked,boards, board_idx)
print("Part 2 solution:",part2_sol)

