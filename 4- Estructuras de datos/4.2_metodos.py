# --- METODOS ---

# Es una función que está asociada a un objeto específico y que puede ser llamada para realizar operaciones o manipulaciones en ese objeto.
# Permiten interactuar con los datos de manera conveniente y coherente.
# Su sintxis es: "dato.metodo()"
# Hay diferentes tipos de métodos tanto para cadenas como para iterables.


# Métodos de cadena.
# Son especialmente útiles para manipular y trabajar con texto.
# Puedes combinarlos y usarlos de diversas formas para manipular y transformar cadenas según tus necesidades.
# Las cadenas en Python son inmutables, lo que significa que no se pueden cambiar directamente después de haber sido creadas.
# Por lo tanto, algunos métodos devuelven una nueva cadena que refleja los cambios que se realizaron.
cadena1 = "Hola, esto es una cadena"
cadena2 = "1234543210"
cadena3 = "abcdefghijklmnopqrstuvwxyz"

# len(cadena): FUNCIÓN que cuenta la longitud de la cadena.
cantidad = len(cadena1)
# .upper(): Devuelve una copia de la cadena en mayúsculas.
upper = cadena1.upper()
# .lower(): Devuelve una copia de la cadena en minúsculas.
lower = cadena1.lower()
# .capitalize(): Devuelve una copia de la cadena con la primera letra en mayúscula y el resto en minúsculas.
capitalize = cadena1.capitalize()
# .title(): Devuelve una copia de la cadena con cada palabra inicial en mayúscula.
title = cadena1.title()
# .strip(): Devuelve una copia de la cadena sin espacios en blanco al principio y al final.
strip = cadena1.strip()
# .lstrip(): Devuelve una copia de la cadena sin espacios en blanco al principio.
lstrip = cadena1.lstrip()
# .rstrip(): Devuelve una copia de la cadena sin espacios en blanco al final.
rstrip = cadena1.rstrip()
# .replace(antiguo, nuevo): Devuelve una copia de la cadena con todas las ocurrencias de "antiguo" reemplazadas por "nuevo".
replace = cadena1.replace("Hola", "Buenas")
# .split(separador): Divide la cadena en una lista de subcadenas utilizando el "separador" como criterio.
split = cadena1.split(" ")
# .join(iterable): Une los elementos de un iterable (como una lista) en una cadena, utilizando la cadena como separador.
iterable = ["1", "2", "3", "4"]
join = "-".join(iterable)
# .startswith(subcadena): Verifica si la cadena comienza con la "subcadena" dada y devuelve un valor booleano.
# Se admiten parámetros opcionales para especificar un rango de índices.
startswith = cadena1.startswith("H")
# .endswith(subcadena): Verifica si la cadena termina con la "subcadena" dada y devuelve un valor booleano.
# Se admiten parámetros opcionales para especificar un rango de índices.
endswith = cadena1.endswith("no")
# .find(subcadena): Devuelve el índice de la primera aparición de la "subcadena" en la cadena, o -1 si no se encuentra.
find = cadena2.find("8")
# .index(subcadena): Similar a find(), pero lanza una excepción si la subcadena no se encuentra.
index = cadena2.index("2")
# .count(subcadena): Cuenta cuántas veces aparece la "subcadena" en la cadena.
count = cadena1.count("e")
# .isalnum(): Verifica si todos los caracteres en la cadena son alfanuméricos.
isalnum = cadena2.isalnum()
# .isnumeric(): verifica si todos los caracteres son numéricos, incluyendo caracteres que representan números en diferentes sistemas.
isnumeric = cadena2.isnumeric()
# .isalpha(): Verifica si todos los caracteres en la cadena son letras (NO SIGNOS NI ESPACIOS).
isalpha = cadena3.isalpha()
# .isdigit(): Verifica si todos los caracteres en la cadena son dígitos numéricos (NO SIGNOS NI ESPACIOS).
isdigit = cadena2.isdigit()
# .isspace(): Verifica si la cadena contiene solo espacios en blanco.
isspace = cadena1.isspace()
# .islower(): Verifica si todos los caracteres en la cadena están en minúsculas.
islower = cadena3.islower()
# .isupper(): Verifica si todos los caracteres en la cadena están en mayúsculas.
isupper = cadena1.isupper()

# rjust(), zfill(), ljust()


# Métodos de Listas.
lista = ["Abel", "Tomas", 24, "Curso", "Python"]

