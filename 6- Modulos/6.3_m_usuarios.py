# --- MÓDULOS DE USUARIOS ---

# Los módulos creados por los usuarios en Python son archivos ".py" que contienen código reutilizable.
# Permiten organizar y reutilizar tus funciones y clases en diferentes programas.
# Mejora la modularidad y el mantenimiento del código.
# Ten cuidado que los archivos que contienen simbolos puedan generar errores al llamarlos, por eso el módulo de ejemplo tiene un nombre sencillo.

import ejemplo_modulos as em

ejemplo_saludo = em.saludar("Abel")
print(ejemplo_saludo)

ejemplo_despedirse = em.despedirse("Abel")
print(ejemplo_despedirse)


# __PYCACHE__
# La carpeta "__pycache__" es una carpeta especial que Python utiliza para almacenar archivos compilados en caché, conocidos como "archivos de caché de bytecode".
# Estos archivos de caché almacenan versiones precompiladas del código fuente de tus módulos, lo que permite que Python ejecute tu código más rápido en futuras ocasiones.
# Para evitar la recompilación repetida del mismo código fuente cada vez que se ejecuta tu programa, Python guarda estos archivos de caché de bytecode en la carpeta "__pycache__".

# La creación de la carpeta "__pycache__" y sus archivos asociados ocurre bajo las siguientes condiciones:
# Importación del módulo:
# - Cuando importas un módulo en tu programa, Python busca si ya existe una versión precompilada del módulo en la carpeta "__pycache__".
# - Si existe, la utiliza para acelerar la carga del módulo. Si no existe, Python crea un nuevo archivo de caché de bytecode en esta carpeta.
# Cambios en el módulo:
# - Si realizas cambios en el código fuente de un módulo (por ejemplo, el archivo .py), Python detectará que el código ha cambiado y automáticamente invalidará el archivo de caché de bytecode existente.
# - La próxima vez que importes el módulo, Python recompilará el código y creará un nuevo archivo de caché de bytecode.
# Versión de Python:
# - Los archivos de caché de bytecode son específicos de la versión de Python que estás utilizando.
# - Si actualizas Python a una nueva versión, los archivos de caché antiguos pueden no ser compatibles y Python los recompilará automáticamente.

# Si deseas limpiar la carpeta de caché, puedes hacerlo manualmente eliminando los archivos .pyc o utilizando herramientas proporcionadas por Python para esta tarea.
