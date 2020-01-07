## imports
import math as ma

def solve_euler_explicit(f, x0, dt):

	''' Cette fonction renvoie la solution à l'équation différentielle dx/dt = f(x) 
	avec la méthode d'Euler explicite, pour une durée de 1 seconde'''

	N = ma.floor(2/dt)

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

def erreur_max(solution, f, x0, dt):
	T,approx = solve_euler_explicit(f, x0, dt)
	err_max = 0
	for t in T:
		err = solution(t) - approx[t/dt]
		if abs(err) > err_max :
			err_max = abs(err)
	return err_max
