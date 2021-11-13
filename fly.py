import pyglet
import random
import math


totalwidth = 1280
totalheight = 720
min_speed_x = min_speed_y = -5
max_speed_x = max_speed_y = 5
img = pyglet.image.load('fly.png')
img.anchor_x = img.width // 2
img.anchor_y = img.height // 2
flies = []
nbflies = 100

class Fly():
    def __init__(self) -> None:
        self.speed_x = random.randint(min_speed_x, max_speed_x)
        self.speed_y = random.randint(min_speed_y, max_speed_y)
        self.sprite = pyglet.sprite.Sprite(img, random.randint(0, totalwidth), random.randint(0, totalheight))
        self.sprite.scale = 0.03
        self.sprite.rotation = math.degrees(math.atan2(self.speed_x, self.speed_y))
        self.min_speed_x = min_speed_x
        self.min_speed_y = min_speed_y
        self.max_speed_x = max_speed_x
        self.max_speed_y = max_speed_y

    def grab_fly(self):
        global mouse_x, mouse_y
        if mouse_x is None or mouse_y is None:
            self.max_speed_x = max_speed_x
            self.min_speed_x = min_speed_x
            self.max_speed_y = max_speed_y
            self.min_speed_y = min_speed_y
            return
        
        x = mouse_x
        y = mouse_y

        flyx, flyy = self.sprite.position
        if flyx >= x + 3:
            self.max_speed_x = 1.5
            self.min_speed_x = min_speed_x
        elif flyx <= x - 3:
            self.max_speed_x = max_speed_x
            self.min_speed_x = -1.5
        else:
            self.max_speed_x = max_speed_x
            self.min_speed_x = min_speed_x

        if flyy >= y + 3:
            self.max_speed_y = 1.5
            self.min_speed_y = min_speed_y
        elif flyy <= x -3:
            self.max_speed_y = max_speed_y
            self.min_speed_y = -1.5
        else:
            self.max_speed_y = max_speed_y
            self.min_speed_y = min_speed_y
    
    def move(self):
        self.sprite.rotation = math.degrees(math.atan2(self.speed_x, self.speed_y))
        self.sprite.x += self.speed_x
        self.sprite.y += self.speed_y
        x, y = self.sprite.position
        if x > 1280:
            self.sprite.x = 0
        if x < 0:
            self.sprite.x = 1280
        if y > 720:
            self.sprite.y = 0
        if y < 0:
            self.sprite.y = 720
        
        self.speed_x += random.randint(-1, 1)
        if self.speed_x > self.max_speed_x:
            self.speed_x = self.max_speed_x
        if self.speed_x < self.min_speed_x:
            self.speed_x = self.min_speed_x

        self.speed_y += random.randint(-1, 1)
        if self.speed_y > self.max_speed_y:
            self.speed_y = self.max_speed_y
        if self.speed_y < self.min_speed_y:
            self.speed_y = self.min_speed_y

window = pyglet.window.Window(1280, 720, "Flysim", True)

i = 0
while i < nbflies:
    flies.append(Fly())
    i += 1

mouse_x = None
mouse_y = None

pyglet.gl.glClearColor(1,1,1,1)

@window.event
def on_draw():
    window.clear()
    for fly in flies:
        fly.grab_fly()
        fly.sprite.draw()
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

def move(dt, *args, **kwargs):
    for fly in flies:
        fly.move()

pyglet.clock.schedule_interval(move, 1/60)

if __name__ == '__main__':
    pyglet.app.run()