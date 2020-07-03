import pygame
from time import sleep, time

class Graph:

    def __init__(self, connections, dropdowns_list, algo, vertices_list, button_list, directed=False):

        self.adjacency_list = {}
        self.connections = connections
        self.is_bipartite = True
        self.dropdowns_list = dropdowns_list
        self.algo = algo
        self.vertices_list = vertices_list
        self.button_list = button_list

        if not directed:
            for i in range(0, len(connections) - 1, 2):
                self.add_vertex(connections[i])
                self.add_vertex(connections[i + 1])
                self.add_edge(connections[i].id, connections[i + 1].id)

    def __repr__(self):
        string = ""
        for i in self.adjacency_list:
            string += str(i) + " -> "
            string += str(self.adjacency_list[i])
            string += "\n"
        return string

    def add_vertex(self, vertex):
        if vertex.id not in self.adjacency_list:
            self.adjacency_list[vertex.id] = vertex

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].adjacent_to.add(self.adjacency_list[v2])
        self.adjacency_list[v2].adjacent_to.add(self.adjacency_list[v1])

    def get_vertices(self):
        keys = []
        for i in self.adjacency_list:
            keys.append(i)
        keys.sort()
        return list(keys)

    def depth_first_search(self):

        self.reset_visited()
        all_vertices = self.get_vertices()

        components = []

        for i in range(len(all_vertices)):
            if not self.adjacency_list[all_vertices[i]].visited:
                new_component = [all_vertices[i]]
                #self.adjacency_list[all_vertices[i]].color = (255, 0, 0)
                self.adjacency_list[all_vertices[i]].b_color = "b"
                new_component += self.explore(all_vertices[i])
                components.append(sorted(new_component))
        return components

    def explore(self, v):
        # update_screen function needed here
        from visual import update_screen

        component = []
        self.adjacency_list[v].visited = True
        curr_vertex = self.adjacency_list[v]
        curr_vertex.color = (255, 0, 0)
        update_screen(self.connections, self.dropdowns_list, self.algo, self.vertices_list, self.button_list)
        pygame.display.update()
        pygame.time.delay(1000)

        if self.adjacency_list[v].b_color == "b":
            color = "g"
        else:
            color = "b"

        for i in curr_vertex.adjacent_to:
            if not i.visited:
                i.b_color = color
                component.append(i.id)
                component += self.explore(i.id)
            elif i.b_color == curr_vertex.b_color:
                self.is_bipartite = False
        return component

    def reset_visited(self):
        for i in self.adjacency_list:
            self.adjacency_list[i].visited = False
