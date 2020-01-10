## imports
import math as ma
from numpy import *

def solve_euler_explicit(f, x0, t0, dt, t_tot=2):

	''' Cette fonction renvoie la solution à l'équation différentielle dx/dt = f(x) 
	avec la méthode d'Euler explicite, pour une durée de 1 seconde'''
	#print(f, x0, t0, t_tot, dt)
	N = int(ma.floor(t_tot/dt))
	t,x = t0,1*x0    # Donne le temps actuel et la position
	T = [t]  # Liste de temps
	X = [1*x]  # Liste de positions
	for _ in range(0,N):
		t += dt    # Nouveau temps
		x += dt*f(x)  # Nouvelle position
		T.append(t)
		X.append(1*x)

	return T, X

def Runge_Kutta_2(f, x0, t0, dt, t_tot = 2):

	N = int(ma.floor(t_tot/dt))  # Number of iterations
	t,x = t0,1*x0				# Current time & current position
	X = [1*x]			# Liste de positions
	T = [t]				# Liste de temps

	for k in range(N):
		t += dt
		middle_pos = x + dt/2*f(x)
		x += dt*f(middle_pos)

		T.append(t)
		X.append(1*x)

	return T,X
	
def euler_implicite(f, x0, t0, dt, t_tot = 2):
	N = int(ma.floor(t_tot/dt))  # Number of iterations
	t,x = t0,1*x0				# Current time & current position
	X = [1*x0]			# Liste de positions
	T = [t]				# Liste de temps

	def phi(approx):
		return x + dt*f(approx) 
	for _ in range(N):
		t += dt
		approx_pos = phi(x)
		x = next_step(approx_pos, phi)

		T.append(t)
		X.append(1*x)

	return T,X

def next_step(approx_pos,phi):
	for _ in range(100):
		approx_pos = phi(1*approx_pos)
	temp = phi(approx_pos)
	while linalg.norm(temp-approx_pos)/linalg.norm(approx_pos) > 0.001 :
		approx_pos = 1*temp
		temp = 1*phi(approx_pos)
	return approx_pos