# .append(elemento): Agrega un elemento al final de la lista.
lista.append("Inglés")
# .extend(iterable): Agrega los elementos de un iterable al final de la lista.
lista.extend([True, 2023])
# .insert(posición, elemento): Inserta un elemento en una posición específica.
lista.insert(2, "Estudiar")
# .remove(elemento): Elimina la primera aparición del elemento en la lista.
lista.remove(24)
# .pop(posición): Elimina y devuelve un elemento en una posición dada, o el último si no se especifica.
# Para eliminar el ultimo elemento de una lista es colocando -1 u otro número negativo.
lista.pop(0)
lista.pop(-1)
# .count(elemento): Cuenta cuántas veces aparece el elemento en la lista.
count = cadena1.count("o")
# .sort(iterable): Ordena un iterable de forma ascendente a descendente.
# Solo ordena los numeros y los "true-false", no los textos. Primero ordena los "false", luego los "true" y luego los numeros.
lista_sort = list([2, 54, False, 23, 1, 5, 8, True, 43, 7])
lista_sort.sort()
# Parametro "reverse=true": si agregamos al sort este parametro invierte los elementos de la lista.
lista_sort.sort(reverse=True)
# .reverse(iterable): Invierte los elementos de una lista.
lista.reverse()
# .index(elemento): Verifica si un elemento (completo) se encuentra en la lista.
lista_index = list(["Tomate", "Lechuga", "Carne", "Huevo", "Cebolla"])
elemento_encontrado = lista_index.index("Lechuga")
# .clear(iterable): Elimina todos los elementos de una lista.
lista.clear()



# Métodos de Tuplas:
# Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
# Por lo tanto, no tienen muchos métodos.
tupla = ("Abel", "Tomas", "24", "24", "Escorpio")

# Algunos de los métodos comunes son:
# count(elemento): Cuenta cuántas veces aparece el elemento en la tupla.
cont = tupla.count("24")
# index(elemento): Verifica si un elemento (completo) se encuentra en la tupla.
ind = tupla.index("Escorpio")



# Métodos de Conjuntos (Sets)
conjunto1 = {"Gordo", "Misi", "Tao"}
conjunto2 = {"Blanquito", "Grisesito"}
setnum1 = {1,2,5,6,9,0}
setnum2 = {1,3,6,9}

# Algunos de estos métodos pueden aceptar conjuntos u otros iterables como argumentos.
# .add(elemento): Agrega un elemento al conjunto.
conjunto2.add("Tao")
# .remove(elemento): Elimina un elemento del conjunto. Lanza un error si el elemento no está presente.
conjunto2.remove("Tao")
# .discard(elemento): Elimina un elemento del conjunto si está presente, sin lanzar error.
conjunto2.discard("Tao")
# .pop(): Elimina y devuelve un elemento arbitrario del conjunto.
conjunto2.pop()
# .union(iterable): Devuelve un nuevo conjunto que contiene todos los elementos de este conjunto y del iterable proporcionado.
union = conjunto1.union(conjunto2)
# .intersection(iterable): Devuelve un nuevo conjunto que contiene los elementos que están presentes en ambos conjuntos.
intersection = setnum1.intersection(setnum2)
# .difference(iterable): Devuelve un nuevo conjunto con los elementos presentes en este conjunto pero no en el iterable.
difference = setnum1.difference(setnum2)
# .symmetric_difference(iterable): Devuelve un nuevo conjunto con los elementos que están en un conjunto o en el otro, pero no en ambos.
symmetric_difference = setnum1.symmetric_difference(setnum2)
# .issubset(iterable): Verifica si el conjunto es un subconjunto del iterable dado, paara eso el subconjunto tiene que tener unicamente valores del superconjunto.
issubset = setnum2.issubset(setnum1)
# .issuperset(iterable): Verifica si el conjunto es un superconjunto del iterable dado, para eso el superconjunto tiene que tener todos los valores del subconjunto.
issuperset = setnum1.issuperset(setnum2)
# .isdisjoint(iterable): Verifica si dos conjuntos no tienen elementos en común.
# si los conjuntos no comparten ningún elemento, el método devuelve True; de lo contrario, devuelve False.
isdisjoint = setnum1.isdisjoint(setnum2)
# .clear(): Elimina todos los elementos del conjunto.
# clear = conjunto1.clear()



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
# .keys(): Devuelve una vista de las claves en el diccionario.
keys = diccionario1.keys()
# .values(): Devuelve una vista de los valores en el diccionario.
values = diccionario1.values()
# .items(): Devuelve una vista de pares clave-valor en el diccionario.
items = diccionario1.items()
# .get("clave", "valor predeterminado"): Devuelve el valor asociado con la clave dada. Si la clave no está presente, devuelve un valor predeterminado opcional.
# este es especialmente útil para manejar casos donde no estás seguro si una clave existe en el diccionario
# y no quieres que el programa genere una excepción si no lo hace.
get1 = diccionario1.get("nombre")
get_none = diccionario1.get("nivel")
get_valor_puesto = diccionario1.get("nivel", "NO ENCONTRADO")
# .pop("clave", "valor predeterminado"): Elimina y devuelve el valor asociado con la clave. Si la clave no está presente, devuelve un valor predeterminado opcional.
pop_dic = diccionario1.pop("nombre")
# .update(iterable|diccionario): Actualiza el diccionario con los pares clave-valor del iterable o diccionario proporcionado.
diccionario1.update(diccionario2)
# .copy(): Devuelve una copia superficial del diccionario.
copy = diccionario1.copy()
# .clear(): Elimina todos los elementos del diccionario.
# clear_dic = diccionario1.clear()
