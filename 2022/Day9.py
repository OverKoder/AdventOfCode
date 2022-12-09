def solve_part1():

    with open('Day9_input.txt','r',encoding='utf8') as input:

        # Initially, both head and tail are in the same spot
        head_x, head_y, tail_x, tail_y = 0, 0, 0, 0

        visitedPositions = {}
        for line in input:

            direction, n_moves = line.split()
            n_moves = int(n_moves)

            # Up
            if direction == 'U':
                
                for i in range(n_moves):

                    head_y += 1

                    # If the head is farther up that the tail, move the tail
                    if head_y > tail_y + 1:
                        
                        # If head and tail are at the same length
                        if head_x == tail_x:

                            tail_y += 1

                        # Move diagonally
                        else:

                            tail_x += (head_x - tail_x)
                            tail_y += 1
                    
                    # Check if the tail has already been on that position
                    try:
                        visitedPositions[(tail_x, tail_y)]
                    
                    except:
                        visitedPositions[(tail_x, tail_y)] = True
                    
            # Down
            elif direction == 'D':

                for i in range(n_moves):

                    head_y -= 1

                    # If the head is farther down that the tail, move the tail
                    if head_y < tail_y - 1:
                        
                        # If head and tail are at the same length
                        if head_x == tail_x:

                            tail_y -= 1

                        # Move diagonally
                        else:

                            tail_x += (head_x - tail_x)
                            tail_y -= 1

                    # Check if the tail has already been on that position
                    try:
                        visitedPositions[(tail_x, tail_y)]
                    
                    except:
                        visitedPositions[(tail_x, tail_y)] = True
            
            # Left
            elif direction == 'L':

                for i in range(n_moves):

                    head_x -= 1

                    # If the head is farther left that the tail, move the tail
                    if head_x < tail_x - 1:
                        
                        # If head and tail are at the same height
                        if head_y == tail_y:

                            tail_x -= 1

                        # Move diagonally
                        else:

                            tail_y += (head_y - tail_y)
                            tail_x -= 1

                    # Check if the tail has already been on that position
                    try:
                        visitedPositions[(tail_x, tail_y)]
                    
                    except:
                        visitedPositions[(tail_x, tail_y)] = True

            # Right
            else:

                for i in range(n_moves):

                    head_x += 1

                    # If the head is farther right that the tail, move the tail
                    if head_x > tail_x + 1:
                        
                        # If head and tail are at the same height
                        if head_y == tail_y:

                            tail_x += 1

                        # Move diagonally
                        else:

                            tail_y += (head_y - tail_y)
                            tail_x += 1

                    # Check if the tail has already been on that position
                    try:
                        visitedPositions[(tail_x, tail_y)]
                    
                    except:
                        visitedPositions[(tail_x, tail_y)] = True

    return len(visitedPositions)

