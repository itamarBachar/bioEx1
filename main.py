import pygame
import random
from utils import check_input


def show_menu():
    pygame.init()

    # Set up the screen
    screen_width = 700
    screen_height = 750
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Spreading rumours")

    # Set up fonts
    title_font = pygame.font.SysFont('Arial', 50)
    label_font = pygame.font.SysFont('Arial', 30)

    # set up input boxes
    input_boxes = [
        pygame.Rect(220, 150 + i * 100, 300, 50)
        for i in range(6)
    ]
    input_texts = [""] * len(input_boxes)

    # Set up button
    button_rect = pygame.Rect(550, 680, 100, 50)
    button_color = (255, 255, 255)
    button_text = label_font.render("Play", True, (0, 0, 0))
    button_text_rect = button_text.get_rect(center=button_rect.center)

    # define last click as the position of the mouse when the mouse button is released
    last_click = None
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # If the user enter a key, add it to the input text of the current input box
                # check which input box is currently selected
                for i, box in enumerate(input_boxes):
                    if box.collidepoint(last_click):
                        # if the user press enter, move to the next input box
                        if event.key == pygame.K_RETURN:
                            input_boxes[i] = False
                            if i < len(input_boxes) - 1:
                                input_boxes[i + 1] = True
                        # if the user press backspace, remove the last character
                        elif event.key == pygame.K_BACKSPACE:
                            input_texts[i] = input_texts[i][:-1]
                        else:
                            input_texts[i] += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if left mouse button was clicked
                    last_click = event.pos
                    if button_rect.collidepoint(event.pos):
                        running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw title
        title_text = title_font.render("Welcome to Spreading Rumours", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, 100))
        screen.blit(title_text, title_rect)

        # Draw input boxes and labels
        for i, box in enumerate(input_boxes):
            # if it the first input box is text is p and not s
            if i == 0:
                label_text = label_font.render(f"Enter P value:", True, (255, 255, 255))
            elif i == 1:
                label_text = label_font.render(f"Enter L value:", True, (255, 255, 255))
            else:
                label_text = label_font.render(f"Enter S{i - 1} value:", True, (255, 255, 255))
            label_rect = label_text.get_rect(center=(120, 170 + i * 100))
            screen.blit(label_text, label_rect)
            pygame.draw.rect(screen, (255, 255, 255), box, 2)
            input_surface = label_font.render(input_texts[i], True, (255, 255, 255))
            screen.blit(input_surface, (box.x + 5, box.y + 5))

        # Draw button
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(button_text, button_text_rect)

        # Update the display
        pygame.display.flip()
        # print the
    # Quit Pygame
    pygame.quit()
    flag = check_input(input_texts)
    return flag, input_texts



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
    def __init__(self, is_person, cell_type, x, y, l):
        self.is_person = is_person
        self.cell_type = cell_type
        self.x = x
        self.y = y
        self.rumor = 0
        self.l = l
        self.wait = 0

    def draw(self, surface, x, y, cell_size):
        if (self.rumor == 0):
            color = (0, 0, 0)

        else:
            color = (255, 255, 255)
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(surface, color, rect)

    def forward(self):
        if self.rumor > 0:
            chance = (1 / self.cell_type) * self.rumor


def startGame(p_person, p_s1, p_s2, p_s3, p_s4, l):
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Rumours spreading")
    # Create the grid
    grid = []
    for i in range(grid_width):
        row = []
        for j in range(grid_height):
            if random.random() < p_person:
                is_person = True
                cell_type = random.choices([S1, S2, S3, S4], [p_s1, p_s2, p_s3, p_s4])[0]
            else:
                is_person = False
                cell_type = None
            cell = Cell(is_person, cell_type, i, j, l)
            row.append(cell)
        grid.append(row)
    show_grid(grid)


def show_grid(grid):
    screen = pygame.display.set_mode(window_size)
    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the window
        screen.fill((255, 255, 255))
        # Draw the grid
        for i in range(grid_width):
            for j in range(grid_height):
                x = i * (cell_size + line_thickness) + line_thickness
                y = j * (cell_size + line_thickness) + line_thickness
                cell = grid[i][j]
                cell.draw(screen, x, y, cell_size)
        # Draw the borders
        for i in range(grid_width + 1):
            x = i * (cell_size + line_thickness)
            pygame.draw.line(screen, line_color, (x, 0), (x, window_size[1]), line_thickness)
        for j in range(grid_height + 1):
            y = j * (cell_size + line_thickness)
            pygame.draw.line(screen, line_color, (0, y), (window_size[0], y), line_thickness)

            # Update the display
        pygame.display.flip()

        # Quit Pygame
    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startGame(0.5, 0.2, 0.3, 0.2, 0.3, 2)
