## imports
import math as ma
from numpy import *

def solve_euler_explicit(f, x0, t0, dt, t_tot=2):

	''' Cette fonction renvoie la solution à l'équation différentielle dx/dt = f(x) 
	avec la méthode d'Euler explicite, pour une durée de t_tot seconde'''
	
	N = int(ma.floor(t_tot/dt))
	t,x = t0,1*x0    # Donne le temps actuel et la position
	T = [t]  # Liste de temps
	X = array(x)  # Liste de positions
	for _ in range(0,N):
		t += dt    # Nouveau temps
		x += dt*f(x)  # Nouvelle position
		T = vstack([T,t])
		X = vstack([X,x])

	return T, X.T

def Runge_Kutta_2(f, x0, t0, dt, t_tot = 2):

	N = int(ma.floor(t_tot/dt))  # Number of iterations
	t,x = t0,1*x0				# Current time & current position
	X = array(x)			# Liste de positions
	T = [t]				# Liste de temps

	for k in range(N):
		t += dt
		middle_pos = x + dt/2*f(x)
		x += dt*f(middle_pos)

		T = vstack([T,t])
		X = vstack([X,x])

	return T,X.T

def Runge_Kutta_4(f, x0, t0, dt, t_tot = 2):

	N = int(ma.floor(t_tot/dt))  # Number of iterations
	t,x = t0,1*x0				# Current time & current position
	X = array(x)			# Liste de positions
	T = [t]				# Liste de temps

	for k in range(N):
		t += dt
		middle_pos_1 = f(x)
		middle_pos_2 = f(x + dt/2*middle_pos_1)
		middle_pos_3 = f(x + dt/2*middle_pos_2)
		middle_pos_4 = f(x + dt*middle_pos_3)
		x += dt/6*(middle_pos_1 + 2*middle_pos_2 + 2*middle_pos_3 + middle_pos_4)

		T = vstack([T,t])
		X = vstack([X,x])

	return T,X.T

def euler_implicite(f, x0, t0, dt, t_tot = 2):
	N = int(ma.floor(t_tot/dt))  # Number of iterations
	t,x = t0,1*x0				# Current time & current position
	X = array(x)			# Liste de positions
	T = [t]				# Liste de temps

	def phi(approx):
		return x + dt*f(approx) 
	for _ in range(N):
		#print(_)
		t += dt
		approx_pos = phi(x)
		x = next_step(approx_pos, phi)
		T = vstack([T,t])
		X = vstack([X,x])

	return T,X.T

def next_step(approx_pos,phi):
	for _ in range(10):
		approx_pos = phi(1*approx_pos)
	temp = phi(approx_pos)
	while linalg.norm(temp-approx_pos)/linalg.norm(approx_pos) > 0.1 :
		approx_pos = 1*temp
		temp = 1*phi(approx_pos)
	return approx_pos

def solve_ivp_euler_explicit_variable_step(f, x0, t0, dtmax, t_f, dtmin = 1e-16, atol = 1e-6):
	dt = dtmax/10; # initial integration step
	ts, xs = [t0], [1*x0]  # storage variables
	t = t0
	ti = 0  # internal time keeping track of time since latest storage point : must remain below dtmax
	x = x0
	while ts[-1] < t_f:
		while ti < dtmax:
			t_next, ti_next, x_next = t + dt, ti + dt, x + dt * f(x)
			x_back = x_next - dt * f(x_next)
			ratio_abs_error = atol / (linalg.norm(x_back-x)/2)
			dt = 0.9 * dt * sqrt(ratio_abs_error)
			if dt < dtmin:
				raise ValueError("Time step below minimum")
			elif dt > dtmax/2:
				dt = dtmax/2
			t, ti, x = t_next, ti_next, x_next
		dt2DT = dtmax - ti # time left to dtmax
		t_next, ti_next, x_next = t + dt2DT, 0, x + dt2DT * f(x)
		ts = vstack([ts,t_next])
		xs = vstack([xs,x_next])
		t, ti, x = t_next, ti_next, x_next
	return (ts, xs.T)
		
def solve_ivp_euler_explicit_variable_step_test(f, x0, t0, dtmax, t_f, dtmin = 1e-16, atol = 1e-6):
	dt = dtmax/10; # initial integration step
	dts, ts, xs = [dt], [t0], [x0]  # storage variables
	N = (t_f-t0)/dtmax
	atol = min(1e-6,1/N)
	t = t0
	ti = 0  # internal time keeping track of time since latest storage point : must remain below dtmax
	x = x0
	while ts[-1] < t_f:
		print(ts[-1])
		while ti < dtmax:
			t_next, ti_next, x_next = t + dt, ti + dt, x + dt * f(x)
			x_back = x_next - dt * f(x_next)
			ratio_abs_error = atol / (linalg.norm(x_back-x)/2)
			dt = 0.9 * dt * sqrt(ratio_abs_error)
			if dt < dtmin:
				raise ValueError("Time step below minimum")
			elif dt > dtmax/2:
				dt = dtmax/2
			t, ti, x = t_next, ti_next, x_next
		dts = vstack([dts,dt])
		dt2DT = dtmax - ti # time left to dtmax
		t_next, ti_next, x_next = t + dt2DT, 0, x + dt2DT * f(x)
		ts = vstack([ts,t_next])
		xs = vstack([xs,x_next])
		t, ti, x = t_next, ti_next, x_next
	return (dts, ts, xs.T)
