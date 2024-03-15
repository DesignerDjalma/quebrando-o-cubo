from ursina import *

app = Ursina()
speed = 10

player = Entity(model='circle', color=color.orange, scale_y=2)
def update():
    player.x += (held_keys['d'] - held_keys['a']) * time.dt * speed
    player.y += (held_keys['w'] - held_keys['s']) * time.dt * speed
    pass

app.run()