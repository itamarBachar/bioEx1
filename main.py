import time
import random

import pygame
from utils import check_input, distance


###
#
#
#  explanation of how to run appear in the report !
#
#
#
###


def show_menu():
    pygame.init()

    # Set up the screen
    screen_width = 680
    screen_height = 770
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
    radio_button1_selected = True
    radio_button2_selected = False
    radio_button3_selected = False
    radio_button_size = 20
    radio_button_spacing = 50
    radio_button1_pos = (570, 520)
    radio_button2_pos = (570, 520 + radio_button_spacing)
    radio_button3_pos = (570, 520 + radio_button_spacing + radio_button_spacing)
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
                return
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
                    mouse_pos = pygame.mouse.get_pos()
                    if distance(mouse_pos, radio_button1_pos) < radio_button_size:
                        radio_button1_selected = True
                        radio_button2_selected = False
                        radio_button3_selected = False
                    elif distance(mouse_pos, radio_button2_pos) < radio_button_size:
                        radio_button1_selected = False
                        radio_button2_selected = True
                        radio_button3_selected = False
                    elif distance(mouse_pos, radio_button3_pos) < radio_button_size:
                        radio_button1_selected = False
                        radio_button2_selected = False
                        radio_button3_selected = True
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw title
        title_text = title_font.render("Welcome to Spreading Rumours", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, 100))
        screen.blit(title_text, title_rect)

        # Draw radio button 1
        pygame.draw.circle(screen, (255, 255, 255), radio_button1_pos, radio_button_size)
        if radio_button1_selected:
            pygame.draw.circle(screen, (255, 0, 0), radio_button1_pos, radio_button_size - 4)

        # Draw radio button 1 label
        label_font = pygame.font.SysFont('Arial', 20)
        label_text = label_font.render('Option 1', True, (255, 255, 255))
        label_rect = label_text.get_rect()
        label_rect.center = (radio_button1_pos[0] + radio_button_size + 40, radio_button1_pos[1])
        screen.blit(label_text, label_rect)

        # Draw radio button 2
        pygame.draw.circle(screen, (255, 255, 255), radio_button2_pos, radio_button_size)
        if radio_button2_selected:
            pygame.draw.circle(screen, (255, 0, 0), radio_button2_pos, radio_button_size - 4)

        # Draw radio button 2 label
        label_text = label_font.render('Option 2a', True, (255, 255, 255))
        label_rect = label_text.get_rect()
        label_rect.center = (radio_button2_pos[0] + radio_button_size + 40, radio_button2_pos[1])
        screen.blit(label_text, label_rect)

        pygame.draw.circle(screen, (255, 255, 255), radio_button3_pos, radio_button_size)
        if radio_button3_selected:
            pygame.draw.circle(screen, (255, 0, 0), radio_button3_pos, radio_button_size - 4)

        label_text = label_font.render('Option 2b', True, (255, 255, 255))
        label_rect = label_text.get_rect()
        label_rect.center = (radio_button3_pos[0] + radio_button_size + 40, radio_button3_pos[1])
        screen.blit(label_text, label_rect)

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

    try:
        flag = check_input(input_texts)
        if flag:
            if radio_button1_selected:
                startGame(float(input_texts[0]),
                          float(input_texts[1]),
                          float(input_texts[2]),
                          float(input_texts[3]),
                          float(input_texts[4]),
                          float(input_texts[5]))
            elif radio_button2_selected:
                B_Game(float(input_texts[0]),
                       float(input_texts[1]),
                       float(input_texts[2]),
                       float(input_texts[3]),
                       float(input_texts[4]),
                       float(input_texts[5]))
            elif radio_button3_selected:
                D_Game(float(input_texts[0]),
                       float(input_texts[1]),
                       float(input_texts[2]),
                       float(input_texts[3]),
                       float(input_texts[4]),
                       float(input_texts[5]))
        else:
            if radio_button1_selected:
                lst1, lst2 = startGame(0.55, 100, 0.02, 0.03, 0.25, 0.7)
            elif radio_button2_selected:
                B_Game(0.7, 10, 0.1, 0.2, 0.2, 0.5)
            elif radio_button3_selected:
                lst1, lst2 = D_Game(0.5, 100, 0.1, 0.1, 0.1, 0.7)
    except ValueError:
        if radio_button1_selected:
            lst1, lst2 = startGame(0.55, 100, 0.02, 0.03, 0.25, 0.7)
        elif radio_button2_selected:
            B_Game(0.7, 10, 0.1, 0.2, 0.2, 0.5)
        elif radio_button3_selected:
            D_Game(0.83, 100, 0.1, 0.25, 0.2, 0.45)


