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

    def convert(self, lines):
        matrix = [[0 for word in line] for line in lines]
        color = [[0 for word in line] for line in lines]
        num = 0 
        for c in range(len(matrix)):
            for r in range(len(matrix[c])): 
                if lines[c][r] == '#':
                    matrix[c][r] = str(r)+' '+str(c)   
                    num += 1                 

        graph = networkx.DiGraph()
        for c in range(len(matrix)):
            for r in range(len(matrix[c])): 
                if matrix[c][r] != 0 and (color[c][r] == 0 or color[c][r] == 'red'):
                    # use if/elif so that there are no overlapping 'tiles'
                    # also to mark a node after a tile is 'placed' there
                    if c+1 <= len(matrix)-1 and matrix[c+1][r] != 0: #and color[c+1][r] == 0:
                        graph.add_edge(matrix[c][r], matrix[c+1][r], capacity=1)
                        color[c][r],color[c+1][r] = 'red', 'blue'
                    if c-1 >= 0 and matrix[c-1][r] != 0: #and color[c-1][r] == 0:
                        graph.add_edge(matrix[c][r], matrix[c-1][r], capacity=1)
                        color[c][r],color[c-1][r] = 'red', 'blue'                    
                    if r-1 >= 0 and matrix[c][r-1] != 0: #and color[c][r-1] == 0:
                        graph.add_edge(matrix[c][r], matrix[c][r-1], capacity=1)
                        color[c][r],color[c][r-1] = 'red', 'blue'
                    if r+1 <= len(matrix[c])-1 and matrix[c][r+1] != 0:# and color[c][r+1] == 0:
                        graph.add_edge(matrix[c][r], matrix[c][r+1], capacity=1)
                        color[c][r],color[c][r+1] = 'red', 'blue'
                elif matrix[c][r] != 0 and color[c][r] == 'blue':
                    if c+1 <= len(matrix)-1 and matrix[c+1][r] != 0 and color[c+1][r] in (0,'red') :
                        graph.add_edge(matrix[c+1][r], matrix[c][r], capacity=1)
                        color[c][r],color[c+1][r] = 'blue', 'red'
                    if c-1 >= 0 and matrix[c-1][r] != 0 and color[c-1][r] in (0,'red'):
                        graph.add_edge(matrix[c-1][r], matrix[c][r], capacity=1)
                        color[c][r],color[c-1][r] = 'blue', 'red'                   
                    if r-1 >= 0 and matrix[c][r-1] != 0 and color[c][r-1] in (0,'red'):
                        graph.add_edge(matrix[c][r-1], matrix[c][r], capacity=1)
                        color[c][r],color[c][r-1] = 'blue', 'red'
                    if r+1 <= len(matrix[c])-1 and matrix[c][r+1] != 0 and color[c][r+1] in (0,'red'):
                        graph.add_edge(matrix[c][r+1], matrix[c][r], capacity=1)
                        color[c][r],color[c][r+1] = 'blue', 'red'

        for c in range(len(matrix)):
            for r in range(len(matrix[c])):                 
                # check if a node is connected by anything 
                if color[c][r] == 'red' and matrix[c][r] != 0 and not graph.in_edges(nbunch=str(r)+' '+str(c)):
                    graph.add_edge('start', matrix[c][r], capacity=1)
                # check if a node connects to anything 
                elif color[c][r] == 'blue' and matrix[c][r] != 0 and not graph.out_edges(nbunch=str(r)+' '+str(c)):
                    graph.add_edge(matrix[c][r], 'end', capacity=1)
        return graph, num, color

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        graph, num, color = self.convert(lines)
        if graph.number_of_edges() > 0:
            solution = networkx.maximum_flow(graph,'start','end')#,flow_func='ford_fulkerson')
        else:
            return ['impossible'] # cases where there are 0 '#'s
        array = []
        for i in solution[1].items():
            for j in i[-1].items():
                if j[-1] == 1 and j[0] != 'end' and i[0] != 'start':
                    array.append(i[0]+' '+j[0])
        
        array = list(set(array))
        # we can only tile when the number of '#' is even, 
        # or resulting array length does not equal half of number of nodes 
        if num%2 != 0 or len(array) != num/2:
            return ['impossible']
        else:
            return array

