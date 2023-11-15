# --- PASS, CONTINUE, BREAK ---

# Son controles de flujo avanzados que se los puede utilizar en búcles y condicionales

# PASS
# Se utiliza como marcador cuando se requiere una declaración en un lugar donde el código aún no está completo.
# Si estas definiendo por ejemplo una clase, puedes usar "pass" para que el intérprete de Python no genere un error de sintaxis.

# Ejemplo en una clase aún por definir:
class Pass:
    pass     # La clase no hace nada de momento


# CONTINUE
# Se usa para saltar la iteración actual y pasar a la siguiente iteración en un búcle.
# Ejemplo con un búcle de números:
for numero in range(10):
    if numero % 2 == 0:
        continue     # Saltar números pares, continuar con la siguiente iteración

# Ejemplo con una lista de frutas:
frutas = ["Banana","Manzana","Pera","Kiwi","Naranja","Sandia","Pomelo"]
for fruta in frutas:
    if fruta == "Manzana":
        continue   # Cuando el búcle llegue a la palabra "manzana", pasará a la siguiente iteración


# BREAK
# Se utiliza para salir de manera prematura de un búcle, en función de una cierta condición.
# Sale inmediatamente del búcle y continúa con la ejecución de las instrucciones siguientes.
# Si está en un condicional el "else" no se ejecuta tampoco.
# Ejemplo con un búcle de números:
for numero in range(10):
    if numero == 5:
        break     # Salir del búcle cuando el número sea 5.
