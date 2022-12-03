# Global variables

# ------------------------------- To solve part 1 -------------------------------
pick_scores = {
    # I play Rock
    'X': 1,

    # I play Paper
    'Y': 2,

    # I play Scissors
    'Z': 3
}

round_scores = {

    # Opponent plays Rock
    'A': {

        # I play Rock (loss)
        'X': 3,

        # I play Paper (win)
        'Y': 6,

        # I play Scissors (draw)
        'Z': 0
    },

    # Opponent plays Paper
    'B': {

        # I play Rock (loss)
        'X': 0,

        # I play Paper (draw)
        'Y': 3,

        # I play Scissors (win)
        'Z': 6
    },

    # Opponent plays Scissors
    'C': {

        # I play Rock (win)
        'X': 6,

        # I play Paper (loss)
        'Y': 0,

        # I play Scissors (draw)
        'Z': 3
    }
}

# ------------------------------- To solve part 2 -------------------------------
round_scores_part2 = {
    # I have to lose
    'X': 0,

    # I have to draw
    'Y': 3,

    # I have to win
    'Z': 6
}

pick_scores_part2 = {

    # Opponent plays Rock
    'A': {

        # I have to lose, then I must play Scissors 
        'X': 3,

        # I have to draw, then I must play Rock 
        'Y': 1,

        # I have to lose, then I must play Paper 
        'Z': 2
    },

    # Opponent plays Paper
    'B': {

        # I have to lose, then I must play Rock 
        'X': 1,

        # I have to draw, then I must play Paper 
        'Y': 2,

        # I have to lose, then I must play Scissors 
        'Z': 3
    },

    # Opponent plays Scissors
    'C': {


        # I have to lose, then I must play Paper 
        'X': 2,

        # I have to draw, then I must play Scissors 
        'Y': 3,

        # I have to lose, then I must play Rock 
        'Z': 1
    }
}

def solve_part1():

    total_score = 0
    for line in open('Day2_input.txt','r',encoding='utf8'):

        opponent, me = line.split()
        total_score += pick_scores[me] + round_scores[opponent][me]
        
    
    return total_score

def solve_part2():

    total_score = 0
    for line in open('Day2_input.txt','r',encoding='utf8'):

        opponent, me = line.split()
        total_score += pick_scores_part2[opponent][me] + round_scores_part2[me]
        
    
    return total_score

def main():

    print("Part 1 solution = ", solve_part1())
    print("Part 2 solution = ", solve_part2())

if __name__ == "__main__":
    main()
