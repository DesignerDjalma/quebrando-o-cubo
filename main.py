from ursina import *

app = Ursina()
speed = 10

player = Entity(model='cube', color=color.orange, scale_y=2)
box = Entity(model='cube', color=color.white,scale_x=1)


box.collider = 'mesh'
player.collider = 'mesh'

def update():
    player.x += (held_keys['d'] - held_keys['a']) * time.dt * speed
    player.z += (held_keys['w'] - held_keys['s']) * time.dt * speed

    box.z += (held_keys['i'] - held_keys['k']) * time.dt * speed 
    pass

app.run()