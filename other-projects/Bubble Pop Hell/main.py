import pygame
import asyncio
import sys, os

from random import randint as rng

from configparser import ConfigParser

import pygame_menu

configFilePath = os.path.join(os.path.dirname(__file__), 'config.ini')
config = ConfigParser()
config.read(configFilePath)

pygame.init()
clock = pygame.time.Clock()

### GAME SETTINGS ###
WIDTH = config.getint("Settings", "window_width")
HEIGHT = config.getint("Settings", "window_height")
refresh_rate = config.getint("Settings", "refresh_rate")

circ_min = config.getint("Settings", "circ_min_size")
circ_max = config.getint("Settings", "circ_max_size")

time_limit = config.getint("Settings", "time_limit")

circ_colour = list(map(int, config.get('Settings', 'init_circ_colour').removeprefix("(").removesuffix(")").split(',')))
bg_colour = list(map(int, config.get('Settings', 'init_bg_colour').removeprefix("(").removesuffix(")").split(',')))

random_circ_colour = config.getboolean("Settings", "random_circ_colour")
random_bg_colour = config.getboolean("Settings", "random_bg_colour")

rainbow_circ = config.getboolean("Settings", "rainbow_circ")
rainbow_circ_speed = config.getint("Settings", "rainbow_circ_speed")
rainbow_bg = config.getboolean("Settings", "rainbow_bg")
rainbow_bg_speed = config.getint("Settings", "rainbow_bg_speed")
### GAME SETTINGS ###

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Pop Hell")
font = pygame.font.Font(None, 36)

score = 0
playing = True
reset_timer = False # A flag to reset the timer
elapsed_time = 0

