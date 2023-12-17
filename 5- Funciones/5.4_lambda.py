# FUNCIÓN LAMBDA

# Se crean utilizando la palabra clave "lambda", seguida de una lista de parámetros separados por comas, dos puntos ":" y una expresión.
# Estas funciones son útiles cuando necesitas crear funciones simples y pequeñas en línea, sin la necesidad de darles un nombre explícito.
# Están diseñadas para ser pequeñas y no deben contener declaraciones múltiples o lógica compleja.
# Son útiles para operaciones simples y rápidas, como funciones de orden superior, filtrado y mapeo en listas.
# Para tareas más complicadas, es preferible utilizar funciones definidas con "def" para mejorar la legibilidad y mantenibilidad del código.

# Supongamos que deseas crear una función que eleve un número al cuadrado utilizando una función lambda:
cuadrado = lambda x: x ** 2
resultado = cuadrado(5)


# Aquí abajo otros ejemplos de funciones creadas con lambda:

# Verificar si un número es par:
es_par = lambda x: x % 2 == 0
r = (es_par(5))
print(r)

# Multiplicación de dos números:
multiplicacion = lambda x, y: x * y
resultado = multiplicacion(4, 6)
print(resultado)

# Obtener el último carácter de una cadena:
ultimo_caracter = lambda cadena: cadena[-1]
e = ultimo_caracter("Hola")
print(e)
