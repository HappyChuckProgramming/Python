import pygame, random, sys

class Node:

    def __init__(self, row, col, size):
        self.m_row = row
        self.m_col = col
        self.m_walls = {}  #walls are inner walls
        self.m_size = size
        self.x = self.m_size*self.m_col + self.m_size  # x, y is topleft corner of node
        self.y = self.m_size*self.m_row + self.m_size

    def disconnect(self, node, flag=True):  #disconnect means break wall
        #self.m_walls.pop(which_one)
        for key,value in self.m_walls.items():
            if  value != None and value.m_row== node.m_row and value.m_col== node.m_col:
                self.m_walls[key] = None
            else:
                #print("node to disconnect not found")
                pass
        if flag:
            node.disconnect(self, False)


    def connections(self):
        m_list = []
        for key,value in self.m_walls.items():
            if value != None:
                m_list.append(key)
        return m_list

    def draw(self, screen, y_offset):
        if self.m_walls["north"] != None:
            start_pos = (self.x, self.y + y_offset)
            end_pos =   (self.x + self.m_size, self.y +y_offset)
            pygame.draw.line(screen, (0,0,0), start_pos, end_pos, 1)

        if self.m_walls["south"] != None:
            start_pos = (self.x, self.y + self.m_size + y_offset)
            end_pos =   (self.x + self.m_size, self.y + self.m_size + y_offset)
            pygame.draw.line(screen, (0,0,0), start_pos, end_pos, 1)

        if self.m_walls["west"] != None:
            start_pos = (self.x, self.y + y_offset)
            end_pos = (self.x, self.y + self.m_size + y_offset)
            pygame.draw.line(screen, (0,0,0), start_pos, end_pos, 1)

        if self.m_walls["east"] != None:
            start_pos = (self.x + self.m_size, self.y + y_offset)
            end_pos = (self.x + self.m_size, self.y + self.m_size + y_offset)
            pygame.draw.line(screen, (0,0,0), start_pos, end_pos, 1)



class Maze:

    def __init__(self, num_rows, num_cols, node_size):
        self.m_num_rows = num_rows
        self.m_num_cols = num_cols
        self.m_node_size = node_size
        self.m_nodes = [ [Node(i, j, self.m_node_size) for j in range(self.m_num_cols)] for i in range(self.m_num_rows) ]


    def connect_nodes_default(self):
        for node in self.iter_node():
            node.m_walls["north"]= self.get_node(node.m_row-1, node.m_col)
            node.m_walls["south"]= self.get_node(node.m_row+1, node.m_col)
            node.m_walls["west"]= self.get_node(node.m_row, node.m_col-1)
            node.m_walls["east"]= self.get_node(node.m_row, node.m_col+1)

    def iter_node(self):
        for i in range(self.m_num_rows):
            for j in range(self.m_num_cols):
                yield self.m_nodes[i][j]

    def get_node(self, row, col):
        if row >= 0 and row < self.m_num_rows \
                and col >= 0 and col < self.m_num_cols:
            return self.m_nodes[row][col]
        else:
            return None

    def printme(self):
        for node in self.iter_node():
            print(node.m_row, node.m_col, node.connections())

    def draw(self, screen, y_offset = 0):
        self.draw_outer_boundary(screen, y_offset)
        for node in self.iter_node():
            node.draw(screen, y_offset)

    def draw_outer_boundary(self, screen, y_offset):
        topleft = (self.m_node_size,self.m_node_size+y_offset)
        topright = (self.m_node_size+self.m_node_size*self.m_num_cols, self.m_node_size+y_offset)
        bottomleft = (self.m_node_size, self.m_node_size+self.m_node_size*self.m_num_rows + y_offset)
        bottomright=(self.m_node_size+self.m_node_size*self.m_num_cols,self.m_node_size+self.m_node_size*self.m_num_rows + y_offset)

        pygame.draw.line(screen, (0,0,0), topleft, topright, 5)
        pygame.draw.line(screen, (0,0,0), topleft, bottomleft, 5)
        pygame.draw.line(screen, (0,0,0), topright, bottomright, 5)
        pygame.draw.line(screen, (0,0,0), bottomleft, bottomright, 5)

    def make_maze(self):
        for node in self.iter_node():
            node_to_disconnect_north= self.get_node(node.m_row-1, node.m_col) #north
            node_to_disconnect_east= self.get_node(node.m_row, node.m_col+1) #east

            if node_to_disconnect_north== None and node_to_disconnect_east==None:
                node_to_disconnect = None
            elif node_to_disconnect_north != None and node_to_disconnect_east==None:
                node_to_disconnect= node_to_disconnect_north
            elif node_to_disconnect_north == None and node_to_disconnect_east!=None:
                node_to_disconnect= node_to_disconnect_east
            else:
                rand_num = random.randint(0,1)
                if rand_num:
                    node_to_disconnect = node_to_disconnect_north
                else:
                    node_to_disconnect = node_to_disconnect_east
            if node_to_disconnect != None:
                #print('curr node:', node.m_row, node.m_col)
                #print('disconnecting:', node_to_disconnect.m_row, node_to_disconnect.m_col)
                node.disconnect(node_to_disconnect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((900,900), 0, 32)
    screen.fill((255,255,255))

    num_rows = 30
    num_cols = 30
    node_size = 26
    maze = Maze(num_rows, num_cols, node_size)
    maze.connect_nodes_default()
    #maze.printme()
    #maze.draw(screen)

    maze.make_maze()
    #maze.printme()
    #maze.draw(screen, num_rows*node_size +100)
    maze.draw(screen, node_size)
    
    running = True
    held_down = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                held_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                held_down = False
            elif event.type == pygame.MOUSEMOTION:
                if held_down:
                    pygame.draw.circle(screen, (250,20,50), event.pos, 5, 0)
        pygame.display.update()

    pygame.quit()
    sys.exit()

#client code
main()
