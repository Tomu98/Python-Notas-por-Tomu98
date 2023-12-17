# FUNCIONES

# Una función en programación es un bloque de código reutilizable que realiza una tarea específica cuando se llama.
# Permiten organizar el código en piezas más pequeñas y manejables, facilitando la comprensión, el mantenimiento y la reutilización del código.


# def
# Se utiliza para definir la función, seguida de su nombre y paréntesis, donde puede contener los parámetros de entrada de la función.
# El bloque de código de la función se encuentra indentado debajo de la declaración "def".
# Para llamar a la función solo pondríamos el nombre de la función, con paréntesis y (si es que tiene) con sus respectivos parámetros.
# Las variables que se crean dentro de una función son variables locales, solo funcionen individualmente dentro de la misma función y no afuera de la misma.

# ( parámetros )
# Los parámetros son valores que se pasan a la función cuando se llama.
# Pueden ser cero o más.
# Se colocan dentro de los paréntesis de la función.

# return
# La instrucción "return" indica qué valor debe devolver la función cuando se la llama.
# No todas las funciones necesitan devolver un valor.
# Si no se especifica una instrucción return, la función devuelve automáticamente None.

# Ejemplo de sintaxis de una función:
def saludo():
    """Función de saludo"""
    return print("¡Hola, bienvenido!")
saludo()

# Ejemplos de funciones de suma y de saludo con dos parámetros:
def suma(a,b):
    """Función que suma dos argumentos"""
    return print(a + b)

suma(2,2)
suma(3,8)
suma(2,5)

def bienvenida(nombre, sexo):
    """Función de bienvenida"""
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "princesa"
    elif sexo == "hombre":
        adjetivo = "titán"
    else:
        adjetivo = "amor"
    return print(f"Hola {nombre}, mi {adjetivo} ¿cómo andas?")

bienvenida("Rubio", "hOmBre")
bienvenida("Pecas", "mUjer")
bienvenida("X", "No lo sé")



# VARIABLE GLOBAL
# "global" se utiliza para indicar que una variable que se está utilizando dentro de una función es una variable global.
# Cualquier cambio que hagas en ella afectará a la variable global fuera de la función.
# Ejemplo:
contador = 0    # Variable global

def incrementar_contador():
    pass
    # global contador   # Con "global" utilizamos la variable global dentro de la función
    # contador += n


# Función Recursiva
# Es una función que se llama a sí misma dentro de su propio código.
# Es útil cuando se necesita resolver un problema que se puede dividir en subproblemas similares y más pequeños.
# Cada vez que la función se llama a sí misma, se trabaja con una versión reducida del problema hasta que se alcanza un caso base que no requiere más recursión.
# Ejemplo:
def factorial(n):
    """Función de ejemplo de recursividad"""
    # Caso base: si "n" es igual a 0, el factorial es 1.
    if n == 0:
        return 1
    # Caso recursivo: llama a la función factorial con n-1 y multiplica por n.
    return n * factorial(n - 1)

resultado = factorial(6)
print(f"El factorial es: {resultado}")

# En este ejemplo, hemos creado una función llamada "factorial" que calcula el factorial de un número "n".
# El caso base es cuando "n" es igual a 0, en cuyo caso el factorial es 1.
# En el caso recursivo, llamamos a la función "factorial" con "n - 1" y multiplicamos el resultado por "n".
# Esto significa que la función se llamará a sí misma con valores más pequeños de "n" hasta que alcance el caso base.
# Luego, se multiplicarán los valores de "n" a través de las llamadas recursivas para calcular el factorial.
# Es importante tener un caso base en una función recursiva para evitar que se ejecute indefinidamente.
