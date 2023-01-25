from collections import defaultdict

class Graph:
 
    def __init__(self,vertices):
        self.vertex= vertices
        self.graph = defaultdict(list)
 
    def edge(self,x,y):
        self.graph[x].append(y)

    def DLS(self,source,target,maxDepth):

        if source == target : 
            return True

        if maxDepth <= 0 : 
            return False

        for val in self.graph[source]:
                if(self.DLS(val,target,maxDepth-1)):
                    return True
        return False
 
    def target(self,source, target, maxDepth):
        for ele in range(maxDepth):
            if (self.DLS(source, target, ele)):
                return True
        return False
 
g = Graph (7);
g.edge(0, 1)
g.edge(0, 2)
g.edge(1, 3)
g.edge(1, 4)
g.edge(2, 5)
g.edge(2, 6)
 
target = 6; maxDepth = 3; source = 0
 
if g.target(source, target, maxDepth) == True:
    print ("Target is found")
else :
    print ("Target is not found")

        
