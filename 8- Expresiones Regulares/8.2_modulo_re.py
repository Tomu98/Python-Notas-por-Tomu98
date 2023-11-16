# --- MÓDULO RE ---

import re

# El módulo "re" en Python es una biblioteca estándar que proporciona soporte para expresiones regulares.
# El nombre "re" es una abreviatura de "regular expressions" (expresiones regulares en inglés), y este módulo permite trabajar con patrones de búsqueda y manipulación de texto utilizando expresiones regulares.

# El módulo "re" utiliza la sintaxis estándar de expresiones regulares.
# Además de estas funciones básicas, también puedes acceder a propiedades y métodos en objetos de coincidencia para obtener información detallada sobre las coincidencias encontradas.

texto = "Hola, mi número de teléfono es 123-456-7890."
patron = r'\d{3}-\d{3}-\d{4}'  # Patrón para buscar números de teléfono

# Buscar una coincidencia en el texto
coincidencia = re.search(patron, texto) # Función utilizada para el patron



# Contiene varias funciones y clases que facilitan la manipulación de cadenas de texto con expresiones regulares.

# "re.search"(patrón, cadena):
# Se utiliza para buscar un patrón especificado dentro de una cadena de texto y devuelve un objeto de coincidencia ("MatchObject") si encuentra una coincidencia.
# Si no se encuentra ninguna coincidencia, devuelve "None".
# - "patrón": Una expresión regular que defines como un patrón de búsqueda.
# - "cadena": La cadena de texto en la que deseas buscar el patrón.
# Supongamos que tienes la siguiente cadena de texto y deseas buscar la palabra "Python" en ella:

textoSearch = "Python es un lenguaje de programación poderoso y versátil."
patronSearch = r"Python"

coincidencia = re.search(patronSearch, textoSearch)

if coincidencia:
    print(f"Se encontró una coincidencia 'Search': {coincidencia.group()}")
else:
    print("No se encontró ninguna coincidencia 'Search'.")



# "re.findall"(patrón, cadena):
# Esta función busca todas las coincidencias del patrón en la cadena y devuelve una lista de todas las coincidencias encontradas.
# Devuelve una lista vacía si no se encuentra ninguna coincidencia en la cadena.
# Supongamos que tienes una cadena de texto con múltiples direcciones de correo electrónico y deseas encontrar todas estas direcciones en la cadena:

textoFindall = "Mis correos son abel@email.com, jere@domain.com y celeste@example.net"
patronFindall = r'\S+@\S+'  # \S coincide con caracteres no espacios en blanco

coincidencias = re.findall(patronFindall, textoFindall)

for correo in coincidencias:
    print(f"Correo encontrado con 'findall': {correo}")

# En este ejemplo, utilizamos "re.findall()" con el patrón "r'\S+@\S+'" para buscar todas las direcciones de correo electrónico en la cadena "texto".
# Este patrón busca cadenas que contengan un "@" entre caracteres que no sean espacios en blanco.
# El resultado es una lista de todas las direcciones de correo electrónico encontradas en el texto.



# "re.match"(patrón, cadena)
# Se utiliza para buscar un patrón especificado al principio de una cadena de texto y devuelve un objeto de coincidencia ("MatchObject") si encuentra una coincidencia en la posición inicial.
# Si no encuentra ninguna coincidencia al principio de la cadena, devuelve "None".
# Supongamos que tienes una cadena de texto y deseas verificar si comienza con la palabra "Hola":

textoMatch = "Hola, ¿cómo estás?"
patronMatch = r"Hola"

coincidencia = re.match(patronMatch, textoMatch)

if coincidencia:
    print(f"Se encontró una coincidencia 'Match': {coincidencia.group()}")
else:
    print("No se encontró ninguna coincidencia 'Match'.")



# "re.finditer"(patrón, cadena):
# Similar a "re.findall()", pero devuelve un iterador que proporciona objetos de coincidencia en lugar de una lista.
# Se utiliza para buscar todas las ocurrencias de un patrón especificado dentro de una cadena de texto y devuelve un iterador que proporciona objetos de coincidencia ("MatchObject") para cada coincidencia encontrada.
# Es útil cuando necesitas encontrar y procesar todas las coincidencias de un patrón en una cadena.
# Cada objeto de coincidencia proporcionado por el iterador contiene información sobre la posición y el contenido de la coincidencia, lo que te permite realizar tareas específicas en cada coincidencia encontrada.
# Supongamos que tienes una cadena de texto con múltiples números de teléfono y deseas encontrar y procesar todas las ocurrencias de números de teléfono en la cadena:

textoFinditer = "Mis números de teléfono son 123-456-7890 y 987-654-3210."
patronFinditer = r'\d{3}-\d{3}-\d{4}'  # Patrón para números de teléfono

coincidencias = re.finditer(patronFinditer, textoFinditer)

for coincidencia in coincidencias:
    numero_telefono = coincidencia.group()
    print(f"Número de teléfono encontrado con 'finditer': {numero_telefono}")



