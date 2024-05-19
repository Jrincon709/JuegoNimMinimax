class Tablero:
    def __init__(self) -> None:
        self.tablero = []
        self.pila = '\U0001f4e6'

    def __repr__(self) -> str:
        return f"{self.tablero}"
   

    def crearTablero(self,numeroFilas:int,numeroColumnas:list):
        for i in range(numeroFilas):
            self.tablero.append([])
            for j in range(numeroColumnas[i]):
                self.tablero[i].append(self.pila)
        return self.tablero
    
    def imprimirTablero(self):
        for fila in self.tablero:
            print(' '.join(fila))

    def eliminarPilas(self, fila: int, cantidad: int):
        
        for _ in range(cantidad):
            self.tablero[fila].pop()
        self.eliminarFilas(fila)
        
    def eliminarFilas(self,fila:int):
        if len(self.tablero[fila]==0):
            self.tablero.pop(fila)
            print(self.tablero)


tablero = Tablero()
tablero.crearTablero(3,[3,1,3])
tablero.imprimirTablero()
tablero.eliminarPilas(1,1)
tablero.imprimirTablero()
