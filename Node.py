class Node:
  def __init__(self,estado):
    self.child = []
    self.estado = estado

  def agregar_hijo(self, hijo):
      self.hijos.append(hijo)
    

  