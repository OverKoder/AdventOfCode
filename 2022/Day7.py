# ------------- Global Variables -------------------
total = 0

class Directory():

    def __init__(self, name, parent) -> None:
        
        # Name of the directory
        self.name = name 

        # Parent directory
        self.parent = parent

        # Size of directory (this will be updated)
        self.size = -1
        
        # Children directories
        self.child_nodes = {}

        # Files of the directory (which, at the same time, are not directories)
        self.files = []

    def isLeaf(self):
        return len(self.child_nodes) == 0

    def addChild(self, child):

        self.child_nodes[child.name] = child
        return

    def getChild(self, name):

        return self.child_nodes[name]

    def addFile(self, file, size):

        self.files.append((file,size))
        return

    def updateSize(self):
        """
        Recursively updates the size of all directories (this method is only called on the root directory)
        """
        global total

        # Base case: We reached a leaf node (NO DIRECTORIES!!!), which means the
        # size of the directory is the sum of the sizes of the files
        if self.isLeaf():
            self.size = sum([tupl[1] for tupl in self.files])

            # Check if size is less than threshold given in the problem
            if self.size < 100000:
                total += self.size

        # General case: the size of the directory is the sum of the sizes of the files
        # and the directories
        else:

            # First, sum the size of the files
            self.size = sum([tupl[1] for tupl in self.files])

            # Now add, the size of the children
            for child in self.child_nodes:

                self.size += self.child_nodes[child].updateSize()

            if self.size < 100000:
                total += self.size

        return self.size

def solve_part1():

    global total

    """
    We will divide this problem into two sections:
    1.- Build the directory tree given the input.
    2.- Given the directory tree from the previous section, compute recursively the size of each directory
    """

    input = open('Day7_input.txt','r', encoding='utf8').readlines()

    i = 1

    # Create root directory
    current_directory = Directory(name='/', parent = None)
    root = current_directory
    while i < len(input):

        # Read line
        line = input[i]

        # If it's a command, the line starts with '$', and commands are either 'cd' or 'ls
        if line[0] == '$':

            line = line.split()
            
            # 'ls' command, the following lines will all be files or directories, until a line starts with '$', a command
            if len(line) == 2:
                
                i += 1
                # Read line
                line = input[i]

                while(line[0] != '$') and i < len(input):

                    line = line.split()
                    
                    # current_directory contains another directory
                    if line[0] == 'dir':
                        
                        child = Directory(name=line[1],parent=current_directory)
                        current_directory.addChild(child)
                    
                    else:

                        current_directory.addFile(file=line[1], size=int(line[0]))

                    i += 1
                    if i < len(input):
                        line = input[i]

            # 'cd' command
            else:
                
                target = line[2]

                # If target directory is '..' this means change to parent directory
                if target == '..':
                    current_directory = current_directory.parent

                # Change to a child directory
                else:
                    current_directory = current_directory.getChild(target)
                    
                i += 1
                
    # Now, update all sizes, starting from the root node
    root.updateSize()

    # We return root, since the tree used in this solution is used
    # in the next part
    return root, total

def solve_part2(node, delete_sizes):
    """
    This part consists of running through the tree and checking the size of each directory
    """

    # Base case: We reached a leaf node, we check if this directory
    # can free enough space
    if node.isLeaf() and node.size >= 8381165:
        delete_sizes.append(node.size)
        return delete_sizes

    # General case: Recursively check the child nodes
    else:

        for child in node.child_nodes:

            solve_part2(node.child_nodes[child], delete_sizes)

    if node.size >= 8381165:
        delete_sizes.append(node.size)

    return delete_sizes


def main():

    root, total = solve_part1()
    print("Part 1 solution = ", total)

    print("Part 2 solution = ", min(solve_part2(root, [])))

    return

if __name__ == "__main__":
    main()