import sys
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

        f.close()

    def insert_edge(self, x, y, is_directed):
        edge_node = EdgeNode(y, self.adjacency_list[x - 1])
        self.adjacency_list[x - 1] = edge_node
        self.degree_list[x - 1] += 1

        if(is_directed == False):
            self.insert_edge(y, x, True)

    def print_adjacency_list(self):
        for i in range(0, self.num_vertices):
            print(i + 1, "->", end = " ")
            edge = self.adjacency_list[i]
            while(edge != None):
                print(edge, end =" ")
                edge = edge.next
            print()

    def solve_bandwidth(self):
        a = [-1]*self.num_vertices #solution list
        k = 0
        self.finished = False
        self.permute_vertices(a, k)

    def permute_vertices(self, a, k):
        if(k == len(a)): # if the length of the solution list == the number of vertices, print the permutation
            print(a, end = "->")
            self.check_permutation(a)
        else:
            k += 1
            candidates = []
            self.generate_candidates(a, k, candidates, )
            for i in range(0, len(candidates)):
                a[k - 1] = candidates[i]
                self.permute_vertices(a, k)
                if(self.finished):
                    return
                a[k - 1] = -1

    def generate_candidates(self, a, k, c):
        # get numbers not in the array yet
        for i in range(0, self.num_vertices): # go through possible vertices
            found = False
            for j in range(0, k):
                if a[j] == (i + 1):
                    found = True
            if(not found):
                c.append(i + 1)

    def check_permutation(self, a):
        # go through the vertices
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
                    temp_length = end - start
                    if(temp_length > max_length):
                        max_length = temp_length
                edge = edge.next

        # FIXME
        print(max_length)
        if(a[0] == 1 and a[1] == 5 and a[2] == 6 and a[3] == 4 and a[4] == 7 and a[5] > 2):
            self.finished = True
        # find the longest edge based on permutation
        return True


file_name = sys.argv[1] 

graph = Graph()
graph.read_graph(file_name)
# graph.print_adjacency_list()
graph.solve_bandwidth()

# solve bandwith
# prune search space
# change data structure

