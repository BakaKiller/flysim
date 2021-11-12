import pyglet
import random
import math

window = pyglet.window.Window(1280, 720, "Flysim", True)
img = pyglet.image.load('fly.png')
img.anchor_x = img.width // 2
img.anchor_y = img.height // 2
fly = pyglet.sprite.Sprite(img, random.randint(0, 1280), random.randint(0, 720))
min_speed_x = min_speed_y = -5
max_speed_x = max_speed_y = 5
mouse_x = None
mouse_y = None
speed_x = random.randint(min_speed_x, max_speed_x)
speed_y = random.randint(min_speed_y, max_speed_y)
fly.scale = 0.03
fly.rotation = math.degrees(math.atan2(speed_x, speed_y))
pyglet.gl.glClearColor(1,1,1,1)

@window.event
def on_draw():
    window.clear()
    grab_fly()
    fly.draw()
    pyglet.clock.tick()

@window.event
def on_mouse_motion(x, y, dx, dy):
    global mouse_x, mouse_y
    mouse_x = x
    mouse_y = y

@window.event
def on_mouse_leave(x, y):
    global mouse_x, mouse_y
    mouse_x = None
    mouse_y = None

def grab_fly():
    global max_speed_y, max_speed_x, min_speed_y, min_speed_x, mouse_x, mouse_y
    if mouse_x is None or mouse_y is None:
        max_speed_x = 5
        min_speed_x = -5
        max_speed_y = 5
        min_speed_y = -5
        return
    
    x = mouse_x
    y = mouse_y

    flyx, flyy = fly.position
    if flyx >= x + 3:
        max_speed_x = 0
        min_speed_x = -5
    elif flyx <= x - 3:
        max_speed_x = 5
        min_speed_x = 0
    else:
        max_speed_x = 5
        min_speed_x = -5

    if flyy >= y + 3:
        max_speed_y = 0
        min_speed_y = -5
    elif flyy <= x -3:
        max_speed_y = 5
        min_speed_y = 0
    else:
        max_speed_y = 5
        min_speed_y = -5

def move(dt, *args, **kwargs):
    global speed_x, speed_y
    fly.rotation = math.degrees(math.atan2(speed_x, speed_y))
    fly.x += speed_x
    fly.y += speed_y
    x, y = fly.position
    if x > 1280:
        fly.x = 0
    if x < 0:
        fly.x = 1280
    if y > 720:
        fly.y = 0
    if y < 0:
        fly.y = 720
    
    speed_x += random.randint(-1, 1)
    if speed_x > max_speed_x:
        speed_x = max_speed_x
    if speed_x < min_speed_x:
        speed_x = min_speed_x

    speed_y += random.randint(-1, 1)
    if speed_y > max_speed_y:
        speed_y = max_speed_y
    if speed_y < min_speed_y:
        speed_y = min_speed_y

    pass

pyglet.clock.schedule_interval(move, 1/60)

if __name__ == '__main__':
    pyglet.app.run()