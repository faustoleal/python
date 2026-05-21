###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# # Ejemplo de una función para imprimir algo en consola
# def saludar():
#   print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#   print(f"¡Hola {nombre}!")

# saludar_a("midudev")
# saludar_a("madeval")
# saludar_a("pheralb")
# saludar_a("felixicaza")
# saludar_a("Carmen Ansio")

# # Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstring
# def restar(a, b):
#   """Resta dos números y devuelve el resultado"""
#   return a - b

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("midudev", 25, "gato")
describir_persona("hombre", "madeval", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21) 

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

# Ejercicio 1: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

print("\nEjercicio 1:")

def tabla_de_multiplicar(number:int) -> str :
  for num in range(1,11):
    print(f"{number} x {num} = {number * num}")

tabla_de_multiplicar(5)
#tabla_de_multiplicar(4)
#tabla_de_multiplicar(3)

# Ejercicio 2: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("\nEjercicio 2:")

def contar_letras_en_palabras(palabras: list[str], letra:str) -> int:
  count = 0
  for palabra in palabras:
    if palabra.lower().startswith(letra.lower()):
      count += 1
  print(count)

contar_letras_en_palabras(palabras=["pedro", "pepe", "eko", "perro"], letra="P")
#contar_letras_en_palabras(palabras=["pedro", "pepe", "eko", "serro"],letra="P")
#contar_letras_en_palabras(palabras=["pedro", "pepe", "eko", "gato"], letra="G")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

print("\nEjercicio 3:")

def factorial_de_numero(number:int) -> int:
  num = 1
  multiplicador = 1

  while num <= number:
    multiplicador *= num
    num += 1
  
  print(multiplicador)

factorial_de_numero(5)
#factorial_de_numero(8)
#factorial_de_numero(2)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

print("\nEjercicio 4:")

def validacion_de_contraseña(contraseña: str) -> str:
  while len(contraseña) < 8:
    print(f"Tu contraseña: {contraseña} no tiene el largo requerido")
    contraseña =  input("Escribe contraseña válida:")
    if len(contraseña) > 8:  
     print("Contraseña inválida")

  print(f"Contraseña: {contraseña} es válidad")

#validacion_de_contraseña("perro")
#validacion_de_contraseña("perro2000")
#validacion_de_contraseña("perro23")


#Some numbers have funny properties. For example:

#89 --> 8¹ + 9² = 89 * 1
#695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
#46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

#In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

#(a 
#p
#+b 
#p+1
# +c 
#p+2
# +d 
#p+3
#+...)=n∗k

#If it is the case we will return k, if not return -1.

def dig_pow(n,p):
    array = list(map(int, str(n)))
    
    result = 0
    
    for i,number in enumerate(array):
        #print(number ** (p + i))
        result += number ** (p + i)

    response = result // n

    if result % n == 0 :
      print(response)
    else: print(-1)

        


dig_pow(89, 1)
dig_pow(92, 1)
dig_pow(695, 2)
dig_pow(46288, 3)

#The museum of incredibly dull things
#The museum of incredibly dull things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

#However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.

#Task
#Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

#Don't change the order of the elements that are left.

#Examples
#* Input: [1,2,3,4,5], output = [2,3,4,5]
#* Input: [5,3,2,1,4], output = [5,3,2,4]
#* Input: [2,2,1,2,1], output = [2,2,2,1]

def remove_smallest(numbers):
    if not numbers: return []

    min_value = min(numbers)
    
    first_appearence = numbers.index(min_value)
    
    return [num for i, num in enumerate(numbers) if i != first_appearence ]

#There is an array with some numbers. All numbers are equal except for one. Try to find it!

#find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
#find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
#It’s guaranteed that array contains at least 3 numbers.

#The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    set_arr = set(arr)
    unique = 0
    
    for num in set_arr:
        if arr.count(num) == 1:
            unique += num
    return unique

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

#Additionally, if the number is negative, return 0.

#Note: If a number is a multiple of both 3 and 5, only count it once.

def solution(number):
    multiplos = 0
    for num in range(0, number):
        if num % 3 == 0 or num % 5 == 0:
            multiplos += num
            
    return multiplos

#Create a parser to interpret and execute the Deadfish language.

#Deadfish operates on a single value in memory, which is initially set to 0.

#It uses four single-character commands:

#i: Increment the value
#d: Decrement the value
#s: Square the value
#o: Output the value to a result array
#All other instructions are no-ops and have no effect.

#Examples
#Program "iiisdoso" should return numbers [8, 64].
#Program "iiisdosodddddiso" should return numbers [8, 64, 3600].

