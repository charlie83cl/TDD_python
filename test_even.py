# importar el marco de prueba de Python 
import unittest

#1reverseList : escribe una función que invierta los valores 
# en la lista (sin crear una matriz temporal).
#Ejemplo: reverseList ([1,3,5]) debería devolver [5,3,1]
#Prueba de ejemplo: afirmarEqual (reverseList ([1,3,5]), [5,3,1])
#Agregue al menos otros 3 casos de prueba
def reverseList(list):
    for i in range(len(list)/2):
        list[i], list[len(list) -i -1] = list[len(list) -i -1], list[i]
    return list

#2isPalindrome : escribe una función que verifique si la palabra 
# dada es palíndrome (una palabra que se lee igual en ambos sentidos).
#Ejemplo: isPalindrome ("racecar") debería devolver True
#Prueba de ejemplo: afirmarEqual (isPalindrome ("racecar"), 
# True) o afirmarTrue (isPalindrome ("racecar"))
#Prueba de ejemplo: afirmarFalse (isPalindrome ("rabcr")).
#Agregue al menos otros 5 casos de prueba

def palindrome(string):
    string =  string.lower()
    #eliminar espacio no deseados
    auxStr = ""
    for i in range(len(string)):
        if string[i] != "":
            auxStr += string[i]
    
    for i in range(int(len(string)/2)):
        if auxStr[i] != auxStr[len(auxStr) -i -1]:
            return False
    return True

#3 monedas : escribe una función que determine cuántas monedas 
# de 25 centavos, de 10 centavos, de 5 centavos y de 1 centavo 
# le dará a un cliente para un cambio en el que minimice la cantidad de monedas que entrega.
#Ejemplo: dado 87 centavos, el resultado debe ser 3 cuartos, 1 centavo, 0 níquel y 2 centavos
#Prueba de ejemplo: afirmar Igual (moneda (87), [3,1,0,2])
#Agregue al menos otros 5 casos de prueba

def monedas(amount):
    quarter = 25
    dime = 10
    niquel = 5
    penny = 1

    cQuarter = int(amount / quarter)
    cDime = int((amount - (quarter * cQuarter)) / dime)
    cNiquel = int((amount - (quarter * cQuarter) - (dime * cDime)) / niquel)
    cPenny = int((amount - (quarter * cQuarter) - (dime * cDime) - (niquel * cNiquel)) / penny)

    return [cQuarter, "Quarters", cDime, "Dimes", cNiquel, "Niquels", cPenny, "Pennys"]

print("estas son tus monedas", monedas(4369))

#4 BONUS - factorial - Escribe una función recursiva que devuelve el factorial 
# de un número dado. Recuerde que el factorial de un número es el producto 
# de todos los números entre 1 y el número dado (por ejemplo, 4! = 4 * 3 * 2 * 1).
#Ejemplo: factorial (5) debería devolver 120.
#Agregue al menos 3 casos de prueba

def factorial(num):
    if num < 0:
        return "error, nose puede calcular el factoria de un Numero Negativo"
    elif num == 0:
        return 1
    
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
            return factorial

#4 version con factorial recursivo. que se llame asi mismo.-

def factorial(num):
    if num < 0:
        return "error, nose puede calcular el factoria de un Numero Negativo - denuevo"
    elif num == 0:
        return 1
    else:
        num = num * factorial(num-1)
    return num


#5 BONUS - fibonacci - Escribe una función recursiva que acepta un número, n, 
# y devuelve el enésimo número de Fibonacci de la secuencia. 
# Los primeros dos números de Fibonacci son 0 y 1. Cada número posterior 
# se calcula sumando los 2 números anteriores de la secuencia. 
# (es decir, 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
#Ejemplo: fibonacci (5) debería devolver 3 (el quinto número en la secuencia es 3).
#Agregue al menos 3 casos de prueba

#version no recursivo
def fibonacciNoRecursivo(n):
    if n < 2:
        return n
    else:
        fibonacci = [0,1]
        for f in range(2, n):
            fibonacci.append(fibonacci[f-1] + fibonacci[f-2])
        return fibonacci
print(fibonacciNoRecursivo(11))    

def fibonacci(n):
    if n < 2:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# nuestra "unit"
# esto es lo que estamos ejecutando nuestra prueba en 
def isEven(n):
    if n % 2 == 0:
        return True
    else:   
        return False
# nuestros "unit tests" 
# inicializado creando una clase que hereda de unittest.TestCase 
class IsEvenTests(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # otra forma de escribir arriba es 
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        # otra forma de escribir lo de arriba es
        self.assertFalse(isEven(3))
    #  cualquier tarea que desee ejecutar antes de ejecutar cualquier método anterior, colóquelas en el método setUp 
    def setUp(self):
        # agrega las tareas setUp 
        print("running setUp")
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown 
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas