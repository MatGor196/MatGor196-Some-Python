from manim import *

class NOS(ThreeDScene):
    def construct(self):
        osie = ThreeDAxes(x_range = [0, 3, 1], y_range = [0, 3, 1], z_range = [0, 2, 1],
                          x_length = 4, y_length = 4, z_length = 3)

        self.set_camera_orientation(phi=60*DEGREES, theta=60*DEGREES)

        ox = osie.get_x_axis_label(Tex("x"))
        oy = osie.get_y_axis_label(Tex("y"))
        oz = osie.get_z_axis_label(Tex("z"))

        pa1 = Dot([1,1,2])
        pa2 = Dot([1,2,2])
        pa3 = Dot([1,2,1])
        pa4 = Dot([1,1,1])

        pb1 = Dot([2,1,2])
        pb2 = Dot([2,2,2])
        pb3 = Dot([2,2,1])
        pb4 = Dot([2,1,1])

        linia12a = Line([1,1,2], [1,2,2])
        linia23a = Line([1,2,2], [1,2,1])
        linia34a = Line([1,2,1], [1,1,1])
        linia41a = Line([1,1,1], [1,1,2])

        linia12b = Line([2,1,2], [2,2,2])
        linia23b = Line([2,2,2], [2,2,1])
        linia34b = Line([2,2,1], [2,1,1])
        linia41b = Line([2,1,1], [2,1,2])

        linia1ab = Line([1,1,2], [2,1,2])
        linia2ab = Line([1,2,2], [2,2,2])
        linia3ab = Line([1,2,1], [2,2,1])
        linia4ab = Line([1,1,1], [2,1,1])

        Linie_pomiedzy = VGroup(linia1ab, linia2ab, linia3ab, linia4ab)
        Linie_b = VGroup(linia12b, linia23b, linia34b, linia41b)
        Linie_a = VGroup(linia12a, linia23a, linia34a, linia41a)
        Punkty_a = VGroup(pa1, pa2, pa3, pa4)
        Punkty_b = VGroup(pb1, pb2, pb3, pb4)

        self.add(osie, ox, oy, oz)
        self.add(Linie_pomiedzy, Linie_a, Linie_b, Punkty_a, Punkty_b)
        self.wait(0.5)
        Linie_pomiedzy.add_updater(lambda obj, dt: obj.rotate(dt * 90 * DEGREES))
        Linie_b.add_updater(lambda obj, dt: obj.rotate(dt * 90 * DEGREES))
        Linie_a.add_updater(lambda obj, dt: obj.rotate(dt * 90 * DEGREES))
        Punkty_a.add_updater(lambda obj, dt: obj.rotate(dt * 90 * DEGREES))
        Punkty_b.add_updater(lambda obj, dt: obj.rotate(dt * 90 * DEGREES))
        self.wait(15)