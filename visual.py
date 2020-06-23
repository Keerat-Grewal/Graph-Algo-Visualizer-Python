import pygame

# initialize game and create screen and caption
pygame.init()
# original size = (1000, 800)
screen = pygame.display.set_mode((1000, 800), 0, 32)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# SIZE[0] = WIDTH
# SIZE[1] = HEIGHT
SIZE = pygame.display.get_surface().get_size()
# for the five buttons
spacing = SIZE[0] // 5

pygame.display.set_caption("Graph Algorithm Visualizer")

class DropDownMenu:
    def __init__(self, pos, width, height, color, text_color, main_text, dropdowns):
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.main_text = main_text
        self.text_color = text_color
        self.dropdowns = dropdowns
        self.is_pushed = False

    def draw_dropdown(self):
        points = []
        point1 = (self.pos[0] + int((self.width // 5) * 4), int(self.height // 2.5))
        point2 = (self.pos[0] + (int((self.width // 5) * 4)) - 10, int(self.height // 2.5))
        point3 = (point2[0] + (point1[0] - point2[0]) // 2 , int(self.height // 2.5 + 10))

        points.append(point1)
        points.append(point2)
        points.append(point3)

        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.width, self.height), 0)
        pygame.draw.polygon(screen, (0, 0, 0), points)
        font = pygame.font.SysFont('comicsans', 25)
        text = font.render(self.main_text, 1, self.text_color)
        screen.blit(text, (self.pos[0] + (self.width // 2 - text.get_width() // 2),
                           self.pos[1] + (self.height // 2 - text.get_height() // 2)))


class Button:
    def __init__(self, x_pos, y_pos, width, height, color, text_color, text=""):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.is_pushed = False

    def draw_button(self):
        pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, self.text_color)
            screen.blit(text, (self.x_pos + (self.width // 2 - text.get_width() // 2),
                               self.y_pos + (self.height // 2 - text.get_height() // 2)))

    def is_covered(self, mouse_pos):
        if mouse_pos[0] > self.x_pos and mouse_pos[0] < self.x_pos + self.width:
            if mouse_pos[1] > self.y_pos and mouse_pos[1] < self.y_pos + self.height:
                return True
        return False

class Vertex:
    def __init__(self, pos, id):
        self.pos = pos
        self.color = (0, 153, 0)
        self.id = id
        self.is_pushed = False

    def draw_vertex(self):
        pygame.draw.circle(screen, (0, 0, 0), self.pos, 22)
        pygame.draw.circle(screen, self.color, self.pos, 20)

        font = pygame.font.SysFont('comicsans', 25)
        text = font.render(str(self.id), 1, (0, 0, 0))
        screen.blit(text, (self.pos[0] - 5, self.pos[1] - 8))

    def is_covered(self, mouse_pos):
        distance = ((mouse_pos[0] - self.pos[0]) ** 2 + (mouse_pos[1] - self.pos[1]) ** 2) ** 0.5
        print(distance)
        if distance < 22:
            return True
        return False


def draw_vertices(vertices):
    for i in vertices:
        i.draw_vertex()

def draw_button(buttons):
    for i in buttons:
        i.draw_button()

def draw_connections(connections):
    for i in range(0, len(connections) - 1, 2):
        pygame.draw.line(screen, (0, 0, 0), connections[i].pos, connections[i + 1].pos, 5)

def draw_dropdowns(dropdowns):
    for i in dropdowns:
        i.draw_dropdown()

def initial_screen():
    # this screen helps the user understand how to use the visualizer
    return

def main():
    visual_running = True
    button_list = []
    vertices_list = []
    graph_types = ["Undirected graph", "Directed graph", "Weighted graph"]
    dropdowns_list = []

    # all the buttons
    nav_button = Button(0, 0, SIZE[0], 55, (0, 0, 0), (255, 255, 255))
    vertex_button = Button(0, SIZE[1] - 55, spacing, 50, (242, 242, 242), (0, 0, 0), "Create Vertex")

    # all the dropdowns
    graph_dropdown = DropDownMenu((0, 0), spacing, 50, (31, 61, 122), (255, 255, 255),
                                  "Graphs", graph_types)
    tree_dropdown = DropDownMenu((graph_dropdown.pos[0] + spacing, 0), spacing, 50, (31, 61, 122), (255, 255, 255),
                                  "Trees", graph_types)
    algo_dropdown = DropDownMenu((tree_dropdown.pos[0] + spacing, 0), spacing, 50, (31, 61, 122), (255, 255, 255),
                                  "Algorithms", graph_types)
    clear_dropdown = DropDownMenu((algo_dropdown.pos[0] + spacing, 0), spacing, 50, (31, 61, 122), (255, 255, 255),
                                  "Clear Board", graph_types)
    speed_dropdown = DropDownMenu((clear_dropdown.pos[0] + spacing, 0), spacing, 50, (31, 61, 122), (255, 255, 255),
                                  "Speed", graph_types)

    # add all elemets to their appropriate list
    button_list.append(nav_button)
    button_list.append(vertex_button)

    dropdowns_list.append(graph_dropdown)
    dropdowns_list.append(tree_dropdown)
    dropdowns_list.append(algo_dropdown)
    dropdowns_list.append(clear_dropdown)
    dropdowns_list.append(speed_dropdown)

    vertex_id = 1
    connections = []

    while visual_running:
        screen.fill((242, 242, 242))

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                visual_running = False
                pygame.quit()
                quit()
                break

            # if user is hovering over mouse then change color
            if event.type == pygame.MOUSEMOTION:
                if vertex_button.is_covered(mouse_pos):
                    vertex_button.text_color = (0, 128, 128)
                else:
                    vertex_button.text_color = (0, 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if vertex_button.is_covered(mouse_pos):
                    vertex_button.is_pushed = True
                    print("Vertex button pushed")
                elif vertex_button.is_pushed:
                    print("Draw vertex")
                    if not vertex_button.is_covered(mouse_pos):
                        vertices_list.append(Vertex(mouse_pos, vertex_id))
                        vertex_id += 1
                        vertex_button.is_pushed = False
                    else:
                        print("Not valid vertex location")
                # check if any of the vertices on screen have been pushed and set is_pushed to True
                else:
                    for i in range(len(vertices_list)):
                        print("HERE")
                        if vertices_list[i].is_covered(mouse_pos):
                            vertices_list[i].is_pushed = True
                            connections.append(vertices_list[i])
                            break

        # make sure there is at least one connection before drawing
        if len(connections) > 1:
            draw_connections(connections)
        #print(connections)
        # draw button and update display
        draw_vertices(vertices_list)
        draw_button(button_list)
        draw_dropdowns(dropdowns_list)
        pygame.display.update()

if __name__ == '__main__':
    main()