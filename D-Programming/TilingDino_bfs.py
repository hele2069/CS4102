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

    def isAdjacent(self, node1, node2):
        x1,y1 = node1.split(' ')
        x2,y2 = node2.split(' ')
        if int(x1) == int(x2) and abs(int(y1)-int(y2)) == 1:
            return True 
        elif int(y1) == int(y2) and abs(int(x1)-int(x2)) == 1:
            return True 
        else:
            return False 

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        nodes = []
        num = 0 

        graph = networkx.DiGraph()

        # instantiate nodes 
        for c in range(len(lines)):
            for r in range(len(lines[c])): 
                if lines[c][r] == '#':
                    nodes.append(str(r)+' '+str(c))
                    graph.add_node(str(r)+' '+str(c))
                    num += 1                 
        # if there are no '#'s, return impossible
        if num == 0 or num%2 != 0: 
            return ['impossible']

        # add adjacent edges 
        for i in range(len(nodes)):
            for j in range(i+1,len(nodes)):
                if self.isAdjacent(nodes[i],nodes[j]):
                    graph.add_edge(nodes[i],nodes[j],capacity=1)
        # if there are no edges, return impossible
        if graph.number_of_edges() == 0:
            return ['impossible']

        # BFS
        left = []
        right = []
        discovered = []
        level = {}
        while nodes: 
            start_node = nodes[0]
            left.append(start_node)
            discovered.append(start_node)
            nodes.remove(start_node)
            level[start_node] = 0
            queue = []
            queue.append(start_node)
            while queue:
                temp = queue.pop(0)
                for i in list(graph.neighbors(temp)):
                    if i not in discovered:
                        discovered.append(i)
                        nodes.remove(i)
                        level[i] = level[temp]+1
                        queue.append(i)
                        if (level[temp]+1)%2 == 0:
                            left.append(i)
                        else: 
                            right.append(i)

        # link start and end node 
        for i in range(len(left)):
            graph.add_edge('start',left[i],capacity=1)
        for i in range(len(right)):
            graph.add_edge(right[i],'end',capacity=1)

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

