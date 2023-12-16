# DATOS COMPUESTOS

# Son estructuras de datos que pueden contener múltiples valores de diferentes tipos.
# Permiten almacenar y organizar información más compleja en una sola variable.
# Los datos compuestos más comunes son las listas, tuplas, conjuntos y diccionarios.



# list[]
# Una lista es una secuencia ordenada y mutable de elementos.
# Puede contener elementos de diferentes tipos, como números, cadenas, booleanos, y otras listas.
# Las listas se definen utilizando corchetes "[]" y los elementos se separan por comas ",".
# Las listas se pueden modificar después de haberlas creado.
# Almacena datos duplicados.
# Tienen orden.
# Se accede a elementos por su índice.
lista = ["Abel Tomas", "Python", True, 1.73]
variable_lista = list[1, 2, 3, 4, 5, 6]



# tuple()
# Una tupla es una secuencia ordenada e inmutable de elementos.
# Las tuplas se definen utilizando paréntesis "()" y los elementos se separan por comas ",".
# A diferencia de las listas, no puedes modificar los elementos después de que se haya creado.
# Almacena datos duplicados.
# Tienen orden.
# Se accede a elementos por su índice.
tupla = ("Abel Tomas", "Python", True, 1.73)
variable_tupla = tuple((1, 2, 3, 4, 5, 6))



# set{}
# Un conjunto es una colección desordenada de elementos únicos.
# Se utilizan principalmente para operaciones matemáticas como uniones, intersecciones y diferencias entre conjuntos.
# Los conjuntos se definen utilizando llaves "{}" o la función "set()".
# El conjunto se modifica pero NO los elementos.
# No almacena datos duplicados.
# No se accede a los elementos por su índice.
# No tienen orden.
conjunto = {"Abel Tomas", "Python", True, 1.73}
variable_conjunto = set(("dato1", "dato2"))

# Frozenset: es un tipo de dato inmutable que representa un conjunto (set) de elementos.
# La diferencia clave entre un conjunto (set) y un "frozenset" radica en la mutabilidad
# Los conjuntos (sets) son mutables, lo que significa que se pueden modificar después de su creación.
# Los "frozensets" son inmutables, lo que significa que una vez creados, no se pueden modificar.
# Son útiles en situaciones en las que necesitas crear conjuntos de elementos que no cambiarán durante la ejecución del programa.
frozen_set = frozenset([1, 2, 3, 4, 5])

# Metiendo un conjunto dentro de otro conjunto
set1 = frozenset(["dato1", "dato2"])
set2 = {set1, "dato3"}

# Teoría de conjuntos
# Pueden haber conjuntos que son subconjuntos de otros conjuntos y otros que son un superconjunto de otro conjunto.
# Para eso ambos conjuntos deben tener los mismos valores.
conjunto1 = {1, 3, 5, 7}   # Superconjunto
conjunto2 = {1, 3, 7}      # Subconjunto



# dict{ clave-valor }
# Un diccionario es una colección de pares clave-valor, donde cada clave está asociada a un valor.
# Se definen utilizando llaves "{}" y pares "clave-valor" separados por dos puntos ":".
# Le pasamos un dato y un valor {"key" : "value"}.
# Los datos se separan con comas.
# Muestra los datos por clave asociada, NO por índice.
diccionario = {
    "nombre": "Abel Tomas",
    "curso": "Dalto",
    "esta_emocionado": True,
    "Altura": 1.73,
    "dato_duplicado": "Abel Tomas"
}



# ÍNDICE (listas, Tuplas y cadenas)
# Las listas y tuplas son secuencias ordenadas de elementos y se accede a ellos mediante índices enteros.
# Para acceder a estos datos con su índice debemos colocar el índice del dato dentro de corchetes "[]".
# El índice del iterable y de la cadena empieza desde el número cero.
# Si queremos obtener el último dato y no sabemos su índice, empezamos con "-1", con esto tomará el último dato.
# Ejemplo:
iterable = [1, 2, 3, 4, 5]
print(iterable[1])   # En este caso, el índice "1" corresponde al dato "2".
print(iterable[-1])  # En este caso, el índice "-1" corresponde al dato final, que sería "5".

# Los índices no se pueden utilizar en conjuntos y en los diccionarios, ya que estos iterables no son ordenados.



# SLICING (listas, tuplas y cadenas)
# Es la técnica de extraer una porción o subconjunto de elementos de un iterable.
# Nos permite acceder a un rango específico de elementos dentro de la secuencia, siendo muy útil para manipular datos de manera eficiente.
# Se pueden utilizar índices negativos para empezar desde el final.

# Su sintaxis es: secuencia[inicio:fin:paso]
# inicio: índice del primer elemento que deseas incluir en el slice.
# fin: índice del ultimo elemento que no deseas incluir en el slice (es decir, el slice incluirá hasta el valor anterior a ese índice).
# paso: el valor entre elementos consecutivos en el slice, es opcional y por defecto es 1.

# Ejemplo en un iterable:
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[2:5])    # Output: [2, 3, 4]
print(numeros[1::2])   # Output: [1, 3, 5, 7, 9]
print(numeros[::3])    # Output: [0, 3, 6, 9]

# Ejemplo en una cadena:
cadena = "I love Python"
print(cadena[7:9])     # Output: "Py"
print(cadena[::3])     # Output: "Io tn"

# Ejemplo de Slicing con pasos negativos:
print(numeros[::-1])   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(cadena[::-1])    # Output: "nohtyP evol I"
