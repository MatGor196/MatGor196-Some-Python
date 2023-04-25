from manim import *

class Cien_szescianu(ThreeDScene):
    def construct(self):
        osie = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        zrodlo_swiatla = [1.5, 1.5, 2.5]

        lokalizacje1 = [[1, 1, 1], [2, 1, 1], [2, 1, 2], [1, 1, 2]]
        srodek1 = [1.5, 1, 1.5]
        punkty1 = []

        for lokalizacja in lokalizacje1:
            punkty1.append(Dot3D(osie.c2p(*lokalizacja)))

        lokalizacje2 = [[1, 2, 1], [2, 2, 1], [2, 2, 2], [1, 2, 2]]
        srodek2 = [1.5, 2, 1.5]
        punkty2 = []

        for lokalizacja in lokalizacje2:
            punkty2.append(Dot3D(osie.c2p(*lokalizacja)))


        punkty_cien1 = []

        for i in range(4):
            punkty1[i].add_updater(lambda punkt, dt: punkt.rotate(dt * PI, axis=np.array([0, 1, 0]), about_point=osie.c2p(*srodek1)))

        a, b, c = zrodlo_swiatla

        for i in range(4):
            a1, b1, c1 = lokalizacje1[i]
            t = (-c1) / (c - c1)

            cien_lokalizacja = [t*a + (1 - t)*a1, t*b + (1 - t)*b1, 0]
            punkty_cien1.append(Dot(osie.c2p(*cien_lokalizacja), color=GREY))

        def zwroc_updater_punktu_cienia_nr(i):
            def updater_punktu(punkt):
                a1, b1, c1 = punkty1[i].get_center()
                t = (-c1) / (c - c1)

                punkt_lokalizacja = [t * a + (1 - t) * a1, t * b + (1 - t) * b1, 0]
                punkt.move_to(osie.c2p(*punkt_lokalizacja))
            return updater_punktu

        for i in range(4):
            punkty_cien1[i].add_updater(zwroc_updater_punktu_cienia_nr(i))


        punkty_cien2 = []

        for i in range(4):
            punkty2[i].add_updater(lambda punkt, dt: punkt.rotate(dt * PI, axis=np.array([0, 1, 0]), about_point=osie.c2p(*srodek2)))

        for i in range(4):
            a1, b1, c1 = lokalizacje2[i]
            t = (-c1) / (c - c1)

            cien_lokalizacja = [t*a + (1 - t)*a1, t*b + (1 - t)*b1, 0]
            punkty_cien2.append(Dot(osie.c2p(*cien_lokalizacja), color=GREY))

        def zwroc_updater_punktu_cienia_nr(i):
            def updater_punktu(punkt):
                a1, b1, c1 = punkty2[i].get_center()
                t = (-c1) / (c - c1)

                punkt_lokalizacja = [t * a + (1 - t) * a1, t * b + (1 - t) * b1, 0]
                punkt.move_to(osie.c2p(*punkt_lokalizacja))
            return updater_punktu

        for i in range(4):
            punkty_cien2[i].add_updater(zwroc_updater_punktu_cienia_nr(i))


        linie_szescianu1 = [Line(punkty1[0], punkty1[1]),
                            Line(punkty1[1], punkty1[2]),
                            Line(punkty1[2], punkty1[3]),
                            Line(punkty1[3], punkty1[0])]

        linie_szescianu1[0].add_updater(lambda linia: linia.become( Line(punkty1[0], punkty1[1]) ))
        linie_szescianu1[1].add_updater(lambda linia: linia.become(Line(punkty1[1], punkty1[2])))
        linie_szescianu1[2].add_updater(lambda linia: linia.become(Line(punkty1[2], punkty1[3])))
        linie_szescianu1[3].add_updater(lambda linia: linia.become(Line(punkty1[3], punkty1[0])))

        linie_szescianu2 = [Line(punkty2[0], punkty2[1]),
                            Line(punkty2[1], punkty2[2]),
                            Line(punkty2[2], punkty2[3]),
                            Line(punkty2[3], punkty2[0])]

        linie_szescianu2[0].add_updater(lambda linia: linia.become(Line(punkty2[0], punkty2[1])))
        linie_szescianu2[1].add_updater(lambda linia: linia.become(Line(punkty2[1], punkty2[2])))
        linie_szescianu2[2].add_updater(lambda linia: linia.become(Line(punkty2[2], punkty2[3])))
        linie_szescianu2[3].add_updater(lambda linia: linia.become(Line(punkty2[3], punkty2[0])))

        linie_szescianu3 = [Line(punkty1[0], punkty1[1]),
                            Line(punkty1[1], punkty1[2]),
                            Line(punkty1[2], punkty1[3]),
                            Line(punkty1[3], punkty1[0])]

        linie_szescianu3[0].add_updater(lambda linia: linia.become(Line(punkty1[0], punkty2[0])))
        linie_szescianu3[1].add_updater(lambda linia: linia.become(Line(punkty1[1], punkty2[1])))
        linie_szescianu3[2].add_updater(lambda linia: linia.become(Line(punkty1[2], punkty2[2])))
        linie_szescianu3[3].add_updater(lambda linia: linia.become(Line(punkty1[3], punkty2[3])))


        linie_cienia1 = [Line(punkty_cien1[0], punkty_cien1[1], color=GREY),
                            Line(punkty_cien1[1], punkty_cien1[2], color=GREY),
                            Line(punkty_cien1[2], punkty_cien1[3], color=GREY),
                            Line(punkty_cien1[3], punkty_cien1[0], color=GREY)]

        linie_cienia1[0].add_updater(lambda linia: linia.become(Line(punkty_cien1[0], punkty_cien1[1], color=GREY)))
        linie_cienia1[1].add_updater(lambda linia: linia.become(Line(punkty_cien1[1], punkty_cien1[2], color=GREY)))
        linie_cienia1[2].add_updater(lambda linia: linia.become(Line(punkty_cien1[2], punkty_cien1[3], color=GREY)))
        linie_cienia1[3].add_updater(lambda linia: linia.become(Line(punkty_cien1[3], punkty_cien1[0], color=GREY)))

        linie_cienia2 = [Line(punkty_cien2[0], punkty_cien2[1], color=GREY),
                         Line(punkty_cien2[1], punkty_cien2[2], color=GREY),
                         Line(punkty_cien2[2], punkty_cien2[3], color=GREY),
                         Line(punkty_cien2[3], punkty_cien2[0], color=GREY)]

        linie_cienia2[0].add_updater(lambda linia: linia.become(Line(punkty_cien2[0], punkty_cien2[1], color=GREY)))
        linie_cienia2[1].add_updater(lambda linia: linia.become(Line(punkty_cien2[1], punkty_cien2[2], color=GREY)))
        linie_cienia2[2].add_updater(lambda linia: linia.become(Line(punkty_cien2[2], punkty_cien2[3], color=GREY)))
        linie_cienia2[3].add_updater(lambda linia: linia.become(Line(punkty_cien2[3], punkty_cien2[0], color=GREY)))

        linie_cienia3 = [Line(punkty_cien1[0], punkty_cien2[0], color=GREY),
                         Line(punkty_cien1[1], punkty_cien2[1], color=GREY),
                         Line(punkty_cien1[2], punkty_cien2[2], color=GREY),
                         Line(punkty_cien1[3], punkty_cien2[3], color=GREY)]

        linie_cienia3[0].add_updater(lambda linia: linia.become(Line(punkty_cien1[0], punkty_cien2[0], color=GREY)))
        linie_cienia3[1].add_updater(lambda linia: linia.become(Line(punkty_cien1[1], punkty_cien2[1], color=GREY)))
        linie_cienia3[2].add_updater(lambda linia: linia.become(Line(punkty_cien1[2], punkty_cien2[2], color=GREY)))
        linie_cienia3[3].add_updater(lambda linia: linia.become(Line(punkty_cien1[3], punkty_cien2[3], color=GREY)))


        self.add(osie)

        #self.add(Dot3D(osie.c2p(*srodek1), color=BLUE), Dot3D(osie.c2p(*srodek2), color=BLUE))
        self.add(Dot3D(osie.c2p(*zrodlo_swiatla), color=YELLOW))
        self.add(*punkty1)
        self.add(*punkty2)

        self.add(*punkty_cien1)
        self.add(*punkty_cien2)

        self.add(*linie_szescianu1)
        self.add(*linie_szescianu2)
        self.add(*linie_szescianu3)

        self.add(*linie_cienia1)
        self.add(*linie_cienia2)
        self.add(*linie_cienia3)
        
        self.wait(15)