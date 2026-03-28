class Graph:

    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def add_vertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def add_edge(self, node1, node2):
        # undirected Graph
        if node2 not in self.adjacentList[node1]:
            self.adjacentList[node1].append(node2)
        if node1 not in self.adjacentList[node2]:
            self.adjacentList[node2].append(node1)

    def show_connections(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            vertex = None
            for vertex in nodeConnections:
                connections += vertex + " "

            print(node + "-->" + connections)


my_graph = Graph()
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')
my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')

my_graph.show_connections()
# Answer:
#  0-->1 2
#  1-->3 2 0
#  2-->4 1 0
#  3-->1 4
#  4-->3 2 5
#  5-->4 6
#  6-->
