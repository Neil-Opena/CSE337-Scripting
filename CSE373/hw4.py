import sys
import math
import queue
class EdgeNode():
    def __init__(self, y, next_edge=None):
        self.y = y
        self.next = next_edge

    def __str__(self):
        return str(self.y)

class Graph():
    def __init__(self):
        self.num_vertices = 0
        self.num_edges = 0
        self.adjacency_list = []
        self.degree_list = []

        self.finished = False
        self.setup_completed = False
        self.ordered_vertices = []
        self.min_degree = 0
        self.max_degree = 0
        self.lower_bound = 0

        self.heuristic = []
        self.solution = []
        self.solution_length = 0

    def read_graph(self, file_name):
        f = open(file_name)
        self.num_vertices = int(f.readline().strip()) # first line = number of vertices
        self.num_edges = int(f.readline().strip()) # second line = number of edges
        self.adjacency_list = [None]*self.num_vertices
        self.degree_list = [0]*self.num_vertices

        for edge_line in f:
            edge = edge_line.strip().split()
            x = int(edge[0])
            y = int(edge[1])
            self.insert_edge(x, y, False)

        self.solution_length = self.num_vertices

        self.ordered_vertices = [i[0] + 1 for i in sorted(enumerate(self.degree_list), key = lambda x:x[1])]
        self.min_degree = self.degree_list[self.ordered_vertices[0] - 1]
        self.max_degree = self.degree_list[self.ordered_vertices[-1] - 1]
        self.lower_bound = math.ceil(self.max_degree / 2)

        # perform bfs with vertex with smallest degree

        for i in range(0, self.num_vertices):
            if(i + 1 not in self.heuristic):
                self.heuristic += self.bfs(self.ordered_vertices[i])

        f.close()

    def insert_edge(self, x, y, is_directed):
        edge_node = EdgeNode(y, self.adjacency_list[x - 1])
        self.adjacency_list[x - 1] = edge_node
        self.degree_list[x - 1] += 1
        if(is_directed == False):
            self.insert_edge(y, x, True)

    def bfs(self, start):
        q = queue.Queue()
        discovered = set()
        discovered.add(start)
        q.put(start)
        result = []
        while(not q.empty()):
            v = q.get()
            result.append(v)
            edge = self.adjacency_list[v - 1]
            while(edge != None):
                y = edge.y
                if(y not in discovered):
                    q.put(y)
                    discovered.add(y)
                edge = edge.next
        return result

    def solve_bandwidth(self):
        a = [-1]*self.num_vertices #solution list
        k = 0
        self.finished = False
        self.permute_vertices(a, k)
        print(self.solution, "->", self.solution_length)

    def permute_vertices(self, a, k):
        if(k == len(a)): # if the length of the solution list == the number of vertices, print the permutation
            self.check_permutation(a)
        else:
            k += 1
            candidates = []
            self.generate_candidates(a, k, candidates)
            for i in range(0, len(candidates)):
                a[k - 1] = candidates[i]
                if(self.continue_from_prune(a,k)):
                    self.permute_vertices(a, k)
                    if(self.finished):
                        return
                a[k-1] = -1

    def continue_from_prune(self, a, k):
        if(self.get_bandwidth(a,k) < self.solution_length): # check if edges in the graph are higher than lower bound already
            return True
        print(a, "bandwidth=", self.get_bandwidth(a,k))
        return False

        # what if theres a check for symmetry

    def get_bandwidth(self, a, k):
        max_length = 0
        for i in range(0, k):
            # for each vertex in the solution vector, get the bandwidth
            v = a[i]
            edge = self.adjacency_list[v - 1]
            while(edge != None):
                temp_length = 0
                for j in range(0, k):
                    if(a[j] == edge.y):
                        temp_length = j - i
                        break
                if(temp_length != 0 and temp_length > max_length):
                    max_length = temp_length
                edge = edge.next
        return max_length

    def generate_candidates(self, a, k, c):
        # get numbers not in the array yet
        if(not self.setup_completed):
            for i in range(self.heuristic[k - 1], self.num_vertices + 1): # go through possible vertices
                found = False
                for j in range(0, k): # check solution vector for vertices placed
                    if a[j] == (i):
                        found = True
                if(not found):
                    c.append(i)
        else:
            for i in range(1, self.num_vertices + 1): # go through possible vertices
                found = False
                for j in range(0, k): # check solution vector for vertices placed
                    if a[j] == (i):
                        found = True
                if(not found):
                    c.append(i)

            # MAKE METHOD TO CHECK IF GREATER

    def check_permutation(self, a):
        # go through the vertices
        self.setup_completed = True
        max_length = 0
        for i in range(0, self.num_vertices):
            edge = self.adjacency_list[i]
            while(edge != None):
                # get distance from vertex (i + 1) and edge in permutation
                if(i+1 < edge.y): # only check half
                    start = -1
                    end = -1
                    for j in range(0, len(a)):
                        if(a[j] == (i + 1)):
                            start = j
                        if(a[j] == edge.y):
                            end = j
                    temp_length = abs(end - start)
                    if(temp_length > max_length):
                        max_length = temp_length
                edge = edge.next

        if(max_length < self.solution_length):
            self.solution_length = max_length
            self.solution = list(a)
            if(max_length <= self.lower_bound): # if it hits the lower bound, stop
                self.finished = True
        print(a, "=>", max_length)
        # find the longest edge based on permutation

file_name = sys.argv[1] 

graph = Graph()
graph.read_graph(file_name)
graph.solve_bandwidth()
