from ursina import Entity # type: ignore
from ursina import held_keys, color, time

class Player(Entity):
    def __init__(self, 
                 model: str = "cube", 
                 color: color = color.red, 
                 scale: tuple[int, ...] = (1, 1, 1), 
                 position: tuple[int, ...] = (0, 0, 0),
                 speed: float = 1.0,
                 ) -> None:
        
        super().__init__(
            model=model,
            color=color,
            scale=scale,
            position=position,
        )
        self.speed = speed

    def update(self):
        self.x += (held_keys['d'] - held_keys['a']) * time.dt * self.speed
        self.y += (held_keys['w'] - held_keys['s']) * time.dt * self.speed



def teste(*args, **kwargs) -> None:
    p1 = Player()

def main(*args, **kwargs) -> None:
    pass


if __name__ == "__main__":
    main()
    # Fim do Código