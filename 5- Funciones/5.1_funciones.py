# --- FUNCIONES ---

# FUNCIÖN
# Es un bloque de código reutilizable que realiza una tarea específica cuando se llama.
# Permiten organizar el código en piezas más pequeñas y manejables, lo que facilita la comprensión, el mantenimiento y la reutilización del código.
# Se define con la palabra clave "def", seguida del nombre de la función y paréntesis que pueden contener los parámetros de entrada de la función.
# El bloque de código de la función se encuentra indentado debajo de la declaración de la función.
# Para llamar a la función solo pondriamos el nombre de la funcíon, con parentesis y (si es que tiene) con sus respectivos parámetros.
# Las variables que se crean dentro de una función son variables locales, solo funcionen induvidualmente dentro de la misma función y no afuera de la misma.

# PARÁMETROS
# Los parámetros son valores que se pasan a la función cuando se llama.
# Pueden ser cero o más.

# RETURN
# La instrucción "return" indica qué valor debe devolver la función cuando se la llama.
# No todas las funciones necesitan devolver un valor.
# Si no se especifica una instrucción return, la función devuelve automáticamente None.

# Ejemplo de una función de bienvenida sin parámetros:
def saludo():
    return print("¡Hola, bienvenido!")
saludo()

# Ejemplos de funciones de suma y de saludo con dos parámetros:
def suma(a,b):
    return print(a + b)

suma(2,2)
suma(3,8)
suma(2,5)

def bienvenida(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "princesa"
    elif sexo == "hombre":
        adjetivo = "titán"
    else:
        adjetivo = "amor"
    return print(f"Hola {nombre}, mi {adjetivo} ¿como andas?")

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


# "Función Recursiva"
# Una función recursiva en Python es una función que se llama a sí misma dentro de su propio cuerpo.
# Esto puede ser útil cuando se necesita resolver un problema que se puede dividir en subproblemas similares y más pequeños.
# Cada vez que la función se llama a sí misma, se trabaja con una versión reducida del problema hasta que se alcanza un caso base que no requiere más recursión.
# Ejemplo:
def factorial(n):
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

# Ten en cuenta que es importante tener un caso base en una función recursiva para evitar que se ejecute indefinidamente.