# define const values
S1 = 0
S2 = 1
S3 = 2
S4 = 3
rumour_chance = [1, 2 / 3, 1 / 3, 0]
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
    def __init__(self, is_person, cell_type, x, y, length_of_wait):
        self.is_person = is_person
        self.cell_type = cell_type
        self.x = x
        self.y = y
        self.rumor = 0
        self.length_of_wait = 0
        self.spread_rumor = 0

    def draw(self, surface, x, y, cell_size):
        if not self.is_person:
            color = (0, 0, 0)
        elif self.rumor == 0:
            color = (255, 0, 0)
        else:
            color = (255, 255, 255)

        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(surface, color, rect)

    def chance_spread(self):
        if not self.is_person:
            return 0
        if self.spread_rumor == 0:
            return 0
        if self.spread_rumor == 1:
            return rumour_chance[self.cell_type]
        if self.spread_rumor == 2:
            if self.cell_type == 0:
                return 1
            else:
                return rumour_chance[self.cell_type - 1]
        if self.spread_rumor == 3:
            if self.cell_type == 0 or self.cell_type == 1:
                return 1
            else:
                return rumour_chance[self.cell_type - 2]
        if self.spread_rumor == 4:
            if self.cell_type == 0 or self.cell_type == 1 or self.cell_type == 2:
                return 1
            else:
                return rumour_chance[self.cell_type - 3]
        if self.spread_rumor >= 5:
            return 1


def opening_screen(p_person, length_of_wait, p_s1, p_s2, p_s3, p_s4):
    # Initialize Pygame
    pygame.init()

    # Set up the window
    window_size = (700, 750)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Countdown")

    # Set up font
    font = pygame.font.SysFont('Arial', 30)
    font2 = pygame.font.SysFont('Arial', 60)

    # Define variables
    heading = font2.render("Spreading Rumours in:  ", True, (255, 255, 255))
    p_person = "p - person: " + str(p_person)
    length_of_wait = "L is:  " + str(length_of_wait)
    p_s1 = "p_s1: " + str(p_s1)
    p_s2 = "p_s2: " + str(p_s2)
    p_s3 = "p_s3: " + str(p_s3)
    p_s4 = "p_s4: " + str(p_s4)

    # Define countdown function
    def countdown():
        for i in range(5, 0, -1):
            # Clear the screen
            screen.fill((0, 0, 0))
            # Draw title
            screen.blit(heading, (20, 20))
            # Display the countdown
            text = font2.render(str(i), True, (255, 0, 0))
            text_rect = text.get_rect(center=(580, 55))
            screen.blit(text, text_rect)

            # Display other variables
            p_person_text = font.render(p_person, True, (255, 255, 255))
            p_person_rect = p_person_text.get_rect(center=(window_size[0] / 2, window_size[1] / 4))
            screen.blit(p_person_text, p_person_rect)

            length_of_wait_text = font.render(str(length_of_wait), True, (255, 255, 255))
            length_of_wait_rect = length_of_wait_text.get_rect(center=(window_size[0] / 2, window_size[1] / 4 + 100))
            screen.blit(length_of_wait_text, length_of_wait_rect)

            p_s1_text = font.render(p_s1, True, (255, 255, 255))
            p_s1_rect = p_s1_text.get_rect(center=(window_size[0] / 2, window_size[1] / 4 + 200))
            screen.blit(p_s1_text, p_s1_rect)

            p_s2_text = font.render(p_s2, True, (255, 255, 255))
            p_s2_rect = p_s2_text.get_rect(center=(window_size[0] / 2, window_size[1] / 4 + 300))
            screen.blit(p_s2_text, p_s2_rect)

            p_s3_text = font.render(p_s3, True, (255, 255, 255))
            p_s3_rect = p_s3_text.get_rect(center=(window_size[0] / 2, window_size[1] / 4 + 400))
            screen.blit(p_s3_text, p_s3_rect)

            p_s4_text = font.render(p_s4, True, (255, 255, 255))
            p_s4_rect = p_s4_text.get_rect(center=(window_size[0] / 2, window_size[1] / 4 + 500))
            screen.blit(p_s4_text, p_s4_rect)

            # Update the screen
            pygame.display.flip()

            # Wait one second
            time.sleep(1)

    # Run the countdown function
    countdown()

    # Quit Pygame
    pygame.quit()


