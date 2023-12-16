# VARIABLES

# Una variable es un espacio donde almacenamos datos, cada variable contiene un dato específico.
# Las variables pueden tener un dato simple (variable) o un dato compuesto (iterable).
# Sintaxis:
nombre = "Dato"   # Definiendo una variable.



# CONVENCIONES
# Hay diferentes tipos de convenciones para nombrar variables, funciones y constantes, algunas de estas son:
nombre_variable = "Snake Case"   # variable con "snake_case" (recomendado en Python).
nombreVariable = "Camel Case"   # variable con "camelCase" (recomendado en JavaScript).
NombreVariable = "Pascal Case"   # variable con "Pascal Case" (clases, funciones, constantes)



# CONSTANTES
# Son valores que no cambian en la ejecución del programa y se utilizan para representar datos fijos o valores inmutables.
# Se usa nombres en mayúsculas para indicar que una variable es una constante y su valor no debería cambiar.
# Ejemplos:
PI = 3.14159
GRAVEDAD = 9.8
DIAS_EN_LA_SEMANA = 7



# DESENPAQUETADO
# Es la capacidad de tomar los datos de un iterable y asignarles variables individuales.
# Puede mejorar la legibilidad del código y simplificar la asignación de valores en una sola operación.
# Se realiza utilizando la sintaxis de asignación múltiple, se proporcionan las variables y luego el iterable.

# Desempaquetado:
datos_en_lista = ["Abel", "Romero", 24]
nombre, apellido, edad = datos_en_lista
print(apellido)   # Romero

# Desempaquetado de una lista:
lista = [1, 2, 3]
a, b, c = lista
print(b)   # 2

# Desempaquetado de una tupla:
tupla = ("manzana", "banana", "cereza")
fruta1, fruta2, fruta3 = tupla
print(fruta3)  # cereza

# Desempaquetado con valores restantes:
# Si queremos solo desempaquetar por ejemplo dos datos en dos variables y el resto aparte, utilizamos "*".
numeros = [10, 20, 30, 40, 50]
primero, segundo, *restantes = numeros
print(segundo)      # 20
print(restantes)    # [30, 40, 50]

# Desempaquetado de un diccionario (las claves se desempaquetan):
datos = {"nombre": "Abel", "edad": 24, "ciudad": "Metán"}
nombre1, edad1, ciudad = datos.values()
print(edad)



# VARIABLES LOCALES Y GLOBALES
# Hay diferentes tipos de variables, están las locales y las globales.

# - Variables Locales:
# Son aquellas que se definen dentro de una función y solo son accesibles dentro de esa función.
# Significa que no puedes usarlas fuera de la función en la que se crearon.
# - Variables Globales:
# Son aquellas que se definen fuera de cualquier función o bloque de código.
# Son accesibles desde cualquier parte del programa, incluidas las funciones.

# Ejemplo:
variable_global = "¡Hola, soy una variable global!"    # Variable global

def variable():
    variable_local = "¡Hola, soy una variable local!"  # Variable local.
    print(variable_local)
variable()

# La variable local solo es accesible dentro de la función "variable()", intentar acceder a ella fuera de la función resultaría en un error.
# Mientras que la global se la puede llamar dentro de la función con la palabra clave "global" (Explicado mejor en "Funciones").
