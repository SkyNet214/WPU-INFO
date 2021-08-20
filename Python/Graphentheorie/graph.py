# graph .py
# Ein Graph ist ein Menge von Knoten und eine Menge von ungerichteten Kanten
# Die Darstellung erfolgt in einer Adjazenzliste mithilfe eines Dictionary
# Knotenwerte sind vorerst nur Zahlen

class Graph():
    def __init__ (self, graph={}) -> None :
        self.__graph = graph

    def vertex_count(self) -> int:
        return len(self.__graph) # Anzahl der Knoten

    def vertices(self):
        """gibt die Knoten des Graphen aus"""
        return list(self.__graph.keys())

    def _generate_edges(self):
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                edges.append({node,neighbour})
        return edges

    def edges(self):
        """ gibt die Kanten eines Graphen aus """
        return self._generate_edges()

    # Die wohlformatierte Ausgabe eins Graphen ermoeglichen
    def __str__(self) -> str:
        res = "vertices:"
        for k in self.__graph :
            res += str(k) + " "
        res += "\nedges: "
        for edge in self._generate_edges():
            res += str(edge) + " "
        return res

    def add_edge(self, edge):
        (v0, v1) = tuple(edge)
        if v0 in self.__graph:
            self.__graph[v0].append(v1)
        else:
            self.__graph[v0] = [v1]

    def add_vertex(self, vertex):
        if vertex not in self.__graph:
            self.__graph[vertex] = []

    def contains(self, node):
        for i in self.__graph:
            if i == node:
                return True
            for j in self.__graph[i]:
                if j == node:
                    return True
        return False

    def contains_cycles(self):
        def check_neighbours(graph_dict, v0, n):
            if n in graph_dict:
                for i in graph_dict[n]:
                    if i == v0 or check_neighbours(graph_dict, v0, i):
                        return True
            return False

        for i in self.__graph:
            if check_neighbours(self.__graph, i, i):
                return True
        return False

if __name__ == "__main__":
    # Grundlegende Konstruktion des Graphen testen

    #d ={1:[1] ,5:[2 ,3]}
    d = {1:[2], 2:[3], 3:[4,5,6], 6:[90, 64], 90:[1], 64:[]}
    graph = Graph(d)
    print(graph)
    print("Edges of graph:")
    print(graph.edges())
    graph.add_edge({2 ,3})
    print(graph.edges())
    print(graph)
    print(graph.contains(20))
    print(graph.contains_cycles())