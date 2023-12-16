# MÉTODOS

# Es una función que está asociada a un objeto específico y que puede ser llamada para realizar operaciones o manipulaciones en ese objeto.
# Permiten interactuar con los datos de manera conveniente y coherente.
# Su sintaxis es: "dato.método()"
# Hay diferentes tipos de métodos tanto para cadenas como para iterables.



# Métodos de cadena.
# Son útiles para manipular y trabajar con cadenas de texto.
# Puedes combinarlos y usarlos de diversas formas para manipular y transformar cadenas según tus necesidades.
# Las cadenas en Python son inmutables, lo que significa que no se pueden cambiar directamente después de haber sido creadas.
# Por lo tanto, algunos métodos devuelven una nueva cadena que refleja los cambios que se realizaron.
cadena1 = "Hola, esto es una cadena"
cadena2 = "1234543210"
cadena3 = "abcdefghijklmnopqrstuvwxyz"

# len(cadena)
cantidad = len(cadena1)  # FUNCIÓN que cuenta la longitud de la cadena.

# .upper()
upper = cadena1.upper()  # devuelve una copia de la cadena en mayúsculas.

# .lower()
lower = cadena1.lower()  # devuelve una copia de la cadena en minúsculas.

# .capitalize()
capitalize = cadena1.capitalize()  # devuelve una copia de la cadena con la primera letra en mayúscula y el resto en minúsculas.

# .title()
title = cadena1.title()  # devuelve una copia de la cadena con cada palabra inicial en mayúscula.

# .strip()
strip = cadena1.strip()  # devuelve una copia de la cadena sin espacios en blanco al principio y al final.

# .lstrip()
lstrip = cadena1.lstrip()  # devuelve una copia de la cadena sin espacios en blanco al principio.

# .rstrip()
rstrip = cadena1.rstrip()  # devuelve una copia de la cadena sin espacios en blanco al final.

# .replace(antiguo, nuevo)
replace = cadena1.replace("Hola", "Buenas")  # devuelve una copia de la cadena con todas las ocurrencias de "antiguo" reemplazadas por "nuevo".

# .split(separador)
split = cadena1.split(" ")  # divide la cadena en una lista de subcadenas utilizando el "separador" como criterio.

# .join(iterable)
iterable = ["1", "2", "3", "4"]
join = "-".join(iterable)  # une los elementos de un iterable (como una lista) en una cadena, utilizando la cadena como separador.

# .startswith(subcadena)
# verifica si la cadena comienza con la "subcadena" dada y devuelve un valor booleano.
# se admiten parámetros opcionales para especificar un rango de índices.
startswith = cadena1.startswith("H")

# .endswith(subcadena)
# verifica si la cadena termina con la "subcadena" dada y devuelve un valor booleano.
# se admiten parámetros opcionales para especificar un rango de índices.
endswith = cadena1.endswith("no")

# .find(subcadena)
find = cadena2.find("8")  # devuelve el índice de la primera aparición de la "subcadena" en la cadena, o -1 si no se encuentra.

# .index(subcadena)
index = cadena2.index("2")  # similar a find(), pero lanza una excepción si la subcadena no se encuentra.

# .count(subcadena)
count = cadena1.count("e")  # cuenta cuántas veces aparece la "subcadena" en la cadena.

# .isalnum()
isalnum = cadena2.isalnum()  # verifica si todos los caracteres en la cadena son alfanuméricos.

# .isnumeric()
isnumeric = cadena2.isnumeric()  # verifica si todos los caracteres son numéricos, incluyendo caracteres que representan números en diferentes sistemas.

# .isalpha()
isalpha = cadena3.isalpha()  # verifica si todos los caracteres en la cadena son letras (NI SIGNOS NI ESPACIOS).

# .isdigit()
isdigit = cadena2.isdigit()  # verifica si todos los caracteres en la cadena son dígitos numéricos (NI SIGNOS NI ESPACIOS).

# .isspace()
isspace = cadena1.isspace()  # verifica si la cadena contiene solo espacios en blanco.

# .islower()
islower = cadena3.islower()  # verifica si todos los caracteres en la cadena están en minúsculas.

# .isupper()
isupper = cadena1.isupper()  # verifica si todos los caracteres en la cadena están en mayúsculas.



# Métodos de Listas.
# Útiles para manipular y trabajar con listas.
lista = ["Abel", "Tomas", 24, "Curso", "Python"]

# .append(elemento)
lista.append("Inglés")  # agrega un elemento al final de la lista.

# .extend(iterable)
lista.extend([True, 2023])  # agrega los elementos de un iterable al final de la lista.

# .insert(posición, elemento)
lista.insert(2, "Estudiar")  # inserta un elemento en una posición específica.

# .remove(elemento)
lista.remove(24)  #  elimina la primera aparición del elemento en la lista.

# .pop(posición)
# elimina y devuelve un elemento en una posición dada, o el último si no se especifica.
# para eliminar el último elemento de una lista es colocando -1 u otro número negativo.
lista.pop(0)
lista.pop(-1)

# .count(elemento)
count = cadena1.count("o")  # cuenta cuántas veces aparece el elemento en la lista.

