from tkinter import *


class LatticeDraw(object):
    def __init__(self, matrix, pixel_size, tessellation, alphabet_list):

        self.matrix = matrix  # graph to be drawn
        self.tessellation = tessellation
        self.alphabet_list = alphabet_list

        self.canvas_width = pixel_size[0]
        self.canvas_height = pixel_size[1]
        self.node_width = len(matrix[0])
        self.node_height = len(matrix)

        self.node_map = self.generate_node_map(0)
        self.node_maps = [self.generate_node_map(-5), self.generate_node_map(0), self.generate_node_map(5)]   # the coordinates of each node

        self.line_thickness = 5  # thickness of the connection lines
        self.circle_radius = 10  # radius of the node circles

        self.offset_list = [-self.line_thickness, 0, self.line_thickness]
        self.text_offset_list = [-15, 0, 15]
        self.color_list = ["#FF0000", "#00FF00", "#0000FF"]
        self.text_space = 15
    def draw(self):
        master = Tk()
        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.draw_node_map()
        if self.tessellation == "rectangular":
            self.segment_draw_rectangular()
        if self.tessellation == "triangular":
            self.segment_draw_triangular()
        mainloop()

    def create_circle(self, x, y, r, **kwargs):
        self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    def generate_node_map(self, offset):
        if self.tessellation == "triangular":
            distance = self.canvas_width // (self.node_width + self.node_height * 0.5 + 1)
        elif self.tessellation == "rectangular":
            distance = self.canvas_height // (self.node_height + 1)

        node_map = []
        for i in range(self.node_height):
            node_map.append([])
            for j in range(self.node_width):
                if self.tessellation == "triangular":
                    node_map[i].append([i * (distance // 2) + j * distance + distance + offset,
                                        i * (distance * (3 ** (1/2))/2) + distance])
                elif self.tessellation == "rectangular":
                    node_map[i].append([distance + j * distance,distance + i * distance])
        return node_map

    def draw_node_map(self):
        count = 0
        for i in self.node_map:
            for j in i:
                count += 1
                self.create_circle(j[0], j[1], self.circle_radius, fill="black")
                self.canvas.create_text(j[0]+25, j[1]-20, text=count, fill="black", font=("Purisa", 15))

    def segment_draw_rectangular(self):
        distance = self.canvas_height // (self.node_height + 1)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[1])):
                for k in range(2):
                    for l in range(len(self.matrix[i][j][k])):
                        if k == 0:
                            self.canvas.create_line(self.node_map[i][j][0] + self.offset_list[l],
                                                    self.node_map[i][j][1] + self.offset_list[l],
                                                    self.node_map[i][j][0] + self.offset_list[l],
                                                    self.node_map[i][j][1] + distance + self.offset_list[l],
                                                    fill=self.color_list[l], width=self.line_thickness)
                            self.canvas.create_text(self.node_map[i][j][0] + self.text_space,
                                                    (2*self.node_map[i][j][1] + distance) // 2 + self.text_offset_list[l],
                                                    text=self.matrix[i][j][k][l],
                                                    fill=self.color_list[l],
                                                    font=("Purisa", 15))
                        elif k == 1:
                            self.canvas.create_line(self.node_map[i][j][0] + self.offset_list[l],
                                                    self.node_map[i][j][1] + self.offset_list[l],
                                                    self.node_map[i][j][0] + distance + self.offset_list[l],
                                                    self.node_map[i][j][1] + self.offset_list[l],
                                                    fill=self.color_list[l], width=self.line_thickness)
                            self.canvas.create_text((2*self.node_map[i][j][0] + distance) // 2 + self.text_offset_list[l],
                                                    self.node_map[i][j][1] + self.text_space,
                                                    text=self.matrix[i][j][k][l],
                                                    fill=self.color_list[l],
                                                    font=("Purisa", 15))
    def segment_draw_triangular(self):
        distance = self.canvas_width // (self.node_width + self.node_height * 0.5 + 1)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[1])):
                for k in range(3):
                    for l in range(len(self.matrix[i][j][k])):
                        if k == 0:
                            self.canvas.create_line(self.node_maps[l][i][j][0],
                                                    self.node_maps[l][i][j][1],
                                                    self.node_maps[l][i][j][0] - distance//2,
                                                    self.node_maps[l][i][j][1] + distance * (3 ** (1/2))/2,
                                                    fill=self.color_list[l], width=self.line_thickness)
                            self.canvas.create_text((2*self.node_maps[l][i][j][0] - distance//2) // 2 - self.text_offset_list[l] - self.text_offset_list[2],
                                                    (2*self.node_maps[l][i][j][1] + distance * (3 ** (1/2))/2) // 2 + self.text_offset_list[l],
                                                    text=self.matrix[i][j][k][l],
                                                    fill=self.color_list[l],
                                                    font=("Purisa", 15))
                        elif k == 1:
                            self.canvas.create_line(self.node_maps[l][i][j][0],
                                                    self.node_maps[l][i][j][1],
                                                    self.node_maps[l][i][j][0] + distance//2,
                                                    self.node_maps[l][i][j][1] + distance * (3 ** (1/2))/2,
                                                    fill=self.color_list[l], width=self.line_thickness)
                            self.canvas.create_text((2*self.node_maps[l][i][j][0] + distance//2) // 2 + self.text_offset_list[l]//3.8 - self.text_offset_list[2],
                                                    (2*self.node_maps[l][i][j][1] + distance * (3 ** (1/2))/2) // 2 + self.text_offset_list[l],
                                                    text=self.matrix[i][j][k][l],
                                                    fill=self.color_list[l],
                                                    font=("Purisa", 15))
                        elif k == 2:
                            self.canvas.create_line(self.node_maps[l][i][j][0],
                                                    self.node_maps[l][i][j][1] + self.offset_list[l],
                                                    self.node_maps[l][i][j][0] + distance,
                                                    self.node_maps[l][i][j][1] + self.offset_list[l],
                                                    fill=self.color_list[l], width=self.line_thickness)
                            self.canvas.create_text((2*self.node_map[i][j][0] + distance) // 2 + self.text_offset_list[l],
                                                    self.node_maps[l][i][j][1] + self.text_space,
                                                    text=self.matrix[i][j][k][l],
                                                    fill=self.color_list[l],
                                                    font=("Purisa", 15))
