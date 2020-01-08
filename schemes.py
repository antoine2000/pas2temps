## imports
import math as ma

def solve_euler_explicit(f, x0, dt, t_tot=2):

	''' Cette fonction renvoie la solution à l'équation différentielle dx/dt = f(x) 
	avec la méthode d'Euler explicite, pour une durée de 1 seconde'''

	N = ma.floor(t_tot/dt)

	t = 0    # Donne le temps actuel
	T = [0]  # Liste de temps
	x = x0   # Donne la position actuelle
	X = [x]  # Liste de positions

	for k in range(0,N):
		t += dt    # Nouveau temps
		x += dt*f(x)  # Nouvelle position
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
	
def Runge_Kutta_2(f, x0, dt, t_tot = 2):

	N = ma.floor(t_tot/dt)  # Number of iterations
	t = 0				# Current time
	x = x0				# Current position

	X = [x0]			# Liste de positions
	T = [t]				# Liste de temps

	for k in range(N):
		t += dt
		middle_pos = x + dt/2*f(x)
		x += dt*f(middle_pos)

		T.append(t)
		X.append(x)

	return T,X
	
def euler_implicite():
	return 42
