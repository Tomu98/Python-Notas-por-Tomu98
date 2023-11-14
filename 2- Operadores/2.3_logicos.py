# --- OPERADORES LOGICOS ---

# Estos operadores comparan datos para devolver un dato booleano

# and (&): Devuelve "True" si ambas expresiones son verdaderas y "False" en cualquier otro caso.
and1 = True & True    # Devuelve True.
and2 = False & True   # Devuelve False.
and3 = True & False   # Devuelve False.
and4 = False & False  # Devuelve False.


# or (|): Devuelve "False" si ambas condiciones no se cumplen y "True" en cualquier otro caso.
or1 = True | True    # Devuelve True.
or2 = False | True   # Devuelve True.
or3 = True | False   # Devuelve True.
or4 = False | False  # Devuelve False.


# not: Devuelve el valor opuesto a la expresión dada.
# Si la expresión es verdadera, devuelve "False", y si la expresión es falsa, devuelve "True".
not1 = not True   # Devuelve False.
not2 = not False  # Devuelve True.


# Ejemplo:
a = 2
b = 4

if a < 4 and b > 6:
    print("Ambas expresiones son verdaderas")
else:
    print("Una expresion es falsa")
