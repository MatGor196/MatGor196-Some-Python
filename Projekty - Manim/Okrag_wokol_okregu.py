from manim import *


class Scena(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        duze_kolo = Circle(radius=2)
        male_kolo = Circle(radius=0.75, stroke_color=BLACK).shift(2*RIGHT)
        srodek_malego_kola = Dot([2, 0, 0]).set_color(BLACK)
        punkt = Dot([2.75, 0, 0]).set_color(GREY)
        krzywa = VMobject().set_color(GREY)
        krzywa.set_points_as_corners([punkt.get_center(), punkt.get_center()])

        def updater_ruchu_malego_kola(kolo):
            kolo.move_to(srodek_malego_kola.get_center())

        male_kolo.add_updater(updater_ruchu_malego_kola)

        def updater_krzywej(krzywa):
            nastepna_krzywa = krzywa.copy()
            nastepna_krzywa.add_points_as_corners([punkt.get_center()])
            krzywa.become(nastepna_krzywa)

        krzywa.add_updater(updater_krzywej)

        self.add(duze_kolo, srodek_malego_kola, male_kolo, punkt, krzywa)

        self.wait(0.5)
        self.play(MoveAlongPath(srodek_malego_kola, duze_kolo), MoveAlongPath(punkt, male_kolo), rate_func = linear, run_time=5)

        self.wait()