import pygame
from matplotlib import pyplot as plt


def check_input(input_text):
    for i in input_text:
        # cast the input to float and check if it is a number\
        try:
            float(i)
        except ValueError:
            return False
    # check if the first input is a number and is not between 0 and 1
    if float(input_text[0]) < 0 or float(input_text[0]) > 1:
        return False
    # go over for 2 to 5 and check if there sum is 1
    if sum([float(input_text[i]) for i in range(2, 6)]) != 1:
        return False
    return True


# define const values
S1 = 1
S2 = 2
S3 = 3
S4 = 4
COLORS = {
    S1: (255, 255, 255),
    S2: (0, 0, 255),
    S3: (0, 255, 0),
    S4: (255, 0, 0),
    None: (0, 0, 0)
}
grid_width = 100
grid_height = 100
window_width = 700
window_height = 700
line_thickness = 1
window_size = (window_width + (grid_width + 1) * line_thickness, window_height + (grid_height + 1) * line_thickness)
line_color = (128, 128, 128)
cell_size = 7


class Cell:
    def _init_(self, is_person, cell_type, x, y, l):
        self.is_person = is_person
        self.cell_type = cell_type
        self.x = x
        self.y = y
        self.rumor = 0
        self.l = l
        self.wait = 0

    def draw(self, surface, x, y, cell_size):
        if self.rumor == 0:
            color = (0, 0, 0)

        else:
            color = (255, 255, 255)
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(surface, color, rect)

    def forward(self):
        if self.rumor > 0:
            chance = (1 / self.cell_type) * self.rumor


def plot_results(lst_person, input_text):
    # average the number of people exposed to the rumor
    for i in range(0, len(lst_person)):
        lst_person[i] = lst_person[i] / 10
    # plot the graph of the number of people exposed to the rumor
    plt.ylabel('percent of people exposed to the rumor')
    plt.xlabel('number of iteration')
    plt.plot(lst_person)
    # put the values p and l and s1 s2 s3 s4 in the graph title and the legend
    plt.title(
        f"p={input_text[0]}, l={input_text[1]}, s1={input_text[2]}, s2={input_text[3]}, s3={input_text[4]}, s4={input_text[5]}")
    # save the graph
    plt.savefig('graph5.png')
