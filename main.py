import pyglet
import random
import math

window = pyglet.window.Window(1280, 720, "Flysim", True)
img = pyglet.image.load('fly.png')
img.anchor_x = img.width // 2
img.anchor_y = img.height // 2
fly = pyglet.sprite.Sprite(img, random.randint(0, 1280), random.randint(0, 720))
speed_x = random.randint(-5, 5)
speed_y = random.randint(-5, 5)
fly.scale = 0.03
fly.rotation = math.degrees(math.atan2(speed_x, speed_y))
pyglet.gl.glClearColor(1,1,1,1)

@window.event
def on_draw():
    window.clear()
    pyglet.clock.tick()
    fly.draw()

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
    if speed_x > 5:
        speed_x = 5
    if speed_x < -5:
        speed_x = -5

    speed_y += random.randint(-1, 1)
    if speed_y > 5:
        speed_y = 5
    if speed_y < -5:
        speed_y = -5
    pass

pyglet.clock.schedule_interval(move, 1/60)

if __name__ == '__main__':
    pyglet.app.run()