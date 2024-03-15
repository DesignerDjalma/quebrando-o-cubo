from ursina import Ursina, Entity, Text # type: ignore
from ursina import invoke, held_keys, color, time



class App:
    def __init__(self):
        self.app = Ursina()

    def run(self):
        self.app.run()



class Jogador(Entity):
    def __init__(self, speed: float = 1.0, **kwargs) -> None:
        super().__init__(**kwargs)
        self.speed = speed

    def update(self):
        """Parte de movimentação e outras ações"""

        self.x += (held_keys['d'] - held_keys['a']) * time.dt * self.speed
        self.y += (held_keys['w'] - held_keys['s']) * time.dt * self.speed










def main() -> None:
    app: App = App()
    jogador: Jogador = Jogador(model= "cube", color= color.red, scale=(1, 1, 1))
    jogador.speed = 10
    app.run()



if __name__ == "__main__":
    main()
    # Fim do Código