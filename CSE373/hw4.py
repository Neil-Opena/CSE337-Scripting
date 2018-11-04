import sys
import math
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
        self.max_degree = 0
        self.min_degree = 0
        self.solution = 0
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

        self.min_degree = self.get_min_degree()
        self.solution_length = self.num_vertices

        f.close()

    def get_min_degree(self):
        minimum = self.num_vertices
        for i in range(0, len(self.degree_list)):
            if(self.degree_list[i] < minimum):
                minimum = self.degree_list[i]
        return minimum

    def insert_edge(self, x, y, is_directed):
        edge_node = EdgeNode(y, self.adjacency_list[x - 1])
        self.adjacency_list[x - 1] = edge_node
        self.degree_list[x - 1] += 1
        if(self.degree_list[x - 1] > self.max_degree):
            self.max_degree = self.degree_list[x - 1]

        if(is_directed == False):
            self.insert_edge(y, x, True)

    def solve_bandwidth(self):
        a = [0]*self.num_vertices #solution list
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
        if(self.degree_list[a[0] - 1] == self.min_degree): #first vertex should have minimum degree
            return True

        # check if edges in the graph are higher than lower bound already
        # FIXME

        # what if theres a check for symmetry
        return False

    def generate_candidates(self, a, k, c):
        # get numbers not in the array yet
        # generate solution through bfs
        # make method to generate solution as a graph variable
        #b = [6,3,7,1,2,4,5,8,9,10] # bt-10-9
        #b = [1,5,6,4,7,2,10,8,9,3] # p-10-9
        #b = [1,4,8,9,2,3,6,5,7,10,11] # t-11-10
        b = [3,4,14,9,15,21,11,24,18,20,25,7,23,19,10,1,8,12,5,6,17,2,22,16,13]
        if(not self.setup_completed):
            for i in range(b[k - 1], self.num_vertices + 1): # go through possible vertices
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
                # revise later
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
            self.solution = a
            if(max_length <= math.ceil(self.max_degree / 2)): # if it hits the lower bound, stop
                self.finished = True
        print(a, "=>", max_length)
        # find the longest edge based on permutation

file_name = sys.argv[1] 

graph = Graph()
graph.read_graph(file_name)
graph.solve_bandwidth()

