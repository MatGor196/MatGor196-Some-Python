from manim import *

class Kolo_modulo(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        "wykonywana operacja: liczba = (liczba*MOD) % ILOSC"

        ILOSC = 25
        MOD = 3
        START = 1
        SKALA_ETYKIET = 1
        WLACZONE_ETYKIETY = True
        ILOSC_LINII = 100

        kolo = Circle(color=BLACK, radius=3)

        Punkty = VGroup()
        for i in range(ILOSC):
            punkt = Dot(color=BLACK).shift(3*RIGHT)
            punkt.rotate_about_origin(angle=i/ILOSC*TAU)
            Punkty.add(punkt)

        if WLACZONE_ETYKIETY == True:
            Etykiety = VGroup()
            for i in range(ILOSC):
                etykieta_punktu = Tex("$" + str(i) + "$", color=BLACK)
                etykieta_punktu.next_to(Punkty[i], round(np.sin(i/ILOSC*TAU), 2)*UP + round(np.cos(i/ILOSC*TAU), 2)*RIGHT)
                Etykiety.add(etykieta_punktu.scale(SKALA_ETYKIET))
            self.add(Etykiety)

        Linie = VGroup()
        wartosc = START
        for i in range(ILOSC_LINII):
            stara_wartosc = wartosc
            wartosc = (MOD*wartosc) % ILOSC
            Linie.add(Line(start=[Punkty[stara_wartosc].get_center()], end=[Punkty[wartosc].get_center()], color=BLUE))

        self.add(kolo)
        self.add(Linie)
        self.add(Punkty)

        self.wait()