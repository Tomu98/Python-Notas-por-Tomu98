# --- INPUTS ---

# Son datos que se ingresan en un programa durante su ejecución
# Se pueden obtener utilizando la función input()
nombre = input("Escriba su nombre: ")
print(nombre)

# El dato que nos va a devolver un input es SIEMPRE un TEXTO.
# Para convertir ese input en un número, se utiliza "int()" o "float()"
numero_int = int(input("Escriba un numero entero: "))
numero_float = float(input("Escriba un número racional: "))
print(numero_int)
print(numero_float)
