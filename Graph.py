

class Graphs:

    def __init__(self):
        self.adjacency_list = {};

    def add_vertex(self,vertex):

        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = [];
            return True;
        return False;

    def print_graph(self):

        for vertex in self.adjacency_list:
            print(vertex,':',self.adjacency_list[vertex]);

    def add_edge(self,vertext1,vertext2):

        if vertext1 in self.adjacency_list.keys() and vertext2 in self.adjacency_list.keys():
            self.adjacency_list[vertext1].append(vertext2);
            self.adjacency_list[vertext2].append(vertext1);
            return True;
        return False;

    def remove_edge(self,vertext1,vertext2):

        if vertext1 in self.adjacency_list.keys() and vertext2 in self.adjacency_list.keys():
            self.adjacency_list[vertext1].remove(vertext2);
            self.adjacency_list[vertext2].remove(vertext1);
            return True;
        return False;



customGraph = Graphs();
customGraph.add_vertex("A");
customGraph.add_vertex("B");
customGraph.add_vertex("C");
customGraph.add_edge('A','B');
customGraph.add_edge("A","C");
customGraph.add_edge("B","C");
customGraph.print_graph();
print("after removeing");
customGraph.remove_edge("A","C");
customGraph.print_graph();




#Graph created using adjacency matrix.
class Graph:
    
    def __init__(self,gdict=None):

        if gdict is None:
            gdict = {};
        self.gdict = gdict;

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge);

customDict = {"a":['b','c'],
              "b":['a','d','e'],
              "c":['a','e'],
              "d":['b','e','f'],
              "e":['d','f'],
              "f":['d','e']
              }
graph = Graph(customDict);
graph.addEdge("e",'c');
print(graph.gdict);
print(graph.gdict['e']);



