# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: yh9vhg
# Collaborators: None
# Sources: Introduction to Algorithms, Cormen
#################################
from random import vonmisesvariate
import time

class Supply:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        edgeWeightSum = 0
        # your function to compute the result should be called here
        disjointsets = self.convert(file_data)
        return disjointsets.solution()
    
    def convert(self, input):
        x = [n.split(' ') for n in input]
        vertices = []
        edges = []
        num_v = int(x[0][0]) # number of vertices
        num_e = int(x[0][1]) # number of edges

        for i in range(1,num_v+1): # instantiate vertices and add to list
            v = Vertex(name=x[i][0], type=x[i][1])
            vertices.append(v)
        for j in range(num_v+1, num_e+num_v+1): # instantiate edges and add to list
            v1, v2, w = x[j][0],x[j][1],int(x[j][2])

            for j in vertices: # turn each string-type v into Vertex-type v
                if j.name == v1:
                    v1 = j 
                    #v1 = Vertex(j.name, j.type)
                    #v1.store_belongs_to = j.store_belongs_to
                    break
            for j in vertices: # turn each string-type v into Vertex-type v
                if j.name == v2:
                    v2 = j 
                    #v2 = Vertex(j.name, j.type)
                    #v2.store_belongs_to = j.store_belongs_to                    
                    break 
            edges.append([v1,v2,w]) 

        # for each distribution center, link its name to stores that 'belong' to it 
        for i in range(0,len(vertices)): 
            if vertices[i].type == 'dist-center':
                iter = i + 1
                while iter < len(vertices) and vertices[iter].type == 'store':
                    vertices[iter].store_belongs_to = vertices[i].name
                    iter += 1

        return Disjoint_set(V=vertices, E=edges) # create a disjointset with vertices and edges
    

class Vertex:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        # only assign when type = store and the store is 'linked' to another distribution center
        self.store_belongs_to = None 

class Disjoint_set:
    def __init__(self, V, E):
        self.vertices = V
        self.edges = E
        self.index_list = {}

    def makeSet(self):
        for i in self.vertices:
            self.index_list[i.name] = i
    
    def findSet(self,i): # i is vertex 
        name = i.name
        if self.index_list[i.name].name == name:
            return self.index_list[name]
        return self.findSet(self.index_list[name]) # return type 

    def union(self,i,j):
        label_1 = self.findSet(i)
        label_2 = self.findSet(j)
        self.index_list[label_2.name] = label_1
    
    def remove_edges(self):
        for i in list(self.edges):
            if i[0].type == 'port':
                if i[1].type =='store':
                    self.edges.remove(i)
                elif i[1].type == 'port':
                    self.edges.remove(i)
            elif i[0].type == 'rail-hub' and i[1].type =='store':
                self.edges.remove(i)
            elif i[0].type == 'dist-center': 
                if i[1].type == 'store' and i[1].store_belongs_to != i[0].name:
                    self.edges.remove(i)
                elif i[1].type == 'dist-center':
                    self.edges.remove(i)
            elif i[0].type == 'store':
                if i[1].type == 'dist-center' and i[0].store_belongs_to != i[1].name:
                    self.edges.remove(i)
                elif i[1].type == 'port':
                    self.edges.remove(i)     
                elif i[1].type == 'rail-hub':          
                    self.edges.remove(i)     

            # reverse-order check ********
            elif i[1].type == 'port':
                if i[0].type =='store':
                    self.edges.remove(i)
                elif i[0].type == 'port':
                    self.edges.remove(i)
            elif i[1].type == 'rail-hub' and i[0].type =='store':
                    self.edges.remove(i)
            elif i[1].type == 'dist-center': 
                if i[0].type == 'store' and i[0].store_belongs_to != i[1].name:
                    self.edges.remove(i)
                elif i[0].type == 'dist-center':
                    self.edges.remove(i)    
            elif i[1].type == 'store':
                if i[0].type == 'dist-center' and i[1].store_belongs_to != i[0].name:
                    self.edges.remove(i)
                elif i[0].type == 'port':
                    self.edges.remove(i)
                elif i[0].type == 'rail-hub':
                    self.edges.remove(i)

    def solution(self):
        self.makeSet()
        minimum = 0
        self.remove_edges()
        sorted_edges = sorted(self.edges, key=lambda item: item[2])
        i = 0
        edges_accepted = 0
        
        while edges_accepted < len(self.vertices) - 1:
            v1, v2, w = sorted_edges[i]
            i += 1
            uset = self.findSet(v1)
            vset = self.findSet(v2)
            
            if (uset != vset):
                edges_accepted += 1
                self.union(uset,vset)
                minimum += w
                # print(v1.name,v2.name,w) -- testing only

        return minimum