def move_knot(rope: dict, head: int, tail: int):
    """
    In this next part of the problem, the issue is that, when an "internal" moves, it may happen
    that head has moved in another direction that is not the same as the input:

    ..........
    ..........
    ..........
    ..........
    ..54321H.. (5 covers 6, 7, 8, 9, s)
    ..........

    If we move up 4 times:
    -------First move-------
    ..........
    ..........
    ..........
    .......H..
    ..54321.. (5 covers 6, 7, 8, 9, s)
    ..........

    -------Second move-------
    ..........
    ..........
    .......H..
    ...54321..
    ..6....... (6 covers 7, 8, 9, s)
    ..........

    From the perspective of knot 2, knot 1 has moved to the right and up (the same is applied to the rest), when, 
    the input says only to move up 2 times. This in issue that causes us to not able to follow the simple logic
    from the previous part, now, we have to compute carefully every direction.

    Another thing to take into account is that if we continue moving:

    -------Third move-------
    ..........
    .......H..
    .......1..
    ...5432..
    ..6....... (6 covers 7, 8, 9, s)
    ..........

    -------Fourth move (before moving the sixth knot)-------
    .......H..
    .......1..
    ....5432..
    .........
    ..6....... (6 covers 7, 8, 9, s)
    ..........

    In this special case, the fifth knot is 2 position away in each axis, in the example provided in
    the web page, this is solved by moving diagonally:

    .......H..
    .......1..
    ....5432..
    ...6.....
    ..7....... (7 covers 8, 9, s)
    ..........

    So, we also have to be in the lookout for this special case.
    Args:
        rope (dict): Dictionary which represent the rope
        head (int): Index of the knot that acts as the head
        tail (int): Index of the knot that acts as the tail
    """

    # Head has moved above the tail
    if rope[head] ['y'] > rope[tail] ['y'] + 1:

        # If head and tail are at the same length
        if rope[head] ['x'] == rope[tail] ['x']:

            rope[tail] ['y'] += 1
        
        # Move diagonally
        else:

            diff = (rope[head]['x'] - rope[tail]['x'])

            # Special case: check if the difference in both axis is greater than two
            # 1.- The first axis is checked by the outer if
            # 2.- The second axis is checked here by calculating the difference (diff)
            # we add or substract 1 depending on the direction the head goes, also
            # we have to add or substract one since the maximum distance between axis is 2
            rope[tail]['x'] += diff if abs(diff) < 2 else diff + 1 if diff < 0 else diff - 1
            rope[tail]['y'] += 1


    # Head has moved below the tail
    elif rope[head] ['y'] < rope[tail] ['y'] - 1:

        # If head and tail are at the same length
        if rope[head] ['x'] == rope[tail] ['x']:

            rope[tail] ['y'] -= 1
        
        # Move diagonally
        else:

            diff = (rope[head]['x'] - rope[tail]['x'])

            # Special case: check if the difference in both axis is greater than two
            # 1.- The first axis is checked by the outer if
            # 2.- The second axis is checked here by calculating the difference (diff)
            # we add or substract 1 depending on the direction the head goes, also
            # we have to add or substract one since the maximum distance between axis is 2
            rope[tail]['x'] += diff if abs(diff) < 2 else diff + 1 if diff < 0 else diff - 1
            rope[tail]['y'] -= 1


    # Head has moved to the left of the tail
    elif rope[head] ['x'] < rope[tail] ['x'] - 1:

        # If head and tail are at the same height
        if rope[head] ['y'] == rope[tail] ['y']:

            rope[tail] ['x'] -= 1
        
        # Move diagonally
        else:
            
            diff = (rope[head]['y'] - rope[tail]['y'])

            # Special case: check if the difference in both axis is greater than two
            # 1.- The first axis is checked by the outer if
            # 2.- The second axis is checked here by calculating the difference (diff)
            # we add or substract 1 depending on the direction the head goes, also
            # we have to add or substract one since the maximum distance between axis is 2
            rope[tail]['y'] += diff if abs(diff) < 2 else diff + 1 if diff < 0 else diff - 1
            rope[tail]['x'] -= 1


    # Head has moved to the right of the tail
    elif rope[head] ['x'] > rope[tail] ['x'] + 1:

        # If head and tail are at the same height
        if rope[head] ['y'] == rope[tail] ['y']:

            rope[tail] ['x'] += 1
        
        # Move diagonally
        else:

            diff = (rope[head]['y'] - rope[tail]['y'])

            # Special case: check if the difference in both axis is greater than two
            # 1.- The first axis is checked by the outer if
            # 2.- The second axis is checked here by calculating the difference (diff)
            # we add or substract 1 depending on the direction the head goes, also
            # we have to add or substract one since the maximum distance between axis is 2
            rope[tail]['y'] += diff if abs(diff) < 2 else diff + 1 if diff < 0 else diff - 1
            rope[tail]['x'] += 1

    return

def solve_part2():
    """
    A key observation is that this problem is essentialy the same as before, 
    with the previou knots acting as a head for the following knot, which acts as a tail.
    However there is a remaining issue (see move_knot function)
    """
    with open('Day9_input.txt','r',encoding='utf8') as input:

        # Now, we have a rope of ten knots, which they all start in the same position
        # 0 represents the head of the rope and 1 to 9 represent the tail knots
        rope = {key:{'x': 0, 'y': 0} for key in range(10)}

        visitedPositions = {}
        for line in input:

            direction, n_moves = line.split()
            n_moves = int(n_moves)

            # Up
            if direction == 'U':
                
                for i in range(n_moves):

                    # First, move the head
                    rope[0] ['y'] += 1
                    
                    # Now, for the rest of the knots
                    for knot in range(9):

                        move_knot(rope, knot, knot + 1)

                    # Check if the tail has already been on that position
                    try:
                        visitedPositions[(rope[9]['x'], rope[9]['y'])]
                    
                    except:
                        visitedPositions[(rope[9]['x'], rope[9]['y'])] = True
                    
            # Down
            elif direction == 'D':

                for i in range(n_moves):
                    
                    # First, move the head
                    rope[0] ['y'] -= 1
                    

                    # Now, for the rest of the knots
                    for knot in range(9):

                        move_knot(rope, knot, knot + 1)

                    # Check if the tail has already been on that position
                    try:
                        visitedPositions[(rope[9]['x'], rope[9]['y'])]
                    
                    except:
                        visitedPositions[(rope[9]['x'], rope[9]['y'])] = True
            
            # Left
            elif direction == 'L':

                for i in range(n_moves):
                    
                    # First, move the head
                    rope[0] ['x'] -= 1
                    
                    # Now, for the rest of the knots
                    for knot in range(9):

                        move_knot(rope, knot, knot + 1)

                    # Check if the tail has already been on that position
                    try:
                        visitedPositions[(rope[9]['x'], rope[9]['y'])]
                    
                    except:
                        visitedPositions[(rope[9]['x'], rope[9]['y'])] = True

            # Right
            else:

                for i in range(n_moves):
                    
                    # First, move the head
                    rope[0] ['x'] += 1
                    
                    # Now, for the rest of the knots
                    for knot in range(9):

                        move_knot(rope, knot, knot + 1)

                    # Check if the tail has already been on that position
                    try:
                        visitedPositions[(rope[9]['x'], rope[9]['y'])]
                    
                    except:
                        visitedPositions[(rope[9]['x'], rope[9]['y'])] = True

    return len(visitedPositions)

def main():

    print("Part 1 solution = ", solve_part1())

    print("Part 2 solution = ", solve_part2())

if __name__ == "__main__":
    main()