def startGame(p_person, length_of_wait, p_s1, p_s2, p_s3, p_s4):
    opening_screen(p_person, length_of_wait, p_s1, p_s2, p_s3, p_s4)
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Rumours spreading")
    # Create the grid
    grid = []
    list_person = []
    number_of_person = 0
    for i in range(grid_width):
        row = []
        for j in range(grid_height):
            if random.random() < p_person:
                is_person = True
                cell_type = random.choices([S1, S2, S3, S4], [p_s1, p_s2, p_s3, p_s4])[0]
                # append the person to the list if is not from s4
                if is_person:
                    number_of_person += 1
                if cell_type != S4 and is_person:
                    list_person.append((i, j))
            else:
                is_person = False
                cell_type = None
            cell = Cell(is_person, cell_type, i, j, length_of_wait)
            row.append(cell)
        grid.append(row)
    random_person = random.choice(list_person)
    grid[random_person[0]][random_person[1]].rumor = 1
    grid[random_person[0]][random_person[1]].spread_rumor = 1
    print("Number of person: ", number_of_person)
    return show_grid(grid, length_of_wait, number_of_person)


def B_Game(p_person, length_of_wait, p_s1, p_s2, p_s3, p_s4):
    opening_screen(p_person, length_of_wait, p_s1, p_s2, p_s3, p_s4)
    number_of_blocks = int((1 - p_person) * grid_width * grid_height)
    number_of_person = int(p_person * grid_width * grid_height)
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Rumours spreading")
    # Create the grid
    grid = []
    for z in range(grid_width):
        row = []
        for k in range(grid_height):
            cell = Cell(False, None, z, k, length_of_wait)
            row.append(cell)
        grid.append(row)
    number_of_lines = number_of_blocks // 100
    lst_of_places = []
    # over from the middle line
    for i in range(grid_width):
        row = []
        for j in range(number_of_lines):
            if j >= grid_height:
                break
            grid[i][j].is_person = False
            grid[i][j].cell_type = None
            # add the index of the x row and the y to the list
            lst_of_places.append((i, j))
        grid.append(row)
    # go over the grid from start to end and fill with randoms s1 s2 s3 s4
    list_person = []
    for i in range(grid_width):
        for j in range(grid_height):
            # check if (i,j) is in the list of places
            if (i, j) not in lst_of_places:
                grid[i][j].is_person = True
                # choose the type of the person randomly
                cell_type = random.choices([S1, S2, S3, S4], [p_s1, p_s2, p_s3, p_s4])[0]
                grid[i][j].cell_type = cell_type
                if cell_type != S4:
                    list_person.append((i, j))
    random_person = random.choice(list_person)
    grid[random_person[0]][random_person[1]].rumor = 1
    grid[random_person[0]][random_person[1]].spread_rumor = 1
    return show_grid(grid, length_of_wait, number_of_person)


