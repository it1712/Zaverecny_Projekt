from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, NumericProperty, ListProperty
from kivy.uix.image import Image

"""
    Třída Pipe (Widget)
    Metody:
        move() - pohne trubkou doleva
        passed() - když projde trubkou, přičte score
"""


class Pipe(Widget):
    # Šířka mezery mezi horní a dolní trubkou
    GAP_SIZE = NumericProperty(200)
    # = center_y
    pipe_center = NumericProperty(700)

    # Načte texturu
    pipe_body_texture = Image(source="img/pipe.png").texture
    # Souřadnice horní textury (otočení textury) + ... ???
    top_pipe_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))
    # Souřadnice spodní textury - nechat jako vzor
    # lower_pipe_tex_coords = ListProperty((0, 1, 1, 1, 1, 0, 0, 0))

    # Bool pro kontrolu, jestli ji ptáci proletěli
    # stane se z ní jen graf. objekt, než dojde na konec mapy
    is_passed = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Pipe, self).__init__(**kwargs)

    # Pohyb trubky
    def move(self):
        self.center_x -= 5

    # Metoda vyvolaná, když je trubka passnutá
    def passed(self):
        self.is_passed = True

    def __str__(self):
        return f"\n" \
               f"Center = [{self.center_x}, {self.pipe_center}]\n" \
               f"Passed = {self.is_passed}\n" \
               f"pos    = {self.pos}\n" \
               f"size   = {self.size}"
