

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
            try:
                self.adjacency_list[vertext1].remove(vertext2);
                self.adjacency_list[vertext2].remove(vertext1);
            except:
                pass
            return True;
        return False;


    def remove_vertext(self,vertext):

        if vertext in self.adjacency_list.keys():

            for other_vertext in self.adjacency_list[vertext]:
                self.adjacency_list[other_vertext].remove(vertext);
            del self.adjacency_list[vertext];
            return True;
        return False;





customGraph = Graphs();
customGraph.add_vertex("A");
customGraph.add_vertex("B");
customGraph.add_vertex("C");
customGraph.add_vertex("D");
customGraph.add_edge('A','B');
customGraph.add_edge("A","C");
customGraph.add_edge("A","D");
customGraph.add_edge("B","C");
customGraph.add_edge("C","D");
customGraph.print_graph();
print("after removeing");
#customGraph.remove_edge("A","C");
#customGraph.remove_edge("A","D");
customGraph.print_graph();

#After removed vertext;
print("after removing vertext");
#customGraph.remove_vertext("D");
print(customGraph.print_graph());




#Graph created using adjacency matrix.
class Graph:
    
    def __init__(self,gdict=None):

        if gdict is None:
            gdict = {};
        self.gdict = gdict;

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge);



    def dfs(self,vertext):
        
        visited = [vertext];
        queue = [vertext];

        while queue:
            devVertext = queue.pop(0);
            print(devVertext);

            for adjacency in self.gdict[devVertext]:
                if adjacency not in visited:
                    visited.append(adjacency);
                    queue.append(adjacency);

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
graph.dfs("a");
