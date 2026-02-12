import sys

def afd(entrada):
	#Transiciones
	trans={	 'q1': {'0': 'q2', '1': 'q3'},
		 'q2': {'0': 'q2', '1': 'q2'},
		 'q3': {'0': 'q3', '1': 'q3'}
	      }
	# El estado inicial es q1
	q='q1' 
	# El estado de aceptacion es q2
	qf='q2'
	for e in entrada:
		q=trans[q][e]
	if q == qf:
		print("ACEPTADO")
	else:
		print("NO ACEPTADO")
try:
	if len(sys.argv) > 1:
		entrada = sys.argv[1]
		with open(entrada, 'r') as en:
			datos = en.read().split()
			for i in datos:
				afd(i)
	else:
		print("No se detectó archivo de entrada")

except:
	print(" No se encontró el archivo")
