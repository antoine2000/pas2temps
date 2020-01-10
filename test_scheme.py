# Imports
import math as ma
import matplotlib.pyplot as plt
from numpy import *
# Fonctions de test

def printf(solveurs, true_f, f, x0, t0, dt, t_tot=2):
	plt.figure()
	plt.xlabel("t")
	plt.ylabel("Solution")
	plt.title(f.__name__ + " simulée sur " + str(t_tot) + " secondes avec un pas de temps de " + str(dt))	
	for solveur in solveurs:
		T, X = solveur(f,x0,t0,dt,t_tot)
		F = [true_f(t) for t in T]
		plt.plot(T, X[0], label = solveur.__name__)
	plt.plot(T, F, label = 'true')
	plt.legend(loc=0)
	plt.show()

def erreur_max(solveur, solution, f, x0, t0, dt, t_tot=2):
	T,approx = solveur(f, x0, t0, dt, t_tot)
	err_max = 0
	for t in T:
		err = linalg.norm(solution(t) - approx[int(t/dt)][0])
		if err > err_max :
			err_max = err
	return err_max

def test(solveurs, solution, f, x0 = array([1]), t0 = 0, t_tot = 2):
	plt.figure()
	plt.xlabel("-log(pas de temps)")
	plt.ylim([0,0.4])
	plt.ylabel("erreur maximale")
	plt.title("Erreur maximale en fonction du pas de temps choisi pour différents solveurs et la fonction " + f.__name__ + " sur " + str(t_tot) + " secondes")	
	for solveur in solveurs:
		dt = 1
		Liste_err = []
		Liste_t = []
		while dt > 10**-4 :
			Liste_err.append(erreur_max(solveur, solution, f, x0, t0, dt, t_tot))
			Liste_t.append(-ma.log10(dt))
			dt /= 1.01
		Lissage(Liste_err)
		plt.plot(Liste_t, Liste_err, label = solveur.__name__)
	plt.legend(loc = 0)
	plt.show()

def Lissage(L):
	N = len(L)
	for k in range(20,N):
		L[k] = min(L[k-19:k+1])
''' Les fonctions exactes sont doublées de la mention ex'''

def exp(x):
	return x

def exp_ex(t):
	return ma.exp(t)

def carre(x):
	return 2*ma.sqrt(abs(x))

def carre_ex(t):
	return t**2

def cos_ex(t):
	return ma.cos(t)

def cos(xy):
	x, y = xy
	return array([y,-x])
	

# tests 1D
#printf([euler_implicite], exp_ex, exp, 1, 0, 1) 
#printf([solve_euler_explicit, Runge_Kutta_2, euler_implicite], carre_ex, carre, 1, 0, 0.1) 
#test([solve_euler_explicit, Runge_Kutta_2, euler_implicite], carre_ex,carre, 1, 0)

#test 2D
#test([solve_euler_explicit, Runge_Kutta_2, euler_implicite], cos_ex,cos, array([1,0],dtype = float64), 0)
#printf([solve_euler_explicit,Runge_Kutta_2,euler_implicite],cos_ex, cos, array([[cos_ex(-6.0)],[-ma.sin(-6.0)]]),-6.0,0.01,12)
#printf([solve_euler_explicit,Runge_Kutta_2,euler_implicite],exp_ex, exp, array([[1.0]]),0.0,0.01,12)
