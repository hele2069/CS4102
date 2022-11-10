# CS4102 Spring 2022 -- Unit D Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: 
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import networkx

class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        num = 0 
        nodes = [[0 for word in line] for line in lines]
        color = [[0 for word in line] for line in lines]
        for i in range(len(color)):
            for j in range(len(color[i])):
                if (i + j) % 2 == 0:
                    color[i][j] = 'left'
                else:
                    color[i][j] = 'right'

        graph = networkx.DiGraph()
        # instantiate nodes 
        for c in range(len(lines)):
            for r in range(len(lines[c])): 
                if lines[c][r] == '#':
                    nodes[c][r] = (str(r)+' '+str(c))
                    num += 1                 

        # if there are no '#'s, return impossible
        if num == 0 or num%2 != 0: 
            return ['impossible']

        # add adjacent edges 
        for c in range(len(nodes)):
            for r in range(len(nodes[i])):
                if nodes[c][r] != 0 and color[c][r] == 'left':
                    if c+1 <= len(nodes)-1 and nodes[c+1][r] != 0:
                        graph.add_edge(nodes[c][r], nodes[c+1][r], capacity=1)
                    if c-1 >= 0 and nodes[c-1][r] != 0:
                        graph.add_edge(nodes[c][r], nodes[c-1][r], capacity=1)
                    if r+1 <= len(nodes[c])-1 and nodes[c][r+1] != 0:
                        graph.add_edge(nodes[c][r], nodes[c][r+1], capacity=1)
                    if r-1 >= 0 and nodes[c][r-1] != 0:
                        graph.add_edge(nodes[c][r], nodes[c][r-1], capacity=1)
                elif nodes[c][r] != 0 and color[c][r] == 'right':  
                    if c+1 <= len(nodes)-1 and nodes[c+1][r] != 0:
                        graph.add_edge(nodes[c+1][r], nodes[c][r], capacity=1)
                    if c-1 >= 0 and nodes[c-1][r] != 0:
                        graph.add_edge(nodes[c-1][r], nodes[c][r], capacity=1)
                    if r+1 <= len(nodes[c])-1 and nodes[c][r+1] != 0:
                        graph.add_edge(nodes[c][r+1], nodes[c][r], capacity=1)
                    if r-1 >= 0 and nodes[c][r-1] != 0:
                        graph.add_edge(nodes[c][r-1], nodes[c][r], capacity=1)

        # if there are no edges, return impossible
        if graph.number_of_edges() == 0:
            return ['impossible']

        # link start and end node 
        for c in range(len(nodes)):
            for r in range(len(nodes[c])):
                if nodes[c][r] != 0 and color[c][r] == 'left':
                    graph.add_edge('start',nodes[c][r], capacity=1)
                elif nodes[c][r] != 0 and color[c][r] == 'right':
                    graph.add_edge(nodes[c][r],'end', capacity=1)

        # --------------finding solution----------------------------#
        solution = networkx.maximum_flow(graph,'start','end')#,flow_func='ford_fulkerson')
        array = []
        for i in solution[1].items():
            for j in i[-1].items():
                if j[-1] == 1 and j[0] != 'end' and i[0] != 'start':
                    array.append(i[0]+' '+j[0])

        # array = list(set(array)) # remove duplicates 
        # we can only tile when the number of '#' is even, 
        # or resulting array length does not equal half of number of nodes 
        if len(array) != num/2:
            return ['impossible']
        else:
            return array

