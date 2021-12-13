def solve(input,folds,part = 1):


    for fold in folds:
        new_dots = {}
        if fold[0] == 'x':

            for dot in input:

                if dot[0] > fold[1]:
                    new_dots[(dot[0] - 2*( dot[0]- fold[1] ), dot[1])] = None
                else:
                    new_dots[(dot[0] ,dot[1])] = None
            
            
        else:
            for dot in input:

                if dot[1] > fold[1]:
                    new_dots[(dot[0] , dot[1] - 2*( dot[1] - fold[1]) )] = None
                else:
                    new_dots[(dot[0] ,dot[1])] = None

        input = new_dots


    if part == 1:
        return len(input)
    else:
        import matplotlib.pyplot as plt
        x = []
        y = []
        for key in input:
            x.append(key[0])
            y.append(key[1])
        ax = plt.gca()
        ax.invert_yaxis()
        l = ax.figure.subplotpars.left
        r = ax.figure.subplotpars.right
        t = ax.figure.subplotpars.top
        b = ax.figure.subplotpars.bottom
        figw = float(5)/(r-l)
        figh = float(1.2)/(t-b)
        ax.figure.set_size_inches(figw, figh)
        plt.scatter(x, y)
        plt.show()
        return
"""

fold along x=655 (fold left)
fold along y=447 (fold up)
fold along x=327 (fold left)
fold along y=223 (fold up)
fold along x=163 (fold left)
fold along y=111 (fold up)
fold along x=81 (fold left)
fold along y=55 (fold up)
fold along x=40 (fold left)
fold along y=27 (fold up)
fold along y=13 (fold up)
fold along y=6 (fold up)
"""

input = {}

folds = [ ["x",655]  , ["y",447], ["x",327], ["y",223] ,
 ["x",163] , ["y",111] , ["x",81] , ["y",55] , ["x",40] , ["y",27] , ["y",13] , ["y",6] ]

# Get input, only the dots
with open("Day13_input.txt",'r') as inputfile:
    for line in inputfile:
        line = [int(e) for e in line.split("\n")[0].split(",")]
        input[(line[0],line[1])] = None

part1_sol= solve(input,folds)
print("Part 1 solution:", part1_sol)
solve(input,folds,part=2)
