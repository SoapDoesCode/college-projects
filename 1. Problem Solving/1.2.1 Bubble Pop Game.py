import pygame
import asyncio
import sys

from random import randint as rng

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Pop Hell")
font = pygame.font.Font(None, 36)

TIME_LIMIT = 60

score = 0
reset_timer = False # A flag to reset the timer
elapsed_time = 0
circ_colour = (255, 0, 0)

playing = True

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
    print(f"Total Score: {score}")

def handle_click(mouse_pos, circ_size, circ_x, circ_y):
    global score, reset_timer
    min_x = circ_x - circ_size
    max_x = circ_x + circ_size
    min_y = circ_y - circ_size
    max_y = circ_y + circ_size

    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    if mouse_x >= min_x and mouse_x <= max_x and mouse_y >= min_y and mouse_y <= max_y:
        score += 1
        reset_timer = True
        return True
    return False

def generate_target(circ_size, circ_x, circ_y, circ_colour):
    pygame.draw.circle(screen, circ_colour, (circ_x, circ_y), circ_size)

async def main_game():
    global playing, circ_colour

    screen.fill((255, 255, 255))

    rand_size = rng(10, 50)
    rand_x = rng(rand_size, (WIDTH - rand_size))
    rand_y = rng(rand_size, (HEIGHT - rand_size))

    # Start the asynchronous timer
    asyncio.create_task(stop(TIME_LIMIT))

    while playing:
        screen.fill((255, 255, 255))
        generate_target(rand_size, rand_x, rand_y, circ_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # playing = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()

                is_popped = handle_click(mouse_pos, rand_size, rand_x, rand_y)

                if is_popped:
                    rand_size = rng(10, 50)
                    rand_x = rng(rand_size, (WIDTH - rand_size))
                    rand_y = rng(rand_size, (HEIGHT - rand_size))

                    circ_colour = (rng(0, 255), rng(0, 255), 0, 255)
                    generate_target(rand_size, rand_x, rand_y, circ_colour)

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        timer_text = font.render(f"Time: {TIME_LIMIT - elapsed_time} seconds", True, (0, 0, 0))

        screen.blit(score_text, (10, 50))
        screen.blit(timer_text, (10, 10))

        # update the game state and draw the screen
        pygame.display.flip()

        await asyncio.sleep(0) # this is needed, DO NOT REMOVE

asyncio.run(main_game())