# "re.sub"(patrón, reemplazo, cadena):
# Esta función busca todas las coincidencias del patrón en la cadena y las reemplaza con el texto o cadena especificado en "reemplazo".
# - "reemplazo": La cadena o texto con la que deseas reemplazar todas las coincidencias encontradas.
# Devuelve una nueva cadena con las sustituciones realizadas.
# Supongamos que tienes una cadena de texto y deseas reemplazar todas las vocales con la letra "X":

textoSub = "Hola, ¿cómo estás?"
patronSub = r'[aeiouAEIOU]'  # Patrón para vocales

texto_reemplazo = "X"

nuevo_texto = re.sub(patronSub, texto_reemplazo, textoSub)

print(f"nuevo texto remplzdo con 'sub': {nuevo_texto}")

# La función # buscará todas las vocales en la cadena y las reemplazará por "X".



# patron_compilado = "re.compile"(patrón):
# Se utiliza para compilar una expresión regular en un objeto de patrón de búsqueda.
# Este objeto de patrón puede ser reutilizado varias veces para realizar búsquedas o búsquedas y reemplazos en cadenas de texto.
# Compilar la expresión regular una vez y reutilizarla puede mejorar el rendimiento cuando se necesita realizar la misma operación de búsqueda o reemplazo en múltiples cadenas.

# Supongamos que deseas buscar números de teléfono en varias cadenas de texto diferentes utilizando el mismo patrón.
# Puedes compilar el patrón una vez y luego reutilizarlo en cada cadena de texto:

patronCompile = r'\d{3}-\d{3}-\d{4}'
patron_compilado = re.compile(patronCompile)

texto1 = "Mi número de teléfono es 123-456-7890."
texto2 = "Llámame al 987-654-3210 si tienes preguntas."

coincidencias1 = patron_compilado.findall(texto1)
coincidencias2 = patron_compilado.findall(texto2)

print(f"Coincidencias en texto1 con 'compile': {coincidencias1}")
print(f"Coincidencias en texto2 con 'compile': {coincidencias2}")

# En este ejemplo, primero definimos el patrón "r'\d{3}-\d{3}-\d{4}'" para buscar números de teléfono en el formato "###-###-####".
# Luego, utilizamos "re.compile()" para compilar el patrón en un objeto de patrón llamado "patron_compilado".
# Después, aplicamos el objeto de patrón compilado a dos cadenas de texto diferentes ("texto1" y "texto2") utilizando "patron_compilado.findall()".
# Esto nos permite buscar números de teléfono en ambas cadenas utilizando el mismo patrón compilado.




# Pametro "flags"

# Se utiliza para proporcionar modificadores que afectan el comportamiento de la búsqueda o coincidencia de patrones en una cadena de texto.
# Los modificadores (flags) se pasan como argumento a las funciones del módulo "re" y permiten ajustar la forma en que se realiza la búsqueda.

# Algunos de los modificadores comunes que puedes utilizar como argumento en el parámetro "flags" son:

# "flags=re.IGNORECASE" o "re.I"
# Este modificador hace que la búsqueda sea insensible a mayúsculas y minúsculas, lo que significa que la expresión regular coincidirá con texto en cualquier combinación de mayúsculas y minúsculas.

# "flags=re.MULTILINE" o "re.M"
# Este modificador permite que la búsqueda se realice en varias líneas de texto.
# Por ejemplo, si tienes un texto con saltos de línea y deseas buscar un patrón en cada línea, puedes usar este modificador.

# "flags=re.DOTALL" o "re.S"
# Este modificador hace que el carácter punto (".") en la expresión regular coincida con cualquier carácter, incluyendo saltos de línea ("\n").
# Sin este modificador, el punto no coincidiría con saltos de línea por defecto.

# "flags=re.VERBOSE" o "re.X"
# Este modificador permite que escribas expresiones regulares de forma más legible al ignorar espacios en blanco y comentarios en la expresión.
# Esto puede hacer que las expresiones regulares complejas sean más fáciles de entender.

# "flags=re.ASCII" o "re.A"
# Este modificador hace que la búsqueda se realice solo en caracteres ASCII, lo que excluye caracteres no ASCII de la coincidencia.


# Para usar uno o varios de estos modificadores, simplemente los pasas como argumento al parámetro "flags" cuando llamas a una función del módulo "re", como "re.search()", "re.findall()", "re.compile()", entre otras.
textoFlags = "Hola\nMundo\nPython"

# Usamos el modificador re.IGNORECASE para hacer la búsqueda insensible a mayúsculas y minúsculas
patronFlags = r"python"
coincidencia = re.search(patronFlags, textoFlags, flags=re.IGNORECASE)

if coincidencia:
    print(f"Coincidencia encontrada con el parámetro 'flags=IGNORECASE': {coincidencia.group()}")
else:
    print("No se encontró ninguna coincidencia.")

# En este ejemplo, el uso de "flags=re.IGNORECASE" permite que la búsqueda sea insensible a mayúsculas y minúsculas, por lo que encuentra la coincidencia "Python" en el texto a pesar de las diferencias de mayúsculas y minúsculas.


# Los modificadores en el parámetro flags son útiles para personalizar y ajustar la búsqueda de patrones de expresiones regulares según tus necesidades específicas.
