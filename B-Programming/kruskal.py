class Vertice:
    def __init__(self, name, type, switch=None):
        self.name = name
        self.type = type
        self.switch = switch
        self.connected = False

class Kruskal:
    def __init__(self, V, E):
        self.vertices = V
        self.edges = E
        self.index_list = {}
        self.num_union = len(V)

    def makeSet(self):
        for i in self.vertices:
            self.index_list[i.name] = i
    
    def findSet(self,i):
        name = i.name
        if self.index_list[i.name].name == name:
            return self.index_list[name]
        return self.findSet(self.index_list[name])

    def union(self,i,j):
        label_1 = self.findSet(i)
        label_2 = self.findSet(j)
        if i.type == 'breaker' and j.type == 'box':
            self.index_list[label_2.name] = label_1
            return True
        elif j.type == "breaker" and i.type == "box":
            self.index_list[label_1.name] = label_2
            return True
        elif i.type == "breaker" and j.type == "switch":
            if j == label_2:
                self.index_list[label_2.name] = label_1
                return True
        elif j.type == "breaker" and i.type == "switch":
            if i == label_1:
                self.index_list[label_1.name] = label_2
                return True
        elif i.type == "box" and j.type == "switch":
            if j == label_2:
                self.index_list[label_2.name] = label_1
                return True
        elif j.type == "box" and i.type == "switch":
            if i == label_1:
                self.index_list[label_1.name] = label_2
                return True
        if i.type == "box" and j.type == "box":
            if j == label_2:
                self.index_list[label_2.name] = label_1
                return True
            elif label_1.type == "breaker":
                self.index_list[label_2.name] = label_1
                return True
            elif label_2.type == "breaker":
                self.index_list[label_1.name] = label_2
                return True
            self.index_list[label_1.name] = label_2
            return True
        elif i.type == "switch" and j.type == "light":
            if j.switch == i.name and not j.connected:
                self.index_list[label_2.name] = label_1
                j.connected = True
                return True
            else:
                return False
        elif j.type == "switch" and i.type == "light":
            if i.switch == j.name and not i.connected:
                self.index_list[label_1.name] = label_2
                i.connected = True
                return True
            else:
                return False
        if i.type == "light" and j.type == "light":
            if i.switch == j.switch:
                if i.connected and j.connected:
                    return False
                if j.connected:
                    self.index_list[label_1.name] = label_2
                    return True
                if i.connected:
                    self.index_list[label_2.name] = label_1
                    return True
                self.index_list[label_1.name] = label_2
                return True
            else:
                return False
        else:
            return False

    def kruskal(self):
        self.makeSet()
        minimum = 0
        sorted_edges = sorted(self.edges, key=lambda item: item[2])
        i = 0
        while self.num_union>1:
            v1, v2, w = sorted_edges[i]
            i+=1
            uset = self.findSet(v1)
            vset = self.findSet(v2)
            
            if (uset != vset):
                if self.union(v1,v2):
                    self.num_union -= 1
                    minimum+=w
        return minimum
    
x = input().split()
num_v = int(x[0])
num_e = int(x[1])
vertices = []
edges = []
for i in range(num_v):
    name, type = map(str, input().split())
    if type == 'outlet':
        type = 'box'
    if type == 'switch':
        switch = name
    v = Vertice(name, type)
    if type == 'light':
        v = Vertice(name, type, switch)
    vertices.append(v)
for i in range(num_e):
    x= input().split()
    v1, v2, w = x[0],x[1],int(x[2])
    for j in vertices:
        if j.name == v1:
            v1 = j
            break
    for j in vertices:
        if j.name == v2:
            v2 = j
            break 
    edges.append([v1,v2,w])  

k = Kruskal(vertices, edges)
print(k.kruskal())