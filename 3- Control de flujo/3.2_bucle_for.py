# BUCLE FOR

# Permite iterar sobre una secuencia de elementos, como listas, cadenas de texto, rangos numéricos u otras estructuras de datos.
# El bucle "for" se encarga automáticamente de recorrer cada elemento de la secuencia uno por uno.

# Sintaxis del bucle For
# for *variable* in *iterable*:
#       inicia la iteración hasta terminarla

# Ejemplo con una lista de frutas:
frutas = ["manzana", "banana", "naranja", "uva", "pera"]
for fruta in frutas:
    print(f"Me gusta comer una {fruta}")
print("¡Bucle de frutas completado!")

# Ejemplo con una lista de animales:
animales = ["Gato", "Perro", "Loro", "Cocodrilo", "Pez"]
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
print("¡Bucle de animales completado!")

# Ejemplo con una cadena de texto:
cadena = "Hola, Abel Tomas"
for letra in cadena:
    print(letra)
print("¡Bucle de cadena de texto completado!")

# Se puede combinar dentro del código muchas condiciones, agregando condicionales u operadores.
# Ejemplo al recorrer una lista de números y multiplicarlos por 10:
numeros = [4, 52, 35, 7, 23]
for numero in numeros:
    resultado = numero * 10
    print(resultado)
print("¡Bucle de lista de números multiplicados completado!")


# "for" en una sola línea de código
# Ejemplo duplicando números:
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)


# Forma correcta de iterar una lista con su índice:
# Se utiliza "enumerate()".
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El índice es: {indice} y el valor es: {valor}")


# Para poder iterar dos listas o más se utiliza "zip()"
# Las listas tienen que tener las mismas cantidades de datos.
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")


# Iteraciones con diccionarios
# Ejemplos iterando un diccionario para obtener las claves:
diccionario = {
    "Nombre":"Abel",
    "Apellido":"Romero",
    "Edad":24
}
for key in diccionario:
    print(f"La clave es: {key}")

# Iterando un diccionario con "items():" para obtener la clave y el valor:
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor: {value}")
