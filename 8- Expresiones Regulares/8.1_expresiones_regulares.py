# EXPRESIONES REGULARES


# Las expresiones regulares, también conocidas como "regex" o "regexp", son una herramienta poderosa para buscar, manipular y validar cadenas de texto en Python y otros lenguajes de programación.

# Las expresiones regulares son patrones de búsqueda y manipulación de texto.
# Estos patrones se utilizan para buscar, extraer o reemplazar subcadenas dentro de un texto más grande.
# Las expresiones regulares son especialmente útiles cuando necesitas realizar búsquedas complejas o manipular texto de una manera específica.
# Las expresiones regulares pueden volverse mucho más complejas y potentes a medida que adquieres más experiencia.

# Para poder utilizar estas expresiones se importa el módulo "re"
import re


# --- "METACARACTERES" ---
# Los metacaracteres son caracteres especiales que tienen significados especiales en las expresiones regulares.

# Algunos de los más comunes son:
# . : Coincide con cualquier carácter excepto una nueva línea.
# * : Coincide con 0 o más repeticiones del carácter o patrón anterior.
# + : Coincide con 1 o más repeticiones del carácter o patrón anterior.
# ? : Coincide con 0 o 1 repetición del carácter o patrón anterior.
# ^ : Coincide con el inicio de una cadena.
# $ : Coincide con el final de una cadena.
# [] : Define un conjunto de caracteres.
# () : Agrupa patrones juntos.
# \d : Busca digitos númericos.
# \D : Busca todo MENOS digitos númericos del [0 - 9].
# \w : Busca caracteres alfanuméricos [a-z, A-Z, 0-9, _].
# \W : Busca todo MENOS caracteres alfanuméricos [a-z, A-Z, 0-9, _].
# \s : Busca espacios en blanco [espacio, tabs, saltos en linea].
# \S : Busca todo MENOS espacios en blanco [espacio, tabs, saltos en linea].
# \n : Busca saltos en linea.
# \ : Cancelamos caracteres especiales.
# {n} : Busca n cantidad de veces el valor de la izquierda.
# {n,m} : Busca al menos n, como máximo m.
# | : Busca un cosa o la otra.

# Caracteres de Escape: Si desea buscar un metacarácter literal (por ejemplo, .), debe escaparlo con una barra invertida (\.) para que se trate como un carácter normal.
# Clases de Caracteres: Puede definir clases de caracteres utilizando corchetes. Por ejemplo, [aeiou] coincidirá con cualquiera de las vocales.
# Cuantificadores: Los cuantificadores se usan para especificar cuántas veces se debe repetir un carácter o un grupo. Algunos ejemplos son *, +, ?, {n}, {n,}, {n,m}.
# Secuencias de Escape: Puede utilizar secuencias de escape para buscar caracteres especiales, como \d para dígitos, \s para espacios en blanco y \w para caracteres alfanuméricos.

# Aserciones en Expresiones Regulares.
# Las aserciones son patrones que establecen condiciones antes o después de una coincidencia principal sin incluir esas condiciones en la coincidencia final. Algunas de las aserciones comunes son:

# \b : Aserción de límite de palabra, coincide con el límite entre un carácter de palabra (letras, dígitos o guiones bajos) y un carácter que no es una palabra. Útil para buscar palabras completas.
# \B : Aserción de límite negativo de palabra, coincide con el límite entre dos caracteres que son ambos palabras o no palabras.
# (?=...) : Aserción positiva hacia adelante (lookahead), verifica si una parte de la cadena está seguida por un patrón específico. Por ejemplo, patrón1(?=patrón2) coincide con patrón1 solo si está seguido por patrón2.
# (?!...) : Aserción negativa hacia adelante (lookahead negativo), verifica si una parte de la cadena no está seguida por un patrón específico. Por ejemplo, patrón1(?!patrón2) coincide con patrón1 solo si no está seguido por patrón2.

# Ejemplo de uso de \b: \bword\b coincidirá con la palabra "word" solo si está rodeada por límites de palabra.
# Las aserciones son útiles para realizar coincidencias más precisas y contextuales en texto.


# Ejemplos
# Coincidencia de números de teléfono: Supongamos que deseas encontrar números de teléfono en un texto.
# Los números de teléfono en EE. UU. tienen un formato de xxx-xxx-xxxx.
# Puedes usar la siguiente expresión regular:
texto = "Mi número de teléfono es 123-456-7890 y otro número es 987-654-3210."
patron = r'\d{3}-\d{3}-\d{4}'  # \d representa un dígito

# Buscar coincidencias en el texto
coincidencias = re.findall(patron, texto)
print(coincidencias)

# Esta expresión regular r'\S+@\S+' busca cualquier cadena que contenga un "@" entre caracteres que no sean espacios en blanco.



# r"patrón"
# El prefijo "r" antes de una cadena de texto se utiliza para indicar una "cadena cruda" o "raw string".
# Este prefijo "r" es opcional pero comúnmente se utiliza en expresiones regulares para evitar interpretaciones especiales de caracteres de escape como \n o \t.
# En una cadena cruda, los caracteres de escape se interpretan de manera literal, lo que significa que no se consideran secuencias de escape.
# Esto es útil en expresiones regulares porque a menudo se utilizan barras invertidas \ como parte de la sintaxis de las expresiones regulares, y queremos que se interpreten literalmente en lugar de como secuencias de escape de Python.
# Aquí tienes un ejemplo de cómo usar "r" en una expresión regular para validar correos electrónicos:

patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
correo = "usuario@example.com"

if re.match(patron, correo):
    print("La dirección de correo electrónico es válida.")
else:
    print("La dirección de correo electrónico no es válida.")

# En este ejemplo, hemos utilizado "r" antes de la cadena que define la expresión regular.
# La expresión regular "r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'" busca validar una dirección de correo electrónico que cumple con ciertos patrones.
# El uso de "r" asegura que las barras invertidas dentro de la expresión regular se tomen literalmente y no como secuencias de escape especiales.
# En este caso, la expresión regular valida que la dirección de correo electrónico tenga el formato adecuado con un nombre de usuario, el símbolo '@', un dominio de correo y una extensión de dominio.
# Si la dirección de correo se ajusta a este patrón, el programa imprime "La dirección de correo electrónico es válida"; de lo contrario, imprime "La dirección de correo electrónico no es válida".
