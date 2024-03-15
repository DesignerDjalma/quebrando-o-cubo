from ursina import *

app = Ursina()
speed = 10

player = Entity(model='cube', color=color.orange, scale_x = 1)
box = Entity(model='cube', color=color.white,scale_x=1, Texture='assets\textures\Elephant.png')
camera.rotation_x = -15

box.position = Vec3(0,2,3)
box.collider = 'mesh'
player.collider = 'mesh'


def update():
    player.x += (held_keys['d'] - held_keys['a']) * time.dt * speed
    player.y += (held_keys['w'] - held_keys['s']) * time.dt * speed
    if player.position == Vec3(1,1,1):
        player.fade_out(0.4)
    pass

app.run()