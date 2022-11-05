import pygame, sys

pygame.init()

fullscreen = True

clock = pygame.time.Clock()

fps_ = []

cooldown = False

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

def create_window(fullscreen=True):
    global window, monitor_size
    if fullscreen:
        monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    else:
        monitor_size[600, 600]

    
window = pygame.display.set_mode((monitor_size[0], monitor_size[1]), pygame.FULLSCREEN)


def window_color(color):
    try:
        window.fill(color)
    except:
        print("Color was not found")

def SRT_setup():

    global fullscreen
    global cooldown

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        sys.exit()

    if cooldown == False:
        if keys[pygame.K_f]:
            cooldown = True
            
            if fullscreen:
                fullscreen = False
                window = pygame.display.set_mode((monitor_size[0], monitor_size[1]), pygame.RESIZABLE)
                pygame.time.delay(100)
                cooldown = False
            else:
                fullscreen = True
                window = pygame.display.set_mode((monitor_size[0], monitor_size[1]), pygame.FULLSCREEN)
                pygame.time.delay(100)
                cooldown = False

def SRT_quit():
    sys.exit()

def SRT_set_fps(fps=60):
    global fps_
    if fps in fps_:
        pass
    else:
        
        fps__ = clock.tick(fps)

def window_caption(name):

    pygame.display.set_caption(name)

def window_icon(path):
    try:
        pygame.display.set_icon(path)
    except:
        print("Path was not found")

def delay(seconds):

    pygame.time.delay(seconds//1000)

def SRT_show_fps(color, x, y, size):
    font = pygame.font.Font('srt/double-gum.ttf', size)
    text = font.render(f"fps: {round(clock.get_fps())}", None, color)
    window.blit(text, (x, y))

def draw_text(text, color, x, y, size):
    font = pygame.font.Font('srt/double-gum.ttf', size)
    text = font.render(f"{text}", None, color)
    window.blit(text, (x, y))

def draw_player(path, x, y):
    try:
        player_img = pygame.image.load(path)
        window.blit(player_img, (x, y))

    except:
        print("Image Path Was Not Found")
