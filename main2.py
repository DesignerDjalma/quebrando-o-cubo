from ursina import Ursina, Entity, Text # type: ignore
from ursina import invoke, held_keys, color, time

# create a window
app = Ursina(
    title="Ursina Window",
)


jogador: Entity = Entity(model='cube', color=color.orange, scale_y=1, scale_x=1)
score: Text = Text(text="Vida")
# create a function called 'update'.
# this will automatically get called by the engine every frame.

def update():
    jogador.x += held_keys['d'] * time.dt
    jogador.x -= held_keys['a'] * time.dt
    jogador.y += held_keys['w'] * time.dt
    jogador.y -= held_keys['s'] * time.dt

# this part will make the player move left or right based on our input.
# to check which keys are held down, we can check the held_keys dictionary.
# 0 means not pressed and 1 means pressed.
# time.dt is simply the time since the last frame. by multiplying with this, the
# player will move at the same speed regardless of how fast the game runs.


def input(key):
    if key == 'space':
        jogador.y += 1
        invoke(setattr, jogador, 'y', jogador.y-1, delay=.25)


# start running the game
app.run()