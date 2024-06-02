
from Nim import Nim


class Consola:

    def __init__(self):
        self.Nim: Nim = Nim()
        self.opciones = {
            "1": self.iniciar_nuevo_juego,
            "2": self.salir
        }

    @staticmethod
    def mostrar_menu():
        titulo = "Nim"
        print(f"\n{titulo:_^80}")
        print("1. Iniciar nuevo juego")
        print("2. Salir")
        print(f"{'_':_^30}")

    def iniciar_nuevo_juego(self):
        while True:
            try:
                numero_filas = int(input("Ingresa el numero de filas del tablero (entre 4 y 15): "))
                if 3 <= numero_filas <= 15:
                    numero_columnas = []
                    for i in range(numero_filas):
                        while True:
                            try:
                                columnas = int(input(f"Ingrese el número de pilas para la fila {i + 1} (entre 1 y 10): "))
                                if 1 <= columnas <= 10:
                                    numero_columnas.append(columnas)
                                    break
                                else:
                                     print("El número de pilas debe estar entre 1 y 10.")
                            except ValueError:
                                print("Ingresa un número válido.")

                    self.Nim.iniciar_partida(numero_filas, numero_columnas)
                    break

                        
                          # Terminamos el ciclo while porque hemos creado un tablero válido
                else:
                    print("El tamaño del tablero debe estar entre 4 y 15.")
            except ValueError:
                    print("Ingresa un número válido.")

        

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opccion = input("Seleccione una opción: ")
            if opccion == "1":
                self.iniciar_nuevo_juego()
            else:
              print (f"{opccion} no es una opción válida")
             



    def salir(self):
        print("Gracias por jugar Nim.")
        exit()