# .sort(iterable)
# ordena un iterable de forma ascendente a descendente.
# solo ordena los números y los "true-false", no los textos.
# primero ordena los "false", luego los "true" y luego los números.
lista_sort = list([2, 54, False, 23, 1, 5, 8, True, 43, 7])
lista_sort.sort()
# Parametro "reverse=true"
lista_sort.sort(reverse=True)  # si agregamos al sort este parámetro invierte los elementos de la lista.

# .reverse(iterable)
lista.reverse()  # invierte los elementos de una lista.

# .index(elemento)
# verifica si un elemento (completo) se encuentra en la lista.
lista_index = list(["Tomate", "Lechuga", "Carne", "Huevo", "Cebolla"])
elemento_encontrado = lista_index.index("Lechuga")

# .clear(iterable)
lista.clear()  # elimina todos los elementos de una lista.



# Métodos de Tuplas.
# Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
# Por lo tanto, no tienen muchos métodos.
tupla = ("Abel", "Tomas", "24", "24", "Escorpio")

# count(elemento)
cont = tupla.count("24")  # cuenta cuántas veces aparece el elemento en la tupla.

# index(elemento)
ind = tupla.index("Escorpio")  # verifica si un elemento (completo) se encuentra en la tupla.



# Métodos de Conjuntos (Sets)
# Algunos de estos métodos pueden aceptar conjuntos u otros iterables como argumentos.
conjunto1 = {"Gordo", "Misi", "Tao"}
conjunto2 = {"Blanquito", "Grisesito"}
setnum1 = {1,2,5,6,9,0}
setnum2 = {1,3,6,9}

# .add(elemento)
conjunto2.add("Tao")  # agrega un elemento al conjunto.

# .remove(elemento)
conjunto2.remove("Tao")  # elimina un elemento del conjunto. Lanza un error si el elemento no está presente.

# .discard(elemento)
conjunto2.discard("Tao")  # elimina un elemento del conjunto si está presente, sin lanzar error.

# .pop()
conjunto2.pop()  # elimina y devuelve un elemento arbitrario del conjunto.

# .union(iterable)
union = conjunto1.union(conjunto2)  # devuelve un nuevo conjunto que contiene todos los elementos de este conjunto y del iterable proporcionado.

# .intersection(iterable)
intersection = setnum1.intersection(setnum2)  # devuelve un nuevo conjunto que contiene los elementos que están presentes en ambos conjuntos.

# .difference(iterable)
difference = setnum1.difference(setnum2)  # devuelve un nuevo conjunto con los elementos presentes en este conjunto pero no en el iterable.

# .symmetric_difference(iterable)
symmetric_difference = setnum1.symmetric_difference(setnum2)  # devuelve un nuevo conjunto con los elementos que están en un conjunto o en el otro, pero no en ambos.

# .issubset(iterable)
issubset = setnum2.issubset(setnum1)  # verifica si el conjunto es un subconjunto del iterable dado, para eso el subconjunto tiene que tener únicamente valores del superconjunto.

# .issuperset(iterable)
issuperset = setnum1.issuperset(setnum2)  # verifica si el conjunto es un superconjunto del iterable dado, para eso el superconjunto tiene que tener todos los valores del subconjunto.

# .isdisjoint(iterable)
# verifica si dos conjuntos no tienen elementos en común.
# si los conjuntos no comparten ningún elemento, el método devuelve True; de lo contrario, devuelve False.
isdisjoint = setnum1.isdisjoint(setnum2)

# .clear()
# clear = conjunto1.clear()  # elimina todos los elementos del conjunto.



# Métodos de Diccionarios
diccionario1 = {
    "nombre":"Abel",
    "apellido":"Romero",
    "edad":24,
    "curso":"Python"
}
diccionario2 = {
    "nivel":"Principiante",
    "país":"Argentina"
}

# .keys()
keys = diccionario1.keys()  # devuelve una vista de las claves en el diccionario.

# .values()
values = diccionario1.values()  # devuelve una vista de los valores en el diccionario.

# .items()
items = diccionario1.items()  # devuelve una vista de pares clave-valor en el diccionario.

# .get("clave", "valor predeterminado")
# devuelve el valor asociado con la clave dada. Si la clave no está presente, devuelve un valor predeterminado opcional.
# es útil para manejar casos donde no estás seguro si una clave existe en el diccionario y no quieres que el programa genere una excepción si no lo hace.
get1 = diccionario1.get("nombre")
get_none = diccionario1.get("nivel")
get_valor_puesto = diccionario1.get("nivel", "NO ENCONTRADO")

# .pop("clave", "valor predeterminado")
pop_dic = diccionario1.pop("nombre")  # elimina y devuelve el valor asociado con la clave. Si la clave no está presente, devuelve un valor predeterminado opcional.

# .update(iterable|diccionario)
diccionario1.update(diccionario2)  # actualiza el diccionario con los pares clave-valor del iterable o diccionario proporcionado.

# .copy()
copy = diccionario1.copy()  # devuelve una copia superficial del diccionario.

# .clear()
# clear_dic = diccionario1.clear()  # elimina todos los elementos del diccionario.
