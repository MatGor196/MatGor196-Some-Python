from manim import *


class Podwojne_wahadlo(Scene):
	def construct(self):

		self.theta1 = 70*DEGREES
		self.theta2 = -30*DEGREES
		self.predkosc1 = 1
		self.predkosc2 = 1
		czas_animacji = 60

		# konstrukcja wahadła: 3 punkty połączone trzema liniami
		zaczepienie = Dot([0, 2, 0], radius=0.07, color = GRAY)
		punkt1 = Dot(zaczepienie.get_center() + [L1 * np.sin(self.theta1), -L1 * np.cos(self.theta1), 0], radius=0.07, color=GRAY)
		punkt2 = Dot(punkt1.get_center() + [L2 * np.sin(self.theta2), -L2 * np.cos(self.theta2), 0], radius=0.07, color=GRAY)

		# ścieżka poruszająca się za końcem wachadła
		sciezka = VMobject(color=BLUE)
		sciezka.set_points_as_corners([punkt2.get_center(), punkt2.get_center()])

		def updater_sciezki(sciezka):
			nastepna_sciezka = sciezka.copy()
			nastepna_sciezka.add_points_as_corners([punkt2.get_center()])
			sciezka.become(nastepna_sciezka)

		sciezka.add_updater(updater_sciezki)

		# dwa punkty poruszają się w zależności od wartości kąta theta1 i theta2 (mierzone od dołu osi Y przeciwnie do ruchu wskazówek zegara)
		def updater_punktu1(punkt1):
			punkt1.become(Dot(zaczepienie.get_center() + [L1 * np.sin(self.theta1), -L1 * np.cos(self.theta1), 0], radius=0.07, color=GRAY))

		def updater_punktu2(punkt2):
			punkt2.become(Dot(punkt1.get_center() + [L2 * np.sin(self.theta2), -L2 * np.cos(self.theta2), 0], radius=0.07, color=GRAY))

		# linie po prostu poruszają się za punktami
		linia1 = Line(zaczepienie.get_center(), punkt1.get_center())
		linia2 = Line(punkt1.get_center(), punkt2.get_center())
		linia1.add_updater(lambda l: l.become(Line(zaczepienie.get_center(), punkt1.get_center())))
		linia2.add_updater(lambda l: l.become(Line(punkt1.get_center(), punkt2.get_center())))

		# punkt, którego jedynym zadaniem jest zapewnić updater do aktualizacji wartości theta1 i theta2
		do_obliczen = Dot([-20, -20, 0], color=BLACK)

		def obliczenia(punkt, dt):
			punkt.become(punkt)
			self.theta1, self.theta2, self.predkosc1, self.predkosc2 = nastepne_wartosci(self.theta1, self.theta2, self.predkosc1, self.predkosc2)

		do_obliczen.add_updater(obliczenia)

		# dodanie wszystkiego
		self.add(do_obliczen, sciezka, linia1, linia2, zaczepienie, punkt1, punkt2)

		# rozpoczęcie właściwej animacji
		self.wait()
		punkt1.add_updater(updater_punktu1)
		punkt2.add_updater(updater_punktu2)
		self.wait(czas_animacji)
		punkt1.remove_updater(updater_punktu1)
		punkt2.remove_updater(updater_punktu2)
		self.wait()

# stałe globalne używane zarówno w równaniach jak i do konstrukcji wahadła
L1 = 2
L2 = 2
m1 = 1
m2 = 1
g = 9.81	#stała grawitacji
delta = 0.01	#dokładność poruszania się punktu

"""
funkcje zapewniające na podstawie rozwiązań równań różniczkowych aktualizowane w każdej mikro jednostce czasu wartości kątów
najpierw wyliczane jest przyspieszenie obu thet (przyspieszenie kątowe punktów), potem ich prędkości (również kątowe), a potem nowe thety
całość powtarzana rekurencyjnie w zależności od kątów i prędkości ich zmiany
Równania z: https://www.myphysicslab.com/pendulum/double-pendulum-en.html
"""
def nastepne_wartosci(theta1, theta2, theta1_prim, theta2_prim):

	licznik1 = -g*(2*m1 + m2)*np.sin(theta1) - m2*g*np.sin(theta1 - 2*theta2) - 2*np.sin(theta1-theta2)*m2*((theta2_prim**2)*L2 + (theta1_prim**2)*L1*np.cos(theta1-theta2))
	mianownik1 = L1*(2*m1+m2 - m2*np.cos(2*theta1-2*theta2))

	licznik2 = 2*np.sin(theta1-theta2)*((theta1_prim**2)*L1*(m1 + m2) + g*(m1 + m2)*np.cos(theta1) + (theta2_prim**2)*L2*m2*np.cos(theta1-theta2))
	mianownik2 = L2*(2*m1 + m2 - m2*np.cos(2*theta1-2*theta2))

	theta1_bis = licznik1 / mianownik1
	theta2_bis = licznik2 / mianownik2

	nastepna_theta1_prim = theta1_prim + (delta * theta1_bis)
	nastepna_theta2_prim = theta2_prim + (delta * theta2_bis)

	nastepna_theta1 = theta1 + (delta * nastepna_theta1_prim)
	nastepna_theta2 = theta2 + (delta * nastepna_theta2_prim)

	return nastepna_theta1, nastepna_theta2, nastepna_theta1_prim, nastepna_theta2_prim