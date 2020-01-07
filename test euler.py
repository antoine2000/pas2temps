# Imports
import math as ma
import matplotlib.pyplot as plt

# Fonctions de test

def erreur_max(solution, f, x0, dt):
	T,approx = solve_euler_explicit(f, x0, dt)
	err_max = 0
	for t in T:
		err = solution(t) - approx[int(t/dt)]
		if abs(err) > err_max :
			err_max = abs(err)
	return err_max

def test(solution, f, x0 = 1):
	dt = 1
	Liste_err = []
	Liste_t = []
	while dt > 10**-2 :
		#print (dt)
		Liste_err.append(erreur_max(solution, f, x0, dt))
		Liste_t.append(-ma.log10(dt))
		dt /= 1.00001
	plt.figure()
	plt.xlabel("-log(pas de temps)")
	plt.ylabel("erreur maximale")
	plt.title("Erreur maximale en fonction du pas de temps choisi pour le schéma d'euler et la fonction " + f.__name__ + " sur 2 secondes")
	plt.plot(Liste_t, Liste_err)
	plt.show()

''' Les fonctions exactes sont doublées de la mention ex'''

def exp(x):
	return x

def exp_ex(t):
	return ma.exp(t)

def carre(x):
	return 1/2*ma.sqrt(abs(x))

def carre_ex(t):
	return t**2



test(exp_ex, exp, 0)

