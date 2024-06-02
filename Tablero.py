class Tablero:
    def __init__(self) -> None:
        self.tablero = []
        self.pila = '\U0001f4e6'
        self.informacion_tablero = {}

    def __repr__(self) -> str:
        return f"{self.tablero}"
   

    def crearTablero(self,numeroFilas:int,numeroColumnas:list):
        for i in range(numeroFilas):
            self.tablero.append([])
            self.informacion_tablero[i]=numeroColumnas[i]

            for j in range(numeroColumnas[i]):
                self.tablero[i].append(self.pila)
                
        return self.tablero
    
    def imprimirTablero(self):
        for indice ,fila in enumerate(self.tablero):
            print( str(indice)  +' ' + ":"+ ' '.join(fila))

    def eliminar_pilas(self, fila: int, cantidad: int):
        if fila < 0 or fila >= len(self.tablero):
            raise IndexError(f"La fila {fila}  seleccionada no existe")
        if cantidad > len(self.tablero[fila]):
            raise ValueError(f"No hay suficientes pilas en la fila {fila} para eliminar la cantidad indicada.")
        for _ in range(cantidad):
            self.tablero[fila].pop()

        if len(self.tablero[fila]) == 0:
            self.tablero.pop(fila)
        self.actualizar_info()

    def actualizar_info(self):
        self.informacion_tablero = {i: len(fila) for i, fila in enumerate(self.tablero) if len(fila) > 0}



        
    def obtener_informacion_tablero(self,tablero):
        return {i: len(fila) for i, fila in enumerate(tablero) if len(fila) > 0}
