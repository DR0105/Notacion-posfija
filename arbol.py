 class Nodo():
     def __init__(self, val, izq=None, der=None):
         self.valor = val
         self.izq = izq
         self.der = der

     def postfijo (arbol):
         if arbol != None:
             postfijo(arbol.hijoIzq())
             postfijo(arbol.hijoDer())
             print(arbol.valor)

     def hijoIzq():
         return self.izq

     def hijoDer():
         return self.der
    
