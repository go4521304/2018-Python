from pico2d import *
import game_framework
import title_state

name = "LogoState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image("..\\res\\logo.png")

def exit():
    global image
    del(image)

def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time +=0.01

def draw():
    global image
    clear_canvas()
    image.draw(640, 360)
    update_canvas()

def handle_events():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas(1280, 720)
    game_framework.run(current_module)
    close_canvas()