def evaluacionNotacionPosfija(expresionPosfija):
    operandos = []
    listaSimbolos = expresionPosfija.split()

    for simbolo in listaSimbolos:
        if simbolo in "0123456789":
            operandos.append(int(simbolo))
        else:
            operando2 = operandos.pop()
            operando1 = operandos.pop()
            resultado = hacerAritmetica(simbolo,operando1,operando2)
            operandos.append(resultado)
    return operandos.pop()

def hacerAritmetica(operador, operandoIzq, operandoDer):
    if operador == "*":
        return operandoIzq * operandoDer
    elif operador == "/":
        return operandoIzq / operandoDer
    elif operador == "+":
        return operandoIzq + operandoDer
    else:
        return operandoIzq - operandoDer

print(evaluacionNotacionPosfija('7 8 + 3 2 + /'))
