# Imports
import math as ma
import matplotlib.pyplot as plt

# Fonctions de test

def printf(solveurs, true_f, f, x0, dt, t_tot=2):
	plt.figure()
	plt.xlabel("t")
	plt.ylabel("Solution")
	plt.title(f.__name__ + " simulée sur " + str(t_tot) + " secondes")	
	for solveur in solveurs:
		T, X = solveur(f,x0,dt,t_tot)
		F = [true_f(t) for t in T]
		plt.plot(T, X, label = solveur.__name__)
		plt.plot(T, F)
	plt.legend(loc=0)
	plt.show()

def erreur_max(solveur, solution, f, x0, dt, t_tot=2):
	T,approx = solveur(f, x0, dt, t_tot)
	err_max = 0
	for t in T:
		err = solution(t) - approx[int(t/dt)]
		if abs(err) > err_max :
			err_max = abs(err)
	return err_max

def test(solveurs, solution, f, x0 = 1, t_tot = 2):
	plt.figure()
	plt.xlabel("-log(pas de temps)")
	plt.ylabel("erreur maximale")
	plt.title("Erreur maximale en fonction du pas de temps choisi pour différents solveurs et la fonction " + f.__name__ + " sur " + str(t_tot) + " secondes")	
	for solveur in solveurs:
		dt = 1
		Liste_err = []
		Liste_t = []
		while dt > 10**-2 :
			Liste_err.append(erreur_max(solveur, solution, f, x0, dt, t_tot))
			Liste_t.append(-ma.log10(dt))
			dt /= 1.01
		plt.plot(Liste_t, Liste_err, label = solveur.__name__)
	plt.legend(loc = 0)
	plt.show()

''' Les fonctions exactes sont doublées de la mention ex'''

def exp(x):
	return x

def exp_ex(t):
	return ma.exp(t)

def carre(x):
	return 2*ma.sqrt(abs(x))

def carre_ex(t):
	return (t+1)**2



test([solve_euler_explicit, Runge_Kutta_2], exp_ex,exp, 1)
