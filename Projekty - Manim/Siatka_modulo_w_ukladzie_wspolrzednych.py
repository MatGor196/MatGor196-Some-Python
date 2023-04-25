from manim import *


class Scena(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ILE_X = 24
        ILE_Y = 12

        ROZPIECIE_X = 12
        ROZPIECIE_Y = 6
        WYROWNANIE_DO_POCZATKU = False

        SKALA_X = ROZPIECIE_X/ILE_X
        SKALA_Y = ROZPIECIE_Y/ILE_Y

        POCZATEK = [-6, -3, 0]
        KONIEC_OX = [6.5, -3, 0]
        KONIEC_OY = [-6, 3.5, 0]

        # stworzenie osi
        os_x = Arrow(start=POCZATEK, end=KONIEC_OX, buff=0).set_color(BLACK)
        os_y = Arrow(start=POCZATEK, end=KONIEC_OY, buff=0).set_color(BLACK)

        # stworzenie podziałki dla osi x wraz z cyframi
        grupa_osi_x = VGroup()
        for i in range(1, ILE_X + 1):
            linia_dla_cyfry = Line(POCZATEK - 0.1 * DOWN, POCZATEK + 0.1 * DOWN).set_color(BLACK)
            linia_dla_cyfry.shift(RIGHT * i * SKALA_X)
            cyfra = Text(str(i)).next_to(linia_dla_cyfry, DOWN * 0.3).set_color(BLACK).scale(SKALA_X*0.7)
            grupa_osi_x.add(linia_dla_cyfry, cyfra)

        # stworzenie podziałki dla osi y wraz z cyframi
        grupa_osi_y = VGroup()
        for i in range(1, ILE_Y + 1):
            linia_dla_cyfry = Line(POCZATEK - 0.1 * RIGHT, POCZATEK + 0.1 * RIGHT).set_color(BLACK)
            linia_dla_cyfry.shift(UP * i * SKALA_Y)
            cyfra = Text(str(i)).next_to(linia_dla_cyfry, LEFT * 0.3).set_color(BLACK).scale(SKALA_Y*0.7)
            grupa_osi_y.add(linia_dla_cyfry, cyfra)

        # stowrzenie siatki cyfr
        siatka_cyfr = []
        for i in range(ILE_X):
            siatka_cyfr.append([])
            for k in range(ILE_Y):
                siatka_cyfr[i].append((i + k) % 2)

        # stworzenie siatki kwadratów
        Kwadraty = VGroup()
        for i in range(1, ILE_X+1):
            for k in range(1, ILE_Y+1):
                kwadrat = Rectangle(width=SKALA_X, height=SKALA_Y)

                if WYROWNANIE_DO_POCZATKU == True:
                    kwadrat.move_to(POCZATEK - 0.5*SKALA_X*RIGHT - 0.5*SKALA_Y*UP + SKALA_X*i*RIGHT + SKALA_Y*k*UP)
                else:
                    kwadrat.move_to(POCZATEK + SKALA_X * i * RIGHT + SKALA_Y * k * UP)

                if siatka_cyfr[i-1][k-1] == 0:
                    kwadrat.set_fill(color=BLUE, opacity=1)
                else:
                    kwadrat.set_fill(color=GREY, opacity=1)
                Kwadraty.add(kwadrat)

        self.add(Kwadraty, os_x, os_y, grupa_osi_x, grupa_osi_y)

        self.wait()