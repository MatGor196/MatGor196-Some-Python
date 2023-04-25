from manim import *

class TworzenieParaboli(Scene):
    def construct(self):
        self.camera.background_color = WHITE    #kolor tła: biały

        #definiujemy układ współrzędnych
        osie = Axes(x_range=[-2, 9, 1],
                    y_range=[-2, 9, 1],
                    x_length=7,
                    y_length=7,
                    axis_config={"color": BLACK,
                                 "include_numbers": True,
                                 "tip_width": 0.03,
                                 "tip_height": 0.03})

        #zmiana koloru i rozmiaru etykiet (z jakiegoś powodu 'axis_config' tego nie robi)
        dwie_osie = osie.get_axes()
        for os in dwie_osie:
            for numer in os.numbers:
                numer.set_color(BLACK)
                numer.scale(0.8)

        #przygotowanie wykresu paraboli do użytku, ogniska i kierownicy
        #działa na konkretnej paraboli i wyliczonej dla niej ogniska i kierownicy
        wykres_x_2 = osie.get_graph(lambda x: 0.2*(x-2)**2+0.9, color=GREEN, x_range=[-2, 8])
        wykres_kierownicy = osie.get_graph(lambda x: -0.35, color=RED)
        ognisko = Dot(osie.c2p(2, 2.15), color=RED)
        punkt_kierownicy = Dot(osie.c2p(-2, -0.35), color=RED)  #porusza się razem z linią prostopadłą do kierownicy

        #przygotowanie elementów do animacji paraboli
        punkt = Dot(osie.c2p(-2, 4.1), color=DARK_BLUE)
        linia1 = Line(punkt.get_center(), ognisko.get_center(), color=BLUE)
        linia2 = Line(punkt.get_center(), punkt_kierownicy.get_center(), color=BLUE)
        kolo = Circle(radius=punkt.get_center()[1]+0.35, color=BLUE)
        kolo.move_to(punkt.get_center())

        #inicjalizacja i przypisanie wszystkich koniecznych updaterów
        def updater_pkt_kierownicy(pk):
            nowy_punkt = Dot(punkt.get_center(), color=RED)
            nowy_punkt.move_to(osie.c2p(osie.p2c(punkt.get_center())[0],-0.35))
            pk.become(nowy_punkt)

        def updater_kola(k):
            nowe_kolo = Circle(radius=punkt.get_center()[1]-punkt_kierownicy.get_center()[1], color=BLUE)
            nowe_kolo.move_to(punkt.get_center())
            k.become(nowe_kolo)

        punkt_kierownicy.add_updater(updater_pkt_kierownicy)
        kolo.add_updater(updater_kola)

        linia1.add_updater(lambda l1: l1.become(Line(punkt.get_center(), ognisko.get_center(), color=BLUE)))
        linia2.add_updater(lambda l2: l2.become(Line(punkt.get_center(), punkt_kierownicy.get_center(), color=BLUE)))


        # specjalna scieżka tworząca się za punktem poruszającym się po wykresie paraboli
        sciezka = VMobject(color=GREEN)
        sciezka.set_points_as_corners([punkt.get_center(), punkt.get_center()])

        def updater_sciezki(sciezka):
            nastepna_sciezka = sciezka.copy()
            nastepna_sciezka.add_points_as_corners([punkt.get_center()])
            sciezka.become(nastepna_sciezka)
        
        sciezka.add_updater(updater_sciezki)

        #przygotowanie dwóch grup do animacji
        kierownica_ognisko = VGroup()
        kierownica_ognisko.add(ognisko, wykres_kierownicy)

        grupa_animacji = VGroup()
        grupa_animacji.add(linia1, linia2, kolo, punkt_kierownicy)

        #właściwa animacja
        self.wait()
        self.play(Create(osie))
        self.play(Create(kierownica_ognisko))
        self.add(punkt)
        self.add(sciezka)   #dodanie scieżki jaka ma być tworzona, a nie paraboli samej w sobie
        self.play(Create(grupa_animacji))
        self.add(ognisko)   #po to by wyciągnąć ognisko i punkt na przód
        self.add(punkt)
        self.wait()
        self.play(MoveAlongPath(punkt, wykres_x_2), rate_func=linear, run_time=6) #właściwa animacja tworzenia paraboli
        self.wait()