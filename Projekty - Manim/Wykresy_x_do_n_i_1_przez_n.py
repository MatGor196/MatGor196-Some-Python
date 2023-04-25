from manim import *

class Wykresy(Scene):
    def construct(self):
        osie = Axes(x_range=[0, 1, 0.05],
                    y_range=[0, 1, 0.05],
                    x_length=9,
                    y_length=5.5,
                    axis_config={"color": WHITE,
                                 "include_tip": False,
                                 "number_scale_value": 0.5,
                                 "numbers_to_include": np.arange(0, 1.01, 0.10)})

        etykieta_x = osie.get_x_axis_label("x")
        etykieta_y = osie.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)

        wykresy = VGroup()
        for i in np.arange(1, 20+0.1, 0.5):
            wykresy += osie.get_graph(lambda x: x ** i)
            wykresy += osie.get_graph(lambda x: x ** (1/i), use_smoothing=False)

        wykresy += osie.get_horizontal_line(osie.c2p(1, 1, 0), color=BLUE)
        wykresy += osie.get_vertical_line(osie.c2p(1, 1, 0), color=BLUE)
        wykresy += Dot(osie.c2p(1, 1, 0), color=YELLOW)
        wykresy += Tex("(1, 1)").scale(0.75).next_to(osie.c2p(1, 1, 0))

        tytul = Title(r"Wykresy $y=x^{ {1}/{n} }$ i $y=x^n (n=1, 2, ..., 20)$",
                      scale_factor=0.85,
                      include_underline=False)

        self.add(wykresy)
        self.add(osie)
        self.add(etykieta_x, etykieta_y, tytul)
        self.wait()