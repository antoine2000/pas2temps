## imports
import math as ma

def solve_euler_explicit(f, x0, dt):

	''' Cette fonction renvoie la solution à l'équation différentielle dx/dt = f(x) 
	avec la méthode d'Euler explicite, pour une durée de 1 seconde'''

	N = ma.floor(1/dt)

	t = 0    # Donne le temps actuel
	T = [0]  # Liste de temps
	x = x0   # Donne la position actuelle
	X = [x]  # Liste de positions

	for k in range(0,N):
		t += dt    # Nouveau temps
		x += f(x)  # Nouvelle position
		T.append(t)
		X.append(x)

	return T, X


