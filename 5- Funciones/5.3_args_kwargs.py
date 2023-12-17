# *ARGS
# Permite que la función acepte cualquier cantidad de argumentos posicionales separados por coma.
# Puedes combinar "*args" con otros parámetros en la definición de una función, pero "*args" debe aparecer al final de la lista de parámetros.
# Los argumentos pasados después de "*args" deben ser proporcionados mediante keyword arguments.
# Su sintaxis es: *parámetro

# Ejemplo con una función que calcula el promedio de una lista variable de números:
def calcular_promedio(*args):
    total = sum(args)
    promedio = total / len(args)
    return promedio

resultado = calcular_promedio(10, 20, 40, 30)
print(f"El promedio es: {resultado}")


# **KWARGS
# KEYWORD ARGUMENTS (argumentos de palabra clave).
# Son una forma de pasar argumentos a una función utilizando nombres específicos para los parámetros.
# Hace que sea más claro y legible cuál es el propósito de cada argumento.
# El código se vuelve más claro, ya que los valores están explícitamente vinculados a los parámetros correspondientes.
# Puedes proporcionar los argumentos en cualquier orden, evita errores si una función tiene muchos parámetros.
# Pueden usarse para proporcionar valores predeterminados a los parámetros y permite a los usuarios sobrescribir esos valores si es necesario.

# Creando una función de 3 parámetros sin "Keyword Arguments":
def frase(nombre, apellido, adjetivo):
    return print(f"Hola {nombre} {apellido}, sos muy {adjetivo}")

frase("Abel", "Romero", "tontito")

# Creando la misma función agregando "Keyword Arguments":
def frase2(nombre, apellido, adjetivo="Tonto"):
    return print(f"Hola {nombre} {apellido}, sos muy {adjetivo}")

frase2("Abel", "Romero", "Inteligente")

# Tambien al llamar la función se puede agregar "Keyword Arguments":
def saludar(nombre, mensaje="Hola, ¿cómo estás?"):
    print(f"{mensaje} Soy {nombre}.")

saludar(nombre="Celeste", mensaje="¡Hola, bienvenida!")



# Otro ejemplo de ambos combinados:
def saludar_persona(*args, **kwargs):
    if args:
        nombre_completo = " ".join(args)
    else:
        nombre_completo = kwargs.get("nombre", "Desconocido")

    apellido = kwargs.get("apellido", "")
    apodo = kwargs.get("apodo", "")

    mensaje = f"Hola, {nombre_completo} {apellido} ({apodo})! ¡Bienvenido!"
    return mensaje

print(saludar_persona("Celeste", "Torcivia", apodo="Pecas"))
print(saludar_persona(nombre="Cristian", apellido="Parada", apodo="Power"))
print(saludar_persona(apodo="Capo"))
