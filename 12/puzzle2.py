from queue import Queue

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
		
        # Directed or Undirected
        self.m_directed = directed
		
        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}      
	
    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))
    
    # Print the graph representation
    def print_adj_list(self):
      for key in self.m_adj_list.keys():
        print("node", key, ": ", self.m_adj_list[key])

    def bfs(self, start_node, target_node):
        # Set of visited nodes to prevent loops
        visited = set()
        queue = Queue()

        # Add the start_node to the queue and visited list
        queue.put(start_node)
        visited.add(start_node)
        
        # start_node has not parents
        parent = dict()
        parent[start_node] = None

        # Perform step 3
        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == target_node:
                path_found = True
                break

            for (next_node, weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)
                    
        # Path reconstruction
        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node]) 
                target_node = parent[target_node]
            path.reverse()
        return path 

with open("input.txt") as f:
    m = f.read().replace("\r\n", "\n").split("\n")
    m = list(map(lambda a: list(a), m))

graph = {f"{row},{col}": [] for row in range(len(m)) for col in range(len(m[row]))}

# print(graph)

start = []
end = ""

for loc in graph.keys():
    row, col = loc.split(",")
    row, col = int(row), int(col)

    if m[row][col] == "S" or m[row][col] == "a":
        start.append(loc)
        m[row][col] = "a"
    elif m[row][col] == "E":
        end = loc
        m[row][col] = "z"

for loc in graph.keys():
    row, col = loc.split(",")
    row, col = int(row), int(col)

    if row - 1 >= 0 and ord(m[row-1][col]) - ord(m[row][col]) <= 1:
        graph[loc].append(f"{row-1},{col}")
    
    if row + 1 < len(m) and (ord(m[row+1][col]) - ord(m[row][col])) <= 1:
        graph[loc].append(f"{row+1},{col}")
    
    if col + 1 < len(m[0]) and ord(m[row][col+1]) - ord(m[row][col]) <= 1:
        graph[loc].append(f"{row},{col+1}")

    if col - 1 >= 0 and ord(m[row][col-1]) - ord(m[row][col]) <= 1:
        graph[loc].append(f"{row},{col-1}")

c = 0
t = {}
for k in graph.keys():
    t[k] = c
    c += 1

g = Graph(len(m)*len(m[0]), directed=True)

for k in graph:
    for e in graph[k]:
        g.add_edge(t[k], t[e])

path_lens = []

for s in start:
    p = g.bfs(t[s], t[end])
    if len(p)-1 != -1:
        path_lens.append(len(p)-1)

print(min(path_lens))
