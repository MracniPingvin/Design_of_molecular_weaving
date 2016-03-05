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

        self.node_map = self.generate_node_map()  # the coordinates of each node

        self.line_thickness = 5  # thickness of the connection lines
        self.circle_radius = 10  # radius of the node circles

    def draw(self):
        master = Tk()
        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.draw_node_map()
        mainloop()

    def create_circle(self, x, y, r, **kwargs):
        self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    def generate_node_map(self):
        if self.tessellation == "triangular":
            distance = self.canvas_width // (self.node_width + self.node_height * 0.5 + 1)
        elif self.tessellation == "rectangular":
            distance = self.canvas_height // (self.node_height + 1)

        node_map = []
        for i in range(self.node_height):
            for j in range(self.node_width):
                if self.tessellation == "triangular":
                    node_map.append([i * (distance // 2) + j * distance + distance,
                                     i * (distance * (3 ** (1/2))/2) + distance])
                elif self.tessellation == "rectangular":
                    node_map.append([distance + i * distance, distance + j * distance])
        return node_map

    def draw_node_map(self):
        count = 0
        for i in self.node_map:
            count += 1
            self.create_circle(i[0], i[1], self.circle_radius, fill="black")
            self.canvas.create_text(i[0]+25, i[1]-20, text=count, fill="black", font=("Purisa", 15))

    # def segment_draw_triangular(self, start_node):
    #     offset = self.line_thickness
    #     soffset = int(offset * 0.70)
    #     text_offset = 15
    #     for i in self.matrix[start_node[1]][start_node[0]]:
    #         count = 0
    #         letter = i.lower()
    #         if letter in self.alphabet_list[0]:
    #             if count == 0:
    #                 self.canvas.create_line(self.node_map[start_node][0] - soffset,
    #                                         self.node_map[start_node][1] - soffset,
    #                                         self.node_map[end_node][0] - soffset,
    #                                         self.node_map[end_node][1] - soffset,
    #                                         fill="#FF0000",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2 - text_offset,
    #                                         (self.node_map[start_node][1] + self.node_map[end_node][1]) // 2 - text_offset,
    #                                         text=letter,fill="#FF0000")
    #             elif count == 1:
    #                 self.canvas.create_line(self.node_map[start_node][0] - offset,
    #                                         self.node_map[start_node][1] + self.circle_radius,
    #                                         self.node_map[end_node][0] - offset,
    #                                         self.node_map[end_node][1] - offset,
    #                                         fill="#FF0000",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2 - text_offset,
    #                                         (self.node_map[start_node][1] + self.node_map[end_node][1]) // 2 - text_offset,
    #                                         text=letter,fill="#FF0000")
    #             elif count == 2:
    #                 self.canvas.create_line(self.node_map[start_node][0] + self.circle_radius,
    #                                         self.node_map[start_node][1] - offset,
    #                                         self.node_map[end_node][0] - offset,
    #                                         self.node_map[end_node][1] - offset,
    #                                         fill="#FF0000",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2,
    #                                         self.node_map[start_node][1] - text_offset,
    #                                         text=letter,fill="#FF0000")
    #
    #         elif letter in self.alphabet_list[1]:
    #             if count == 0:
    #                 self.canvas.create_line(self.node_map[start_node][0] + soffset,
    #                                         self.node_map[start_node][1] + soffset,
    #                                         self.node_map[end_node][0] + soffset,
    #                                         self.node_map[end_node][1] + soffset,
    #                                         fill="#00FF00",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2 + text_offset,
    #                                         (self.node_map[start_node][1] + self.node_map[end_node][1]) // 2 + text_offset,
    #                                         text=letter,fill="#00FF00")
    #             elif count == 1:
    #                 self.canvas.create_line(self.node_map[start_node][0] + offset,
    #                                         self.node_map[start_node][1] + self.circle_radius,
    #                                         self.node_map[end_node][0] + offset,
    #                                         self.node_map[end_node][1] + offset,
    #                                         fill="#00FF00",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2 + text_offset,
    #                                         (self.node_map[start_node][1] + self.node_map[end_node][1]) // 2 + text_offset,
    #                                         text=letter,fill="#00FF00")
    #             elif count == 2:
    #                 self.canvas.create_line(self.node_map[start_node][0] + self.circle_radius,
    #                                         self.node_map[start_node][1] + offset,
    #                                         self.node_map[end_node][0] + offset,
    #                                         self.node_map[end_node][1] + offset,
    #                                         fill="#00FF00",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2,
    #                                             self.node_map[start_node][1] + text_offset,
    #                                             text=letter,fill="#00FF00")
    #
    #         elif letter in self.alphabet_list[2]:
    #             elif count == 0:
    #                 self.canvas.create_line(self.node_map[start_node][0] - int(self.circle_radius*0.707),
    #                                         self.node_map[start_node][1] + int(self.circle_radius*0.707),
    #                                         self.node_map[end_node][0],
    #                                         self.node_map[end_node][1],
    #                                         fill="#0000FF",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2 + text_offset,
    #                                         (self.node_map[start_node][1] + self.node_map[end_node][1]) // 2 + text_offset + 15,
    #                                         text=letter,fill="#0000FF")
    #             elif count == 1:
    #                 self.canvas.create_line(self.node_map[start_node][0],
    #                                         self.node_map[start_node][1] + self.circle_radius,
    #                                         self.node_map[end_node][0],
    #                                         self.node_map[end_node][1],
    #                                         fill="#0000FF",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2 + text_offset,
    #                                         (self.node_map[start_node][1] + self.node_map[end_node][1]) // 2 + text_offset + 15,
    #                                         text=letter,fill="#0000FF")
    #             elif count == 2:
    #                 self.canvas.create_line(self.node_map[start_node][0] + self.circle_radius,
    #                                         self.node_map[start_node][1],
    #                                         self.node_map[end_node][0],
    #                                         self.node_map[end_node][1],
    #                                         fill="#0000FF",width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2 + 15,
    #                                         self.node_map[start_node][1] + text_offset,
    #                                         text=letter,fill="#0000FF")
    #         count += 1
    #
    # def connect_nodes_squared(self, start_node):
    #     offset = self.line_thickness
    #     text_offset = 15
    #
    #     for i in self.matrix[start_node[1]][start_node[0]]:
    #         count = 0
    #         letter = i.lower()
    #         if letter in self.alphabet_list[0]:
    #             if count == 0:
    #                 self.canvas.create_line(self.node_map[start_node][0] - offset,
    #                                         self.node_map[start_node][1] + self.circle_radius,
    #                                         self.node_map[end_node][0] - offset,
    #                                         self.node_map[end_node][1] - offset,
    #                                         fill="#FF0000", width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2,
    #                                     self.node_map[start_node][1] - text_offset,
    #                                     text=letter, fill="#FF0000")
    #             elif count == 1:
    #                 self.canvas.create_line(self.node_map[start_node][0] + self.circle_radius,
    #                                         self.node_map[start_node][1] - offset,
    #                                         self.node_map[end_node][0] - offset,
    #                                         self.node_map[end_node][1] - offset,
    #                                         fill="#FF0000", width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2,
    #                                         self.node_map[start_node][1] - text_offset,
    #                                         text=letter, fill="#FF0000")
    #         elif letter in self.alphabet_list[1]:
    #             if count == 0:
    #                 self.canvas.create_line(self.node_map[start_node][0] + offset,
    #                                         self.node_map[start_node][1] + self.circle_radius,
    #                                         self.node_map[end_node][0] + offset,
    #                                         self.node_map[end_node][1] + offset,
    #                                         fill="#00FF00", width=5)
    #                 self.canvas.create_text(self.node_map[start_node][0] + text_offset,
    #                                         (self.node_map[start_node][1] + self.node_map[end_node][1]) // 2,
    #                                         text=letter, fill="#00FF00")
    #
    #             elif count == 1:
    #                 self.canvas.create_line(self.node_map[start_node][0] + self.circle_radius,
    #                                         self.node_map[start_node][1] + offset,
    #                                         self.node_map[end_node][0] + offset,
    #                                         self.node_map[end_node][1] + offset,
    #                                         fill="#00FF00", width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2,
    #                                         self.node_map[start_node][1] + text_offset,
    #                                         text=letter, fill="#00FF00")
    #
    #         elif letter in self.alphabet_list[2]:
    #             if count == 0:
    #                 self.canvas.create_line(self.node_map[start_node][0],
    #                                         self.node_map[start_node][1] + self.circle_radius,
    #                                         self.node_map[end_node][0],
    #                                         self.node_map[end_node][1],
    #                                         fill="#0000FF", width=5)
    #                 self.canvas.create_text(self.node_map[start_node][0] + text_offset,
    #                                         (self.node_map[start_node][1] + self.node_map[end_node][1]) // 2 + 15,
    #                                         text=letter, fill="#0000FF")
    #             elif count == 1:
    #                 self.canvas.create_line(self.node_map[start_node][0] + self.circle_radius,
    #                                         self.node_map[start_node][1],
    #                                         self.node_map[end_node][0],
    #                                         self.node_map[end_node][1],
    #                                         fill="#0000FF", width=5)
    #                 self.canvas.create_text((self.node_map[start_node][0] + self.node_map[end_node][0]) // 2 + 15,
    #                                         self.node_map[start_node][1] + text_offset,
    #                                         text=letter, fill="#0000FF")
    #