def complement(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    # left in as an example
    # r = 0 if r > 128 else 255
    # g = 0 if g > 128 else 255
    # b = 0 if b > 128 else 255

    # best equation I have found
    r = 255 - r
    g = 255 - g
    b = 255 - b

    # left in as an example
    # r = 0 if ((r+g+b)/3) > 128 else 255
    # g = 0 if ((r+g+b)/3) > 128 else 255
    # b = 0 if ((r+g+b)/3) > 128 else 255

    rgb_values = [r, g, b]

    return rgb_values

def cycle_rainbow(rgb_colour: list, speed):
    if rgb_colour[0] == 0 and rgb_colour[1] == 0 and rgb_colour[2] == 0:
        rgb_colour = [255, 255, 255]

    if rgb_colour[0]+speed <= 255 and rgb_colour[1] == 0 and rgb_colour[2] == 255:
        rgb_colour[0] += speed # Increase Red (Magenta to Red)
    elif rgb_colour[1]+speed <= 255 and rgb_colour[0] == 255:
        rgb_colour[1] += speed # Increase Green (Red to Yellow)
    elif rgb_colour[0]-speed >= 0 and rgb_colour[1] == 255:
        rgb_colour[0] -= speed # Decrease Red (Yellow to Green)
    elif rgb_colour[2]+speed <= 255 and rgb_colour[1] == 255:
        rgb_colour[2] += speed # Increase Blue (Green to Cyan)
    elif rgb_colour[1]-speed >= 0 and rgb_colour[2] == 255:
        rgb_colour[1] -= speed # Decrease Green (Cyan to Blue)
    elif rgb_colour[2]-speed >= 0 and rgb_colour[0] == 255:
        rgb_colour[2] -= speed # Decrease Blue (Blue to Magenta)

    if rgb_colour[0]-speed < 0:
        rgb_colour[0] = 0
    elif rgb_colour[0]+speed > 255:
        rgb_colour[0] = 255
    if rgb_colour[1]-speed < 0:
        rgb_colour[1] = 0
    elif rgb_colour[1]+speed > 255:
        rgb_colour[1] = 255
    if rgb_colour[2]-speed < 0:
        rgb_colour[2] = 0
    elif rgb_colour[2]+speed > 255:
        rgb_colour[2] = 255

    return rgb_colour

def update_config():
    with open(configFilePath, 'w') as configfile:
        config.write(configfile)

async def stop(time_limit):
    global reset_timer, elapsed_time, playing
    while elapsed_time < time_limit:
        await asyncio.sleep(1)
        # if reset_timer:
        #     elapsed_time = 0
        #     reset_timer = False
        # else:
        elapsed_time += 1
    playing = False
    pygame.quit() # Quit the game after 60 seconds of no pops
    print(f"Final Score: {score}")
    update_config()

def handle_click(mouse_pos, circ_size, circ_x, circ_y):
    global score, reset_timer
    diff_x = abs(mouse_pos[0] - circ_x)
    diff_y = abs(mouse_pos[1] - circ_y)

    total_diff = (diff_x**2 + diff_y**2)**0.5

    if total_diff <= circ_size:
        score += 1
        reset_timer = True
        return True
    return False

def generate_target(circ_size, circ_x, circ_y, circ_colour):
    pygame.draw.circle(screen, circ_colour, (circ_x, circ_y), circ_size)

async def main_game():
    global playing, circ_colour, bg_colour

    screen.fill(bg_colour)

    rand_size = rng(circ_min, circ_max)
    rand_x = rng(rand_size, (WIDTH - rand_size))
    rand_y = rng(rand_size, (HEIGHT - rand_size))

    # Start the asynchronous timer
    asyncio.create_task(stop(time_limit))

    while playing:
        screen.fill((bg_colour))
        generate_target(rand_size, rand_x, rand_y, circ_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # playing = False
                pygame.quit()
                print(f"Final Score: {score}")
                update_config()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()

                is_popped = handle_click(mouse_pos, rand_size, rand_x, rand_y)

                if is_popped:
                    rand_size = rng(circ_min, circ_max)
                    rand_x = rng(rand_size, (WIDTH - rand_size))
                    rand_y = rng(rand_size, (HEIGHT - rand_size))

                    if random_circ_colour:
                        circ_colour = [rng(0, 255), rng(0, 255), 0, 255]
                    if random_bg_colour:
                        bg_colour = [rng(0, 255), rng(0, 255), 0, 255]
                    generate_target(rand_size, rand_x, rand_y, circ_colour)
        
        if rainbow_circ:
            circ_colour = cycle_rainbow(circ_colour, rainbow_circ_speed)
        if rainbow_bg:
            bg_colour = cycle_rainbow(bg_colour, rainbow_bg_speed)

        text_rgb = complement(bg_colour)
        score_text = font.render(f"Score: {score}", True, text_rgb)
        timer_text = font.render(f"Time: {time_limit - elapsed_time} seconds", True, text_rgb)

        screen.blit(score_text, (10, 50))
        screen.blit(timer_text, (10, 10))

        # sets the refresh rate (fps)
        clock.tick(refresh_rate)

        # update the game state and draw the screen
        pygame.display.flip()

        await asyncio.sleep(0) # this is needed, DO NOT REMOVE

def start_game():
    asyncio.run(main_game())

def set_time_limit(time):
    global time_limit
    time_limit = int(time)
    config.set("Settings", "time_limit", str(time_limit))

def set_circ_min(value):
    global circ_min
    circ_min =  int(value)
    config.set("Settings", "circ_min_size", str(circ_min))

def set_circ_max(value):
    global circ_max
    circ_max =  int(value)
    config.set("Settings", "circ_max_size", str(circ_max))

def set_circ_colour(colour):
    global circ_colour
    circ_colour = list(colour)
    config.set("Settings", "init_circ_colour", str(colour))

def set_bg_colour(colour):
    global bg_colour
    bg_colour = list(colour)
    config.set("Settings", "init_bg_colour", str(colour))

def random_circ_toggle(toggle_state):
    global random_circ_colour
    random_circ_colour = toggle_state
    config.set("Settings", "random_circ_colour", str(random_circ_colour))

def rainbow_circ_toggle(toggle_state):
    global rainbow_circ
    rainbow_circ = toggle_state
    config.set("Settings", "rainbow_circ", str(rainbow_circ))

def set_rainbow_circ_speed(speed):
    global rainbow_circ_speed
    rainbow_circ_speed = int(speed)
    config.set("Settings", "rainbow_circ_speed", str(rainbow_circ_speed))

def random_bg_toggle(toggle_state):
    global random_bg_colour
    random_bg_colour = toggle_state
    config.set("Settings", "random_bg_colour", str(random_bg_colour))

def rainbow_bg_toggle(toggle_state):
    global rainbow_bg
    rainbow_bg = toggle_state
    config.set("Settings", "rainbow_bg", str(rainbow_bg))

def set_rainbow_bg_speed(speed):
    global rainbow_bg_speed
    rainbow_bg_speed = int(speed)
    config.set("Settings", "rainbow_bg_speed", str(rainbow_bg_speed))

menu = pygame_menu.Menu("Settings", 800, 600, theme=pygame_menu.themes.THEME_BLUE)

menu.add.button("Start Game", start_game)
menu.add.text_input("Time Limit: ", default=time_limit, onchange=set_time_limit, font_size=25)
menu.add.text_input("Min Circle Size: ", default=circ_min, onchange=set_circ_min, font_size=25)
menu.add.text_input("Max Circle Size: ", default=circ_max, onchange=set_circ_max, font_size=25)
menu.add.color_input("Circle Colour: ", default=tuple(circ_colour), color_type='rgb', onchange=set_circ_colour, font_size=25)
menu.add.color_input("Background Colour: ", default=tuple(bg_colour), color_type='rgb', onchange=set_bg_colour, font_size=25)
menu.add.toggle_switch("Random Circle:", default=random_circ_colour, state_values=(False, True), onchange=random_circ_toggle, font_size=25)
menu.add.toggle_switch("Rainbow Circle:", default=rainbow_circ, state_values=(False, True), onchange=rainbow_circ_toggle, font_size=25)
menu.add.text_input("Rainbow Circle Speed: ", default=rainbow_circ_speed, onchange=set_rainbow_circ_speed, font_size=25)
menu.add.toggle_switch("Random Background:", default=random_bg_colour, state_values=(False, True), onchange=random_bg_toggle, font_size=25)
menu.add.toggle_switch("Rainbow Background:", default=rainbow_bg, state_values=(False, True), onchange=rainbow_bg_toggle, font_size=25)
menu.add.text_input("Rainbow Background Speed: ", default=rainbow_bg_speed, onchange=set_rainbow_bg_speed, font_size=25)

menu.mainloop(screen)


# asyncio.run(main_game())