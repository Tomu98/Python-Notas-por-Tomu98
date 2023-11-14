# ----- TIPOS DE DATOS -----

# Podemos poner diferentes tipos de datos: Textos, numeros y booleanos.

# Texto (String o "str")
# Para colocar un texto se utiliza comillas dobles o simples.
# Con un solo par de comillas, el dato solo ocupara un espacio.
texto1 = 'string'   # Par de comillas simples.
texto2 = "string"   # Par de comillas dobles.

# Mientras que tres pares, utilizará varios espacios.
texto3 = '''Tus datos son:
        nombre: Abel            
        apellido: Romero'''   # Tres pares de comillas simples.
texto4 = """Tus datos son:
        nombre: Abel
        apellido: Romero"""   # Tres pares de comillas dobles.


# Números Integer y Floating-point (int y float)
# Para colocar números solo se agrega el número sin comillas.
numero_int = 40       # "Int" para números enteros.
numero_float = 40.1   # "Float" para números racionales, se utiliza punto.


# Booleanos (bool)
# Datos booleanos, es para definir o comprobar que dato es verdadero o falso.
verdadero = True  # bool verdadero
falso = False     # bool falso



# CONCATENAMIENTO
# La acción de combinar o unir dos o más strings en una sola cadena más larga.
# Se puede concatenar con "+":
bienvenida = "Hola" + " ¿Como estas?"
print(bienvenida)

# Tambien se puede concatenar con "f-strings"
# Es la interpolación de variables y expresiones en cadenas de una manera más legible y conveniente.
# Las "f-strings" te permiten incrustar valores de variables y expresiones dentro de cadenas.
nombre = "Abel"
edad = 24
cadena = f"Hola, me llamo {nombre} y tengo {edad} años."
print(cadena)

# Las "f-strings" también pueden contener expresiones más complejas:
numero = 42
resultado = f"{numero} al cuadrado es: {numero ** 2}."
print(resultado)