def D_Game(p_person, length_of_wait, p_s1, p_s2, p_s3, p_s4):
    opening_screen(p_person, length_of_wait, p_s1, p_s2, p_s3, p_s4)
    number_of_person = int(p_person * grid_width * grid_height)
    grid = []
    list_person = []
    number_of_s1 = 0
    number_of_s4 = 0
    # Initialize the grid with empty cells
    pygame.init()
    pygame.display.set_caption("Rumours spreading")
    for k in range(grid_width):
        row = []
        for z in range(grid_height):
            cell = Cell(False, None, k, z, length_of_wait)
            row.append(cell)
        grid.append(row)
    # Place S1 cells in clusters surrounded by S4 cells or empty cells
    while number_of_s1 < grid_width * grid_height * p_person * p_s1:
        x, y = random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)
        if not grid[x][y].is_person:
            list_person.append((x, y))
            number_of_s1 += 1
            grid[x][y].is_person = True
            grid[x][y].cell_type = S1
            # Add S4 or empty cells around the S1 cell
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    else:
                        if i + x >= 0 and i + x < grid_width and j + y >= 0 and j + y < grid_height:
                            if not grid[i + x][j + y].is_person:
                                if number_of_s4 < grid_width * grid_height * p_person * p_s4:
                                    grid[i + x][j + y].cell_type = S4
                                    grid[i + x][j + y].is_person = True
                                    number_of_s4 += 1

    s2_counter = 0
    s3_counter = 0
    # Fill the remaining cells with S2 and S3 cells
    for i in range(grid_width):
        for j in range(grid_height):
            if not grid[i][j].is_person and s2_counter < grid_width * grid_height * p_person * (p_s2):
                grid[i][j].is_person = True
                grid[i][j].cell_type = S2
                s2_counter += 1
                list_person.append((i, j))
    # Fill the remaining cells with S2 and S3 cells
    for i in range(grid_width):
        for j in range(grid_height):
            if not grid[i][j].is_person and s3_counter < grid_width * grid_height * p_person * (p_s3):
                grid[i][j].is_person = True
                grid[i][j].cell_type = S3
                s3_counter += 1
                list_person.append((i, j))
    while (number_of_s4 < grid_width * grid_height * p_person * p_s4):
        x, y = random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)
        if not grid[x][y].is_person:
            number_of_s4 += 1
            grid[x][y].is_person = True
            grid[x][y].cell_type = S4

    random_person = random.choice(list_person)
    grid[random_person[0]][random_person[1]].rumor = 1
    grid[random_person[0]][random_person[1]].spread_rumor = 1
    return show_grid(grid, length_of_wait, number_of_person)


def play_one_iteration(grid, length):
    list_update = []
    count_new_rumor = 0
    for i in range(grid_width):
        for j in range(grid_height):
            if grid[i][j].is_person:
                if random.random() < grid[i][j].chance_spread():
                    if grid[i][j].length_of_wait == 0:
                        grid[i][j].length_of_wait = length
                        grid[i][j].spread_rumor = 0
                        for x in range(-1, 2):
                            for y in range(-1, 2):
                                if x == 0 and y == 0:
                                    continue
                                if 0 <= i + x < grid_width and 0 <= j + y < grid_height:
                                    if grid[i + x][j + y].is_person:
                                        list_update.append((i + x, j + y))
                    else:
                        if grid[i][j].length_of_wait > 0:
                            grid[i][j].length_of_wait -= 1
    for i in range(len(list_update)):
        if grid[list_update[i][0]][list_update[i][1]].rumor == 0:
            count_new_rumor += 1
            grid[list_update[i][0]][list_update[i][1]].rumor = 1
            grid[list_update[i][0]][list_update[i][1]].spread_rumor = +1
        else:
            grid[list_update[i][0]][list_update[i][1]].spread_rumor += 1
    return grid, count_new_rumor


def show_grid(grid, length_of_wait, number_of_person):
    person_with_rumor = 0
    lst_person_with_rumor = []
    screen = pygame.display.set_mode(window_size)
    # Game loop
    font = pygame.font.Font(None, 50)
    lst_rumor = []
    # Game loop
    running = True
    iteration = 0
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(iteration)
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
        grid, counter = play_one_iteration(grid, length_of_wait)
        text_surface = font.render("Iteration: {}".format(iteration), True, (0, 255, 0))

        # Blit the text surface onto the screen surface
        screen.blit(text_surface, (10, 10))

        # Update the display
        pygame.display.flip()
        person_with_rumor += counter
        lst_rumor.append((iteration, counter))

        precent = person_with_rumor
        lst_person_with_rumor.append(precent)
        if iteration == 9000:
            running = False
        iteration += 1
        # Quit Pygame
    pygame.quit()
    return lst_rumor, lst_person_with_rumor


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    show_menu()
