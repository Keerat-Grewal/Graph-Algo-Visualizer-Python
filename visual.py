import pygame

# initialize game and create screen and caption
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Graph Algorithm Visualizer")


class Button:
    def __init__(self, x_pos, y_pos, width, height, color, text=""):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.is_pushed = False

    def draw_button(self):
        pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (0, 0, 0))
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
        self.color = (255, 255, 255)
        self.id = id

    def draw_vertex(self):
        pygame.draw.circle(screen, (0, 0, 0), self.pos, 22)
        pygame.draw.circle(screen, self.color, self.pos, 20)

        font = pygame.font.SysFont('comicsans', 25)
        text = font.render(str(self.id), 1, (0, 0, 0))
        screen.blit(text, (self.pos[0] - 5, self.pos[1] - 8))

    def is_covered(self, mouse_pos):
        distance = ((mouse_pos[0] - self.pos[0]) ** 2 + (mouse_pos[1] - self.pos[1]) ** 2) ** 0.5
        if distance < 22:
            return True
        return False


def draw_vertices(vertices):
    for i in vertices:
        i.draw_vertex()

def draw_button(buttons):
    for i in buttons:
        i.draw_button()

def main():
    visual_running = True
    button_list = []
    vertices_list = []
    vertex_button = Button(5, 5, 200, 50, (255, 153, 102), "Create Vertex")
    button_list.append(vertex_button)
    id = 1

    while visual_running:
        screen.fill((0, 34, 102))

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
                    vertex_button.color = (255, 238, 230)
                else:
                    vertex_button.color = (255, 153, 102)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if vertex_button.is_pushed:
                    print("Draw vertex")
                    if mouse_pos[1] > vertex_button.y_pos + vertex_button.height:
                        vertices_list.append(Vertex(mouse_pos, id))
                        id += 1
                        vertex_button.is_pushed = False
                    else:
                        print("Not valid vertex location")
                if vertex_button.is_covered(mouse_pos):
                    vertex_button.is_pushed = True
                    print("Vertex button pushed")

        # draw button and update display
        draw_vertices(vertices_list)
        draw_button(button_list)
        pygame.display.update()


main()