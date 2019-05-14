from pila import *
from arbol import *
def evaluacionNotacionPosfija(lista, pila):
    if lista!=[]
        print lista
        if lista[0]!="*" or lista[0]!="/" or lista[0]!="+" or lista[0]!="-":
            pila.apilar(Nodo(lista[0]))
            else:
                der = pila.desapilar()
                izq = pila.desapilar()
                pila.append(Nodo(lista[0],izq,der))
            return evaluacionNotacionPosfija(lista[1:], pila)
        

def hacerAritmetica(arbol):
    if arbol.valor == "*":
        return hacerAritmetica(arbol.izq) * hacerAritmetica(arbol.der)
    elif operador == "/":
        return hacerAritmetica(arbol.izq) / hacerAritmetica(arbol.der)
    elif operador == "+":
        return hacerAritmetica(arbol.izq) + hacerAritmetica(arbol.der)
    elif operador == "-":
        return hacerAritmetica(arbol.izq) - hacerAritmetica(arbol.der)
        
f= open ('operaciones.txt','r')
o=f.read()
f.close()
oper=o.splitlines()
pilaprueba = Pila()
i=0
while i<len(oper):
   print(oper[i]),
   print "= ",
   print(evaluacionNotacionPosfija(oper[i]), pilaprueba)
   i=i+1
 
