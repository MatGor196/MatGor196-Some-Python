from manim import *
import random as r
import math
from numpy import *

class Bladzenie_losowe(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        LICZBA_KROPEK = 5
        PROMIEN_KROPKI = 0.4
        DLUG_LINII = 0.5
        # mnożnik
        M_CZASU_ANIMACJI = 0.5

        kropki = []
        linie = []

        kropki.append(Dot(point=array([0, 0, 0]), radius=PROMIEN_KROPKI).set_fill(color=BLACK))

        x=0
        y=0
        for i in range(LICZBA_KROPEK-1):
            losowa_liczba = r.randrange(0, 360)
            kat = (losowa_liczba/360)*2*PI
            x += math.cos(kat)*DLUG_LINII
            y += math.sin(kat)*DLUG_LINII
            nowa_kropka = Dot(point=array([x, y, 0]), radius=PROMIEN_KROPKI).set_fill(color=BLACK)
            kropki.append(nowa_kropka)

        for i in range(LICZBA_KROPEK-1):
            linie.append(Line(kropki[i], kropki[i+1]).set_stroke(color=BLACK))

        self.add(kropki[0])
        for i in range(LICZBA_KROPEK-1):
            self.play(Create(linie[i]), run_time=M_CZASU_ANIMACJI)
            self.add(kropki[i+1])
        self.wait()