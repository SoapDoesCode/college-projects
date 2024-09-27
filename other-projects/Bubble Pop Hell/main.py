import pygame
import asyncio
import sys

from random import randint as rng

from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

pygame.init()
clock = pygame.time.Clock()

### GAME SETTINGS ###
WIDTH = config.getint("Settings", "window_width")
HEIGHT = config.getint("Settings", "window_height")
REFRESH_RATE = config.getint("Settings", "refresh_rate")

CIRC_MIN = config.getint("Settings", "circ_min_size")
CIRC_MAX = config.getint("Settings", "circ_max_size")

TIME_LIMIT = config.getint("Settings", "time_limit")

circ_colour = list(map(int, config.get('Settings', 'init_circ_colour').split(',')))
bg_colour = list(map(int, config.get('Settings', 'init_bg_colour').split(',')))

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

async def stop(time_limit):
    global reset_timer, elapsed_time, playing
    while elapsed_time < time_limit:
        await asyncio.sleep(1)
        if reset_timer:
            elapsed_time = 0
            reset_timer = False
        else:
            elapsed_time += 1
    playing = False
    pygame.quit() # Quit the game after 60 seconds of no pops
    print(f"Final Score: {score}")

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

    rand_size = rng(CIRC_MIN, CIRC_MAX)
    rand_x = rng(rand_size, (WIDTH - rand_size))
    rand_y = rng(rand_size, (HEIGHT - rand_size))

    # Start the asynchronous timer
    asyncio.create_task(stop(TIME_LIMIT))

    while playing:
        screen.fill((bg_colour))
        generate_target(rand_size, rand_x, rand_y, circ_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # playing = False
                pygame.quit()
                print(f"Final Score: {score}")
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()

                is_popped = handle_click(mouse_pos, rand_size, rand_x, rand_y)

                if is_popped:
                    rand_size = rng(CIRC_MIN, CIRC_MAX)
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
        timer_text = font.render(f"Time: {TIME_LIMIT - elapsed_time} seconds", True, text_rgb)

        screen.blit(score_text, (10, 50))
        screen.blit(timer_text, (10, 10))

        # sets the refresh rate (fps)
        clock.tick(REFRESH_RATE)

        # update the game state and draw the screen
        pygame.display.flip()

        await asyncio.sleep(0) # this is needed, DO NOT REMOVE

asyncio.run(main_game())
