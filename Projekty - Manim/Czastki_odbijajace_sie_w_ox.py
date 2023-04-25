from manim import *

class Czastka(Dot):
    def __init__(self,
                 punkt=ORIGIN,
                 promien: float = DEFAULT_DOT_RADIUS,
                 grubosc_obwodki=0,
                 metnosc=1.0,
                 kolor=WHITE,
                 predkosc=1,
                 kat=0,
                 **kwargs):
        super().__init__(point=punkt,
                         radius=promien,
                         stroke_width=grubosc_obwodki,
                         fill_opacity=metnosc,
                         color=kolor, **kwargs)

        self.kat = kat
        self.predkosc = predkosc
        self.promien = promien

        def ruch_czastki(czastka, dt):
            if self.kat < 0:
                self.kat = TAU - self.kat
            elif self.kat > TAU:
                self.kat = self.kat - TAU

            czastka.shift(dt * predkosc * np.cos(self.kat) * RIGHT)
            czastka.shift(dt * predkosc * np.sin(self.kat) * UP)

            aktualny_x = czastka.get_center()[0]
            aktualny_y = czastka.get_center()[1]

            bariera_x = 7.1-promien
            bariera_y = 4-promien

            if aktualny_x >= bariera_x or aktualny_x <= -bariera_x: #prawa i lewa strona
                self.kat = 1.5*TAU - self.kat

            if aktualny_y >= bariera_y or aktualny_y <= -bariera_y: #góra i dół
                self.kat = TAU - self.kat

        self.add_updater(ruch_czastki)

    def ustaw_kat(self, kat):
        self.kat = kat

    def zwroc_kat(self):
        return self.kat

    def zwroc_promien(self):
        return self.promien


def dystans_ox(czastka1, czastka2):
    return np.absolute(czastka1.get_center()[0] - czastka2.get_center()[0])


class Czastki_odbijajace_sie_w_ox(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ILOSC_CZASTEK = 4 + 2
        WYSUNIECIE_LEWEJ_BARIERY = -3
        WYSUNIECIE_PRAWEJ_BARIERY = 3

        punkt = Dot([-10, -10, 0], color=WHITE)
        punkt.tablica = []

        bariera_lewo_czastka = Czastka(punkt=[WYSUNIECIE_LEWEJ_BARIERY, 0, 0], promien=0, kat=0, predkosc=0, kolor=WHITE)
        bariera_lewo_kreska = Line(start=[WYSUNIECIE_LEWEJ_BARIERY, 0.5, 0], end=[WYSUNIECIE_LEWEJ_BARIERY, -0.5, 0], color=BLACK)
        bariera_lewo = VGroup(bariera_lewo_czastka, bariera_lewo_kreska)

        bariera_prawo_czastka = Czastka(punkt=[WYSUNIECIE_PRAWEJ_BARIERY, 0, 0], promien=0, kat=0, predkosc=0, kolor=WHITE)
        bariera_prawo_kreska = Line(start=[WYSUNIECIE_PRAWEJ_BARIERY, 0.5, 0], end=[WYSUNIECIE_PRAWEJ_BARIERY, -0.5, 0], color=BLACK)
        bariera_prawo = VGroup(bariera_prawo_czastka, bariera_prawo_kreska)

        czastka1 = Czastka(punkt=[-2, 0, 0], promien=0.4, kat=0 * DEGREES, predkosc=0.5, kolor=BLACK)
        czastka2 = Czastka(punkt=[-1, 0, 0], promien=0.2, kat=0 * DEGREES, predkosc=1, kolor=BLACK)
        czastka3 = Czastka(punkt=[0, 0, 0], promien=0.1, kat=180 * DEGREES, predkosc=2, kolor=BLACK)
        czastka4 = Czastka(punkt=[1, 0, 0], promien=0.05, kat=180 * DEGREES, predkosc=4, kolor=BLACK)

        punkt.tablica.append(czastka1)
        punkt.tablica.append(czastka2)
        punkt.tablica.append(czastka3)
        punkt.tablica.append(czastka4)
        punkt.tablica.append(bariera_lewo_czastka)
        punkt.tablica.append(bariera_prawo_czastka)

        def zderzenia_ox(punkt, dt):
            for i in range(ILOSC_CZASTEK):
                for k in range(i):
                    if k != i:
                        suma_promieni = punkt.tablica[i].zwroc_promien() + punkt.tablica[k].zwroc_promien() + 0.01
                        if dystans_ox(punkt.tablica[i], punkt.tablica[k]) <= suma_promieni:
                            punkt.tablica[i].ustaw_kat(punkt.tablica[i].zwroc_kat() + 180 * DEGREES)
                            punkt.tablica[k].ustaw_kat(punkt.tablica[k].zwroc_kat() + 180 * DEGREES)

        punkt.add_updater(zderzenia_ox)

        self.add(punkt)
        self.add(bariera_lewo, bariera_prawo)
        self.add(*punkt.tablica)

        self.wait(20)