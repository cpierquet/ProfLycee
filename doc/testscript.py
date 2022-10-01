# Calcul de la factorielle en langage Python
def factorielle(x):
	if x < 2:
		return 1
	else:
		return x * factorielle(x-1)

# rapidité de tracé
import matplotlib.pyplot as plt
import time
def trace_parabole_tableaux():
	depart=time.clock()
	X = [] # Initialisation des listes
	Y = []
	a = -2
	h = 0.001
	while a<2:
		X.append(a) # Ajout des valeurs
		Y.append(a*a) # au "bout" de X et Y
		a = a+h
	# Tracé de l'ensemble du tableau de valeurs
	plt.plot(X,Y,".b")
	fin=time.clock()
	return "Temps : " + str(fin-depart) + " s."
