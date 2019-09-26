from calc.src.Nodo import Nodo

class ArbolDeExpresiones:

    def __init__(self):
        self.raiz = None

    def constructTree(self, postfix):
        stack = []
        
        for char in postfix:
            
            if not self.isOperator(char):
                t = Nodo(char)
                stack.append(t)
            
            else:
                
                t = Nodo(char)
                t1 = stack.pop()
                t2 = stack.pop()
        
                t.right = t1
                t.left = t2
            
                stack.append(t)
        
        t = stack.pop()
        self.raiz = t
        return self.raiz

    def inorder(self, t):
        if t is not None:
            self.inorder(t.left)
            print(t.value)
            self.inorder(t.right)

    def calcular(self, nodoActual):
        resultado = 0
        if(nodoActual == None):
            return resultado
        else:
            if (nodoActual.esHoja()):
                aux = float(nodoActual.value)
                resultado = aux
            else:
                vIzq = self.calcular(nodoActual.left)
                vDer = self.calcular(nodoActual.right)
                operador = nodoActual.value

                if operador == '+':
                    resultado = vIzq + vDer

                elif operador == '-':
                    resultado = vIzq - vDer

                elif operador == '*':
                    resultado = vIzq * vDer

                elif operador == '/':
                    resultado = vIzq / vDer

        return resultado
        
    def isOperator(self, c):
        return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'








#=============================================
#MENU
#=============================================
def esNumero(char):
    return char in['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def esOperador(char):
    return char in['+', '-', '*', '/']


def esSimbolo(char):
    return char in['(', ')']


def stringToList(expresion):
    lista = []
    i = 0
    while i < len(expresion):
        char = expresion[i]
        if (esNumero(char) or esOperador(char) or esSimbolo(char)):
            if esNumero(char):
                aux = ''
                while i < len(expresion) and esNumero(expresion[i]):
                    aux = aux + expresion[i]
                    i = i+1
                lista.append(aux)
            else:
                lista.append(char)
                i = i + 1
    return lista


def infijaAPostfija(expresion):
    expresion = stringToList(expresion)
    procedencia = {}
    procedencia['*'] = 3
    procedencia['/'] = 3
    procedencia['+'] = 2
    procedencia['-'] = 2
    procedencia['('] = 1
    pila = []
    postfijo = []
    for char in expresion:
        if char == '(':
            pila.append(char)
        elif char == ')':
            tope = pila.pop()
            while tope != '(':
                postfijo.append(tope)
                tope = pila.pop()
        elif esOperador(char):  # si es un operador
            # mientras la pila no esta vacia y el operador en el tope de la pila sea mayor o igual prioridad uqe el nuevo simbolo
            while pila and procedencia[pila[len(pila)-1]] >= procedencia[char]:
                postfijo.append(pila.pop())
            pila.append(char)
        else:  # si es numero
            postfijo.append(char)
    while pila:
        postfijo.append(pila.pop())
    return postfijo




