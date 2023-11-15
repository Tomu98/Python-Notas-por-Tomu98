# --- FUNCIÓNES BUILD IN ---

# Las funciones "built-in" (o funciones integradas) son un conjunto de funciones predefinidas que vienen incorporadas en el lenguaje.
# Están disponibles para su uso sin necesidad de importar módulos adicionales.
# Python ofrece una amplia gama de funciones "built-in" que abarcan diversas áreas.
# Estas funciones son parte fundamental del lenguaje y te permiten realizar tareas comunes de manera eficiente y sin tener que escribir el código desde cero.


# ALGUNAS FUNCIONES BUILD IN IMPORTNTES:
numeros = [2, 6, 4, 23, 5, 12, 31, 9]
mensaje_num = "24"

# Print(): Muestra el parámetro puesto en la consola.
print(numeros)


# type(): Retorna el tipo de un objeto.
tipo = type(numeros)


# str(): Convierte un objeto en una representación de cadena.
string = str(123)


# int(): Convierte una cadena en un número entero.
entero = int(mensaje_num)


# float(): Convierte una cadena en un float.
racional = float(mensaje_num)


# bool():
# Retorna True -> (!=0, True, cadena o datos no vacios)
# Retorna False -> (0, vacio, False, None)
resultado_bool_true = bool(12.23)
resultado_bool_false = bool(0)


# input(): Lee una entrada del usuario desde la consola.
input_nombre = input("Coloque su nombre aquí: ")


# list(): Convierte una secuencia en una lista.
lista = list([1, 2, 3])


# tuple(): Convierte una secuencia en una tupla.
tupla = tuple([4, 5, 6])


# set(): Crea un conjunto (set) a partir de una secuencia.
conjunto = set([7,8,9])


# dict(): Crea un diccionario a partir de pares clave-valor.
diccionario = dict(nombre="Abel", edad=24)


# len(): Obtiene la longitud de una cadena o iterable.
longitud = len(numeros)


# max(): Encuentra el valor máximo de un iterable.
numero_mas_alto = max(numeros)


# min(): Encuentra el valor mínimo de un iterable.
numero_mas_bajo = min(numeros)


# sum(): Suma todos los valores de un iterable.
# Tienen que ser solo números, sino nos devuelve excepciones.
suma_total = sum(numeros)


# abs(): Devuelve el valor absoluto de un número.
valor = -47
absoluto = abs(valor)


# round(): Redondeamos a X decimales.
# Agregamos el numero float y después de una coma ponemos la cantidad de decimales que queremos
numero = round(12.345678, 2)


# range("start","stop","step"): Genera una secuencia de números.
# El "stop" no cuenta hasta el valor dado, solo el anterior a ese.
# Puede ser utilizada en bucles for.
# Si quiero empezar a la inversa tendría que poner un número negativo.
rango = list(range(1,10,2))
rango_negativo = list(range(10, 0,-1))


# sorted(): Ordena una secuencia.
desordenada = [3, 1, 4, 5, 0, 9, 2, 8, 6, 7]
ordenada = sorted(desordenada)


# enumerate(): Itera sobre una secuencia junto con su índice.
enum = ["a", "b", "c"]
for indice, valor in enumerate(enum):
    print(f"Índice: {indice}, Valor: {valor}")


# zip(): Combina múltiples secuencias en una secuencia de tuplas.
nombres = ["Abel", "Jere", "Celeste"]
edades = [24, 21, 21]
datos = list(zip(nombres, edades))


# all(iterable): Verifica si todos los elementos en una secuencia son evaluados como "True".
# Si el iterable está vacío también devuelve True.
resultado_all_true = all([234, "true", [233.34]])
resultado_all_false = all([234, "false", []])


# any(iterable): Verifica si al menos uno de los elementos en una secuencia es evaluado como "True".
# Retorna "True" si al menos un elemento es verdadero, de lo contrario retorna "False".
any_lista = [1, "Hola", False]
print(any(any_lista))


# map(función, secuencia): Aplica una función a cada elemento de una secuencia.
# Se utiliza comúnmente en combinación con funciones lambda.
# Puede ser utilizada en una variedad de situaciones donde es necesario aplicar una operación a cada elemento de una colección de datos.
# Supongamos que tenemos una lista de números y queremos calcular el cuadrado de cada número usando la función map():
numeros_map = [1, 2, 3, 4, 5]
def cuadrado(x):
    return x ** 2
cuadrados1 = map(cuadrado, numeros_map)
print(list(cuadrados1))    # Output: [1, 4, 9, 16, 25]

# También es común usar funciones lambda con map() para hacer el código más conciso:
numeros_map2 = [1, 2, 3, 4, 5]
cuadrados2 = map(lambda x: x ** 2, numeros_map2)
print(list(cuadrados2))    # Output: [1, 4, 9, 16, 25]


# filter(función_de_filtro, secuencia): Filtra elementos de una secuencia según una función de filtro.
# toma una función de filtro y una secuencia, y devuelve un objeto que contiene solo los elementos para los cuales la función de filtro devuelve True.
# se utiliza comúnmente en combinación con funciones lambda.
# supongamos que tenemos una lista de números y queremos filtrar solo los números pares usando la función filter():
numeros_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def es_par(x):
    return x % 2 == 0
pares = filter(es_par, numeros_filter)
print(list(pares))     # Output: [2, 4, 6, 8, 10]

# También podemos usar una función lambda con filter() para hacer el código más conciso:
numeros_filter2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0, numeros_filter2)
print(list(pares))     # Output: [2, 4, 6, 8, 10]


# bin(): se utiliza para convertir un número entero en su representación binaria, que es una secuencia de dígitos "0" y "1" que representa el valor en base 2.
# El valor devuelto por bin() es una cadena de caracteres que comienza con "0b" para indicar que se trata de una representación binaria.
numero_bin = 10
binario = bin(numero_bin)
print(binario)   # Output: 0b1010


# ord(): se utiliza para obtener el valor entero (código de carácter) de un carácter en función de su representación Unicode.
# Toma un carácter como argumento y devuelve su valor numérico correspondiente según la tabla Unicode.
# Cada carácter en Unicode tiene un valor numérico único asociado, lo que permite a ord() convertir un carácter en su representación numérica.
# Es importante mencionar que "ord()" funciona tanto para caracteres en inglés como para caracteres en otros idiomas y símbolos Unicode.
# Es una función útil cuando necesitas trabajar con códigos de caracteres o realizar operaciones de manipulación de cadenas basadas en sus valores numéricos.
charOrd = "A"
valorOrd = ord(charOrd)
print(valorOrd)   # Output: 65


# eval(): se utiliza para evaluar expresiones o evaluaciones de cadenas como código Python.
# Toma una cadena como argumento y la interpreta como una expresión Python, ejecutándola y devolviendo el resultado.
# Es importante tener en cuenta que "eval()" puede ser poderoso, pero también peligroso si se utiliza de manera incorrecta.
#  Puede ejecutar cualquier código Python contenido en la cadena, por lo que debes ser extremadamente cauteloso al usarlo, especialmente si la cadena se genera a partir de fuentes no confiables, ya que podría permitir la ejecución de código malicioso.