def parse(data):
    value = 0
    output = []

    for cmd in data:
        if cmd == "i":
            value += 1
        elif cmd == "d":
            value -= 1
        elif cmd == "s":
            value = value ** 2
        elif cmd == "o":
            output.append(value)

    return output

#A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

#For example, take 153 (3 digits), which is narcissistic:

#    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#and 1652 (4 digits), which isn't:

#   1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
#The Challenge:

#Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

#This may be True and False in your language, e.g. PHP.

#Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

def narcissistic( value ):
    array = list(map(int, str(value)))
    elevado = len(array)
    
    resultado = 0
    
    for num in array:
        resultado += num ** elevado
    
    if resultado == value: 
        return True
    else:
        return False


#Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indexes of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

#For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

#The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

def two_sum(numbers, target):
    seen = {}

    for index, value in enumerate(numbers):
        missing = target - value
        if missing in seen: return (seen[missing], index)
        seen[value] = index

    return None


#Welcome.

#In this kata you are required to, given a string, replace every letter with its position in the alphabet.

#If anything in the text isn't a letter, ignore it and don't return it.

#"a" = 1, "b" = 2, etc.

def alphabet_position(text):
    alpabhet = {chr(i +96): i for i in range(1,27)}
    
    result = []
    
    for letra in text.lower():
        if letra in alpabhet:
            result.append(str(alpabhet[letra]))
            
    return " ".join(result)

#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    array = text.split(" ")
    
    result = []
    
    for palabra in array:
        if palabra.isalpha():
            result.append(palabra[1:] + palabra[0] + "ay")
        else:
            result.append(palabra[1:] + palabra[0])
        
    return " ".join(result)

#Triple Trouble
#Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

#E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

#Note: You can expect all of the inputs to be the same length.

def triple_trouble(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))

#Create function fib that returns n'th element of Fibonacci sequence (classic programming task).

def fibonacci(n: int) -> int:
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + x
    return x


#Definition
#Jumping number is a number such that all adjacent digits in it differ by 1.

#Task
#Given a number, return "Jumping!!" if it is a jumping number, otherwise return "Not!!".

#Notes
#Number passed is always a positive integer.

#Return the result as a string.

#The difference between digit 9 and 0 is not considered as 1.

#All single digit numbers are considered jumping numbers.

def jumping_number(number):
    lista = [int(digito) for digito in str(number)]
    ultimos = lista[-2:]
    
    if len(lista) == 1:
        return "Jumping!!"
    
    for i in range(len(lista) - 1):
        if abs(lista[i] - lista[i + 1]) != 1:
            return "Not!!"
    
    return "Jumping!!"

#Write a function that, given a column title as it appears in an Excel sheet, returns its corresponding column number.

#All column titles will be uppercase.

#Examples:

def title_to_number(title):
    result = 0
    for char in title:
        value = ord(char) - ord('A') + 1
        result = result * 26 + value
    return result

 #   A number m of the form 10x + y is divisible by 7 if and only if x − 2y is divisible by 7. In other words, subtract twice the last digit from the number formed by the remaining digits. Continue to do this until a number known to be divisible by 7 is obtained; you can stop when this number has at most 2 digits because you are supposed to know if a number of at most 2 digits is divisible by 7 or not.

#The original number is divisible by 7 if and only if the last number obtained using this procedure is divisible by 7.

#Examples:
#1 - m = 371 -> 37 − (2×1) -> 37 − 2 = 35 ; thus, since 35 is divisible by 7, 371 is divisible by 7.

#The number of steps to get the result is 1.

#2 - m = 1603 -> 160 - (2 x 3) -> 154 -> 15 - 8 = 7 and 7 is divisible by 7.

#3 - m = 372 -> 37 − (2×2) -> 37 − 4 = 33 ; thus, since 33 is not divisible by 7, 372 is not divisible by 7.

#4 - m = 477557101->47755708->4775554->477547->47740->4774->469->28 and 28 is divisible by 7, so is 477557101. The number of steps is 7.

#Task:
#Your task is to return to the function seven(m) (m integer >= 0) an array (or a pair, depending on the language) of numbers, the first being the last number m with at most 2 digits obtained by your function (this last m will be divisible or not by 7), the second one being the number of steps to get the result.

#Forth Note:
#Return on the stack number-of-steps, last-number-m-with-at-most-2-digits 

#Examples:
#seven(371) should return [35, 1]
#seven(1603) should return [7, 2]
#seven(477557101) should return [28, 7]

def seven(m):
    steps = 0
    while m > 99:  # seguimos hasta que tenga como máximo 2 dígitos
        y = m % 10       # último dígito
        x = m // 10      # resto del número
        m = x - 2 * y    # regla
        steps += 1
    return (m, steps)