from Tablero import Tablero
import copy


class Nim:

    def __init__(self) -> None:
        self.tablerito = Tablero()
        self.turno = 0
        self.profundidad = 10

    def solo_queda_una_casilla(self, tablero):
        if self.quedaUnaPila(tablero):
            return "Jugador" if self.turno == 1 else "IA"
        return None

    def minimax(self, tablero, is_maximizador):
        resultado = self.evaluar(tablero, is_maximizador)   
        if resultado is not None:
            return resultado    


        movimientos = self.obtenerMovimientos(tablero)
        if not movimientos :
            return 0

        if is_maximizador:
            mejorPuntaje = -float('inf')
            for movimiento in movimientos:
                fila, cantidad = movimiento
                tablero_copia = copy.deepcopy(tablero)
                self.movimientoJugador(tablero_copia, fila, cantidad)
                puntaje = self.minimax(tablero_copia, False)

                mejorPuntaje = max(mejorPuntaje, puntaje)

            return mejorPuntaje
        else:
            peor_puntaje = float('inf')
            for movimiento in movimientos:
                fila, cantidad = movimiento
                nuevo_tablero = copy.deepcopy(tablero)
                self.movimientoJugador(nuevo_tablero, fila, cantidad)
                puntaje = self.minimax(nuevo_tablero, True)

                peor_puntaje = min(peor_puntaje, puntaje)

            return peor_puntaje

    def obtenerMovimientos(self, tablero):
        movimientos = []
        for fila, pilas in tablero.informacion_tablero.items():
            for cantidad in range(1, pilas + 1):
                movimientos.append((fila, cantidad))
        return movimientos


    def vacio(self, tablero):
        return all(len(fila) == 0 for fila in tablero.tablero)


 

    def crearTablero(self, numeroFilas: int, numeroColumnas: list):
        self.tablerito.crearTablero(numeroFilas, numeroColumnas)

    def movimientoJugador(self, tablero, fila: int, cantidad: int):
        tablero.eliminar_pilas(fila, cantidad)

    def mostrarTablero(self):
        self.tablerito.imprimirTablero()

    def movimientoIA(self):
        mejorPuntaje = float('-inf')
        mejorMovimiento = None

        movimientos = self.obtenerMovimientos(self.tablerito)


        for movimiento in movimientos:
            fila, cantidad = movimiento
            tablero_copia = copy.deepcopy(self.tablerito)
            tablero_copia.eliminar_pilas(fila, cantidad)
            puntaje = self.minimax(tablero_copia, False)
            if puntaje > mejorPuntaje:
                mejorPuntaje = puntaje
                mejorMovimiento = movimiento

        if mejorMovimiento:
            fila, cantidad = mejorMovimiento

            self.movimientoJugador(self.tablerito, fila, cantidad)
            return True
        return False

    def cambioTurno(self):
        self.turno = 1 if self.turno == 0 else 0

    def evaluar(self, tablero, maximizador):
        if self.vacio(tablero):
            return 10 if maximizador else -10
        return None
    

    def ganador(self, tablero):
        if self.vacio(tablero):
            return "Jugador" if self.turno == 0 else "IA"
        return None
        
    def jugar_partida(self):
        while True:
            print("\n")
            self.mostrarTablero()
        
            

            if self.turno == 0:
                print("Es tu turno!")
                try:
                    fila = int(input("\nIngresa la fila: "))
                    pilas = int(input("\nIngresa la cantidad de pilas a quitar: "))
                    self.movimientoJugador(self.tablerito, fila, pilas)
                except (ValueError, IndexError) as e:
                    print(f"Error: {e}. Por favor, ingresa un número válido.")
                    continue

            if self.turno == 1:
                print("Turno de la IA!")
                print("\nEspera un momento...")
                self.movimientoIA()

            if self.vacio(self.tablerito):
                perdedor = self.ganador(self.tablerito)
                print(f"El perdedor es {perdedor}")
                print("No hay más pilas en el tablero.")
                break

            self.cambioTurno()

    def iniciar_partida(self, numeroFilas, numeroColumnas):
        self.crearTablero(numeroFilas, numeroColumnas)
        self.jugar_partida()
