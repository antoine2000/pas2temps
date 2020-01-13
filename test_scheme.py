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
		print(solveur.__name__)
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
		err = linalg.norm(solution(t) - approx[0][int((t-t0)/dt)])
		err = max(err,10^-16)
		if err > err_max :
			err_max = err
	# print(err_max)
	return err_max

def test(solveurs, solution, f, x0 = array([1]), t0 = 0, t_tot = 2):
	plt.figure()
	plt.xlabel("-log(pas de temps)")
	#plt.ylim([0,1])
	plt.ylabel("erreur maximale")
	plt.title("Erreur maximale en fonction du pas de temps choisi pour différents solveurs et la fonction " + f.__name__ + " sur " + str(t_tot) + " secondes")	
	for solveur in solveurs:
		dt = 0.1
		Liste_err = []
		Liste_t = []
		while dt > 10**-2 :
			print(dt)
			Liste_err.append(erreur_max(solveur, solution, f, x0, t0, dt, t_tot))
			Liste_t.append(-ma.log10(dt))
			dt -= 0.5*10**(-3)
		Lissage(Liste_err)
		plt.plot(Liste_t, Liste_err, label = solveur.__name__)
	plt.legend(loc = 0)
	plt.show()

def Lissage(L):
	N = len(L)
	for k in range(30,N):
		L[k] = min(L[k-30:k+1])
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
	
## Tests IVP

def test_ivp(f, f_ex, x0, t0, dt, t_tot):
	dts,ts,xs = solve_ivp_euler_explicit_variable_step_test(f,x0,t0,dt,t_tot)
	F = [f_ex(t) for t in ts]
	plt.figure()
	plt.subplot(2,1,1)
	plt.plot(ts,dts)
	plt.xlabel("temps")
	plt.ylabel("pas de temps choisi")
	plt.subplot(2,1,2)
	plt.plot(ts,xs[0],label='approx')
	plt.plot(ts,F,label='true')
	plt.legend(loc=0)
	plt.xlabel("temps")
	plt.ylabel("solution")
	plt.show()


# tests 1D
#printf([euler_implicite], exp_ex, exp, 1, 0, 1) 
#printf([solve_euler_explicit, Runge_Kutta_2, euler_implicite], carre_ex, carre, 1, 0, 0.1) 
#test([solve_euler_explicit, Runge_Kutta_2, euler_implicite], carre_ex,carre, 1, 0)

#test 2D
#test([solve_ivp_euler_explicit_variable_step, solve_euler_explicit, euler_implicite, Runge_Kutta_2,Runge_Kutta_4], exp_ex,exp, array([1.0]), 0,10)
printf([solve_ivp_euler_explicit_variable_step,solve_euler_explicit,euler_implicite,Runge_Kutta_2, Runge_Kutta_4],cos_ex, cos, array([cos_ex(-6),-ma.sin(6.0)]),-6.0,0.0001,12)
#printf([solve_ivp_euler_explicit_variable_step,solve_euler_explicit,euler_implicite,Runge_Kutta_2, Runge_Kutta_4],exp_ex, exp, array([1.0]),0,0.1,10)
#printf([solve_euler_explicit,Runge_Kutta_2,euler_implicite, Runge_Kutta_4,solve_ivp_euler_explicit_variable_step],carre_ex, carre, array([1.0]),0.0,0.1,12)

#test IVP
#test_ivp(carre,carre_ex,array([1]),0.0,0.01,40)