from manim import *


class Scena(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        osie = Axes(
            x_range=[0, 100],
            y_range=[0, 100],
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": False,
                         "color": WHITE,
                         "include_tip": False,
                         "tick_size": 0.02})

        punkty = VGroup()

        for i in range(101):
            for k in range(101):
                kwadrat = Square(color=BLACK, fill_opacity=funkcja(i, k))
                kwadrat.move_to(osie.c2p(i, k))
                kwadrat.set_stroke(width=0)
                kwadrat.scale(0.03)
                punkty.add(kwadrat)

        self.add(osie, punkty)
        self.wait()


def funkcja(n, m):
    lista_n = [int(str_cyfra) for str_cyfra in str(n)]
    lista_m = [int(str_cyfra) for str_cyfra in str(m)]
    ilosc_cyfr_n = len(lista_n)
    ilosc_cyfr_m = len(lista_m)
    nww = NWW(ilosc_cyfr_n, ilosc_cyfr_m)

    os_x = []
    os_y = []
    for i in range(nww):
        os_x.append(lista_n[i % ilosc_cyfr_n])
        os_y.append(lista_m[i % ilosc_cyfr_m])

    ilosc_parzystych = 0

    for i in range(nww):
        for k in range(nww):
            if (os_x[i] + os_y[k]) % 2 == 0:
                ilosc_parzystych += 1
    return ilosc_parzystych / (nww * nww)


def NWW(x, y):
    if x > y:
        wiekszy = x
    else:
        wiekszy = y

    while True:
        if ((wiekszy % x == 0) and (wiekszy % y == 0)):
            nww = wiekszy
            break
        wiekszy += 1

    return nww
