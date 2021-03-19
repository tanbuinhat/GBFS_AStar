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
        minheuristic = h[open_list[0]]
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
         

    # function to be implemented
    def A_star(self, s, g, h): # em có tham khảo code tại đây https://github.com/vandersonmr/A_Star_Algorithm/blob/master/libs/python/AStar.py
        open_list = []
        closed_list = []
        open_list.append(s)
        
        parents = {}
        parents[s] = None

        cost_path_to_current = {}  #lưu giá trị cost từ đầu tới hiện tại
        f_cost = {}    
        cost_path_to_current[s] = 0
        f_cost[s] = cost_path_to_current[s] + h[s][0]
        cost_path_list = []      # lưu giá trị cost

        while open_list:
            current = self.getLowest(open_list,f_cost)

            if current == g:
                # path = self.reconstructPath(parents,g)
                return cost_path_list[-1] # giá trị cuối cùng là cost từ node đầu tới cuối ko tính heuristic

            open_list.remove(current)           
            closed_list.append(current)   

            for (i,v) in self.graph[current]:
                total_cost_path = cost_path_to_current[current] + v
                if i not in closed_list and i not in open_list:
                    parents[i] = current
                    cost_path_to_current[i] = total_cost_path
                    f_cost[i] = cost_path_to_current[i] + h[i][0]
                    cost_path_list.append(total_cost_path)
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

print(g.A_star(start, goal, heuristic))
f = open("output.txt", "w")
f.write(str(g.A_star(start, goal, heuristic)))