def solve_part1():

    input = open('Day8_input.txt','r',encoding='utf8').readlines()

    grid = []
    alreadyVisible = {}
    # Top and bottom rows of the grid
    visible = len(input[0][:-1]) * 2

    for line in input:

        grid.append( [int(elem) for elem in line[:-1]] )

    # Left and right columns of the grid
    visible += 2 * len(grid)

    # Remove the corners (they are counted twice)
    visible -= 4

    """
    The strategy to solve this problem is going to be based of the fact that the maximum
    height a tree can have is 9. The main intution is going to be that we can only see
    in a straight line from the edge.
    
    E.g. From position 3 we can only see trees of height: 7, 1, 3, 4 and 9. Now, since the last tree is on the edge
    that tree is already visible, we won't count that tree, the resulting trees are: 7, 1, 3, 4. Where 7 is the tree 
    at the edge, and 1, 3, 4 the "inner" trees. How do we know how many trees are visible? Well, here's where our fact
    comes into play.

    30373
    25512
    65332
    33549
    35390

    The maximum height a tree can have is 9, and the HEIGHT OF THE EDGE TREE IS 7 (this called starting_height in the code),
    which means, from that point, we can only see trees with height higher than 7 (8 and 9). So, we can approach this problem
    by travelling along a column (or row, which by the way, this rule can be extrapolated to rows) until we find a tree of 
    height 9, since, when we find such tree, that tree will block the following trees and there is no need to keep checking.

    It may happen that there is not a tree of height 9 in our row or column, in that case, we will have to check the whole
    row or column, we could calculate the maximum at that row or column, and go through it until we reach the maximum, but 
    that would have the same complexity as just checking the whole column or row.
    """

    # From top edge towards bottom
    for col in range(1, len(grid[0]) - 1):

        starting_height = grid[0][col]

        for row in range(1, len(grid) - 1):

            if grid[row][col] > starting_height:
                
                # Check if tree is already visible from another perspective
                try:
                    alreadyVisible[(row,col)]

                # Not visible from another perspective (this is done to not count the same tree twice)                
                except:
                    alreadyVisible[(row,col)] = True
                    visible += 1

                starting_height = grid[row][col]
            
            # We found a tree of height 9, go to next column
            if starting_height == 9:

                break

    # From bottom edge towards top
    for col in range(1, len(grid[-1]) - 1):

        starting_height = grid[-1][col]

        for row in range(len(grid) - 1, 0, -1):

            if grid[row][col] > starting_height:

                # Check if tree is already visible from another perspective
                try:
                    alreadyVisible[(row,col)]

                # Not visible from another perspective (this is done to not count the same tree twice)                
                except:
                    alreadyVisible[(row,col)] = True
                    visible += 1

                starting_height = grid[row][col]
                
            
            # We found a tree of height 9, go to next column
            if starting_height == 9:

                break

    # From left edge towards right
    for row in range(1, len(grid) - 1):

        starting_height = grid[row][0]

        for col in range(1, len(grid[0]) - 1):

            if grid[row][col] > starting_height:

                # Check if tree is already visible from another perspective
                try:
                    alreadyVisible[(row,col)]

                # Not visible from another perspective (this is done to not count the same tree twice)                
                except:
                    alreadyVisible[(row,col)] = True
                    visible += 1

                starting_height = grid[row][col]
            
            # We found a tree of height 9, go to next row
            if starting_height == 9:

                break

    # From right edge towards left
    for row in range(1, len(grid) - 1):

        starting_height = grid[row][-1]

        for col in range(len(grid[-1]) - 1, 0, -1):

            if grid[row][col] > starting_height:

                # Check if tree is already visible from another perspective
                try:
                    alreadyVisible[(row,col)]

                # Not visible from another perspective (this is done to not count the same tree twice)                
                except:
                    alreadyVisible[(row,col)] = True
                    visible += 1

                starting_height = grid[row][col]

            # We found a tree of height 9, go to next row
            if starting_height == 9:

                break
    
    # We will reuse the grid and the visible trees for next part 
    return grid, visible, alreadyVisible

def solve_part2(grid, alreadyVisible):
    """
    In this next part we will take advantage from the dictionary built in the previous part,
    and the main idea to solve this is that trees that are visible will obviously have higher scenic view than
    non visible trees. So, we will use the previously calculated visible trees and iterate over them as a little optimization.
    Args:
        grid (list): The input
        alreadyVisible (dict): Dictionary of visible tress
    """
    max_view = 0
    for (row, col) in alreadyVisible:

        scenic_view = 1

        # Towards top edge
        for i in range(row - 1, -1 ,-1):

            if grid[i][col] >= grid[row][col]:
                break

        scenic_view *= (row - i)

        # Towards bottom edge
        for i in range(row + 1, len(grid)):

            if grid[i][col] >= grid[row][col]:
                break
        
        scenic_view *= (i - row)

        # Towards left edge
        for i in range(col - 1, -1 ,-1):

            if grid[row][i] >= grid[row][col]:
                break

        scenic_view *= (col - i)    

        # Towards right edge
        for i in range(col + 1, len(grid[row])):

            if grid[row][i] >= grid[row][col]:
                break

        scenic_view *= (i - col)  

        
        if scenic_view > max_view:
            max_view = scenic_view

    return max_view

def main():

    grid, visible, alreadyVisible = solve_part1()


    print("Part 1 solution = ", visible)

    print("Part 2 solution = ", solve_part2(grid, alreadyVisible))

    return

if __name__ == "__main__":
    main()