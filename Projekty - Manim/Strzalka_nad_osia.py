from manim import *

class Strzalka(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        os_liczbowa = NumberLine(x_range=np.array([0, 10, 1]),
                                 length=7,
                                 include_numbers=True,
                                 number_scale_value=0.75).set_color(BLACK)
        strzalka = Arrow(start=UP, end=ORIGIN, color=BLACK, max_tip_length_to_length_ratio=0.17, buff=0.9)

        alfa = ValueTracker(1)

        strzalka.add_updater(lambda s: s.next_to(os_liczbowa.n2p(alfa.get_value()), UP))

        self.add(os_liczbowa, strzalka)

        self.wait(1)
        self.play(alfa.animate.set_value(5))
        self.wait(0.5)
        self.play(alfa.animate.set_value(2))
        self.wait(0.5)
        self.play(alfa.animate.set_value(7))
        self.wait(0.5)
        self.play(alfa.animate.set_value(3))
        self.wait(0.5)
        self.play(alfa.animate.increment_value(1))
        self.wait(0.5)

        self.wait(1)