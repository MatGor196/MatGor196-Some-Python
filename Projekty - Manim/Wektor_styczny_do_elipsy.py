from manim import *


class Animacja(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        alfa = ValueTracker(0)
        elipsa = Ellipse(color=RED).scale(2)
        punkt = Dot(color=BLACK)
        wektor = self.wektor_styczny(alfa.get_value(), elipsa, skala=2).set_color(BLACK)

        punkt.add_updater(lambda p: p.move_to(wektor.get_start()))
        wektor.add_updater(lambda w: w.become(self.wektor_styczny(alfa.get_value() % 1, elipsa, skala=2).set_color(BLACK)))

        self.wait()

        self.play(
            Create(elipsa),
            GrowFromCenter(punkt),
            GrowArrow(wektor)
        )

        self.play(alfa.animate.increment_value(2), run_time=4, rate_func=linear)
        self.wait()


    def wektor_styczny(self, stosunek, figura, mikro_zmiana=0.001, skala=1):
        x_y = figura.point_from_proportion(stosunek)
        x_y_plus_dx_dy = figura.point_from_proportion(stosunek + mikro_zmiana)
        kierunek = Line(x_y, x_y_plus_dx_dy)
        wektor_jednostkowy = kierunek.get_unit_vector() * skala
        wektor = Arrow(x_y, x_y+wektor_jednostkowy, buff=0)
        return wektor