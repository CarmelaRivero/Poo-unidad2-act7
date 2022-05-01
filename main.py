from Viajero import Viajero
from os import path

if __name__ == '__main__':
	viajeros = Viajero.leerArchivo(path.dirname(__file__) + "/viajeros.csv")

	viajero = viajeros[0]

	print(viajero == viajeros[0])
	print(viajero == viajeros[1])
	print(viajero == 100)
	print(viajero == 200)

	viajero = 100 + viajero
	viajero.mostrar()

	viajero = 100 - viajero
	viajero.mostrar()
