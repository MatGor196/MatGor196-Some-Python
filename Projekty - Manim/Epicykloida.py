from manim import *

class Epicykloida(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        duze_kolo = Circle(radius=1.5, color=RED)
        male_kolo = Circle(radius=0.5, color=BLUE).shift(2*RIGHT)
        punkt = Dot(color=BLACK).shift(1.5*RIGHT)

        def tworzenie_sciezki(sciezka):
            nastepna_sciezka = sciezka.copy()
            nastepna_sciezka.add_points_as_corners([punkt.get_center()])
            sciezka.become(nastepna_sciezka)

        sciezka = VMobject(color=BLACK)
        sciezka.set_points_as_corners([punkt.get_center(), punkt.get_center()])
        sciezka.add_updater(tworzenie_sciezki)

        grupa_malego_kola = VGroup()
        grupa_malego_kola.add(male_kolo, punkt)

        def updater_grupy(grupa, dt):
            grupa.rotate(dt*180*DEGREES)
            grupa.rotate(dt*60*DEGREES, about_point=[0, 0, 0])

        self.add(duze_kolo, grupa_malego_kola, sciezka)
        self.wait(1)
        grupa_malego_kola.add_updater(updater_grupy)
        self.wait(6)
        grupa_malego_kola.remove_updater(updater_grupy)
        self.wait(2)