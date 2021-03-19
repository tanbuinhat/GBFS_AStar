from collections import defaultdict
import heapq

# define graph
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, l):
        self.graph[u].append((v, l))


    def getLowest(self,open_list,h):
        minheuristic = h[0]
        lowestNode = None
        for node in open_list:
            if h[node] <= minheuristic: 
                minheuristic = h[node] 
                lowestNode = node
        return lowestNode

    def reconstructPath(self,cameFrom,goal):
        path = []
        node = goal
        path.append(node)
        while node in cameFrom:
            node = cameFrom[node]
            if node == None:
                break
            path.append(node)
        return path        
        

    def sumHeuristic(self,path,h):
        sum = 0
        for i in path:
            for j in h[i]:
                sum = sum + j
        return sum       


    # function to be implemented
    def GBFS(self, s, g, h):  # em có tham khảo code tại đây https://github.com/vandersonmr/A_Star_Algorithm/blob/master/libs/python/AStar.py
        open_list = []
        closed_list = []
        open_list.append(s)
        parents = {}
        parents[s] = None

        while open_list:
            current = self.getLowest(open_list,h)

            if current == g:
                path = self.reconstructPath(parents,g)
                return self.sumHeuristic(path,h)

            open_list.remove(current)           
            closed_list.append(current)   

            for (i,v) in self.graph[current]:
                if i not in closed_list:
                    parents[i] = current
                    if i not in open_list:
                        open_list.append(i)    
                else:
                    if i in closed_list:
                        continue
        return 0


# Driver code
# Create a graph given in the above diagram
g = Graph()
heuristic = []


with open('input.txt', 'r') as f:
    n, m = [int(x) for x in next(f).split()]
    for i in range(m):
        u, v, l = [int(x) for x in next(f).split()]
        g.addEdge(u, v, l)
    for i in range(n):
        h = [int(x) for x in next(f).split()]
        heuristic.append(h)
    start, goal = [int(x) for x in next(f).split()]

print(g.GBFS(start, goal, heuristic))
f = open("output.txt", "w")
f.write(str(g.GBFS(start, goal, heuristic)))