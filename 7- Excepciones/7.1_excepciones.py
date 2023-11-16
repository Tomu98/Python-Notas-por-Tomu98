# --- EXCEPCIONES ---

# Las excepciones son eventos inesperados o errores que pueden ocurrir durante la ejecución de un programa en Python.
# Estos errores pueden ser causados por diversas razones, como errores de sintaxis, problemas de lógica, operaciones matemáticas inválidas, intentos de acceder a variables inexistentes y más.
# Python maneja estas excepciones mediante un mecanismo de manejo de errores que te permite tomar acciones específicas cuando ocurren excepciones.
# El manejo de excepciones es fundamental para escribir programas robustos y evitar que se detengan inesperadamente debido a errores y tambien es una parte importante de la programación defensiva.


# Bloques "try", "except", y "finally"
# Para manejar excepciones en Python, puedes utilizar bloques "try", "except", y "finally".

# "try"
# Se utiliza para rodear el código que puede generar excepciones.
# Su función principal es detectar y controlar las excepciones que pueden ocurrir dentro de él.
# Si ocurre una excepción en el bloque "try", la ejecución del programa se desvía al bloque "except" correspondiente.
# Dentro del bloque "try", debes colocar el código que deseas supervisar en busca de excepciones.
# Puedes tener múltiples bloques "except", cada uno manejando un tipo diferente de excepción.
# Si se lanza una excepción que coincide con uno de los tipos especificados en los bloques "except", se ejecutará el bloque "except" correspondiente.

# "except"
# Se utiliza para manejar las excepciones que se producen dentro del bloque "try".
# Cada bloque "except" maneja un tipo particular de excepción y puede ejecutar código personalizado para manejar esa excepción.
# - "ExcepcionTipo" es el tipo de excepción que se está manejando.
# Puedes especificar el tipo de excepción después de la palabra clave "except".
# Dentro del bloque "except", puedes incluir código que se ejecutará cuando se capture la excepción correspondiente.

# "finally"
# El bloque "finally" es opcional y se utiliza para definir código que se ejecutará siempre, ya sea que se haya producido una excepción en el bloque "try" o no.
# Se usa comúnmente para realizar tareas de limpieza, como cerrar archivos o liberar recursos.
# El bloque "finally" se ejecutará después de que se haya ejecutado el bloque "try" y cualquier bloque "except" que corresponda a la excepción capturada.
# Incluso si no se produce ninguna excepción, el código en el bloque "finally" se ejecutará antes de que el programa continúe su ejecución normal.

# Ejemplo:
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No puedes dividir entre cero.")
        resultado = None
    finally:
        print("Limpieza de recursos o finalización de operación.")
    return resultado

# Prueba la función con diferentes casos
print(dividir(10, 2))  # Resultado válido
print(dividir(5, 0))   # Intento de división por cero

# En este ejemplo, la función "dividir" toma dos argumentos, "a" y "b", e intenta realizar la división.
# Dentro del bloque "try", se realiza la división, y si "b" es igual a cero, se produce una excepción "ZeroDivisionError".
# En ese caso, el bloque "except" maneja la excepción y muestra un mensaje de error.
# Luego, independientemente de si se produce una excepción o no, el bloque "finally" se ejecuta, lo que permite realizar la limpieza o finalización de operaciones necesarias.


# Otro ejemplo:
def sumar_dos():
    while True:
        a = input("Número 1: ")
        b = input("Número 2: ")
        try:
            resultado = int(a) + int(b)
        except ValueError as exc:
            print("Te pedí un número...")
            print(f"ERROR: {exc}")
        else:
            break
        finally:
            print("Esto se ejecuta siempre.")
    return resultado

print(sumar_dos())
