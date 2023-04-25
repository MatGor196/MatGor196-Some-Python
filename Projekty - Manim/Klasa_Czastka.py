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