import pygame, os, random, math, json, ast
from pygame.font import Font

pygame.init()

path = os.path.dirname(os.path.abspath(__file__)) + "\\"
font_size = 48
size = width, height = 960, 540
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 48)
pygame.display.set_caption("Graph Visualizer")
pygame.display.set_icon(pygame.image.load(path + "icon.png"))

VERTEX_SIZE = 50

LIGHT_GRAY = (176, 176, 176)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

class Vertex(pygame.sprite.Sprite):
    id = 0
    def __init__(self, pos, value=None):
        super(Vertex, self).__init__()
        self.pos = pos
        self.id = Vertex.id
        Vertex.id += 1
        self.dragged = False
        self.rect = pygame.Rect(pos, (VERTEX_SIZE, VERTEX_SIZE))
        self.value = self.id if value == None else value

    def render(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.rect.x+VERTEX_SIZE/2), int(self.rect.y+VERTEX_SIZE/2)), int(VERTEX_SIZE/2), int(VERTEX_SIZE/2))
        text = font.render(str(self.value), True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

class Edge(pygame.sprite.Sprite):
    id = 0
    def __init__(self, v0: Vertex, v1: Vertex):
        super(Edge, self).__init__()
        self.v0 = v0
        self.v1 = v1
        self.id = Edge.id
        Edge.id += 1

    def render(self, surface):
        pygame.draw.aaline(surface, GREEN, self.v0.rect.center, self.v1.rect.center)


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
                edges.append((node,neighbour))
        return edges

    def edges(self):
        """ gibt die Kanten eines Graphen aus """
        return self._generate_edges()

    # Die wohlformatierte Ausgabe eins Graphen ermoeglichen
    def __str__(self) -> str:
        res = "vertices:" + str(self.vertices())
        res += "\nedges: "
        for edge in self._generate_edges():
            res += str(edge) + " "
        res += "\nadjacency list: " + str(self.__graph)
        return res

    def add_edge(self, edge):
        (v0, v1) = edge
        if v0 in self.__graph:
            self.__graph[v0].append(v1)
        else:
            self.__graph[v0] = [v1]

    def add_vertex(self, vertex):
        if vertex not in self.__graph:
            self.__graph[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.vertices():
            self.__graph.pop(vertex)
            for v in self.__graph:
                if vertex in self.__graph[v]:
                    self.__graph[v].remove(vertex)

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

    def merge(self, graph):
        print(self.__graph)
        print(graph.__graph)
        self.__graph = {**self.__graph, **graph.__graph}
        print(self.__graph)

def draw_window():
    screen.fill(BLACK)
    for e in edges:
        e.render(screen)

    for v in vertices:
        v.render(screen)
    

vertices = []
edges = []
link = None
graph = Graph()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                for v in vertices:
                    if v.rect.collidepoint(pos):
                        v.dragged = True
                        break
            if event.button == 2 or event.button == 3:
                for v in vertices:
                    if v.rect.collidepoint(pos):
                        if link == None:
                            link = v
                        else:
                            edges.append(Edge(link, v))
                            graph.add_edge((link.value, v.value))
                            link = None
                        break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pos = pygame.mouse.get_pos()
                v = Vertex(((pos[0] - VERTEX_SIZE / 2), (pos[1] - VERTEX_SIZE / 2)))
                vertices.append(v)
                graph.add_vertex(v.id)
            if event.key == pygame.K_DELETE:
                for v in vertices:
                    if v.rect.collidepoint(pygame.mouse.get_pos()):
                        for e in edges:
                            if e.v0 == v or e.v1 == v:
                                edges.remove(e)
                        graph.remove_vertex(v.value)
                        vertices.remove(v)
            if event.key == pygame.K_INSERT:
                inpt_graph = Graph(ast.literal_eval(str(input("> "))))
                for v in inpt_graph.vertices():
                    vertices.append(Vertex((random.randrange(0, width), random.randrange(0, height)), v))
                for e in inpt_graph.edges():
                    v0, v1 = None, None
                    for v in vertices:
                        if v.value == int(e[0]): v0 = v
                        if v.value == int(e[1]): v1 = v
                    if v0 != None and v1 != None:
                        edges.append(Edge(v0, v1))
                graph.merge(inpt_graph)
            if event.key == pygame.K_p:
                print(graph)
        if event.type == pygame.MOUSEBUTTONUP:
            for i in vertices:
                i.dragged = False
    for v in vertices:
        if v.dragged:
            pos = pygame.mouse.get_pos()
            v.rect.x = pos[0] - (v.rect.width/2)
            v.rect.y = pos[1] - (v.rect.height/2)
            break

    font = pygame.font.SysFont(None, font_size)
    draw_window()
    pygame.display.update()

pygame.quit()

# test graphs:
# {1:[2], 2:[3], 3:[4,5,6,90], 4:[], 5:[], 6:[90, 64], 90:[1], 64:[], 7:[]}
# {1:[2], 2:[3,4], 3:[4], 4:[1]}