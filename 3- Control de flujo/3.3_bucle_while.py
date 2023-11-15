# --- BÚCLE WHILE ---

# Este búcle te permite repetir un bloque de código mientras se cumpla una condición específica.
# El código dentro del búcle while se ejecutará una y otra vez mientras la condición sea verdadera.

# Sintaxis del búcle While
# Ejemplo con un contador:
contador = 1

while contador <= 5:
    print(f"El contador es: {contador}")
    contador += 1   # Incrementa el contador en 1 cada iteración

print("¡Búcle completado!")


# ERRORES
# Hay que tener cuidado con que se nos haga búcles infinitos.
# Por ejemplo si en el anterior ejemplo no colocara la suma del contador, el búcle se repetiria infinitamente.
