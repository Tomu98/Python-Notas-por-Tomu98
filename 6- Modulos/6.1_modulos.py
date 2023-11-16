# --- MÓDULOS ---

# Son archivos que contienen funciones, variables y clases que pueden ser utilizadas en otros programas mediante la importación.
# Ayudan a organizar y reutilizar el código de manera eficiente.
# Hay módulos estándar de Python y módulos creados por otros usuarios.
# Se puede importar módulos creados por ti mismo.
# La función del modulo pasaría a utilizarse como método.


# Importar con "import":
# "Import (módulo), (módulo2//opcional)"
# Para importar un modulo se escribe la palabra "import" sefuido del modulo que queremos utilizar.
# Podemos importar la cantidad de modulos que necesitemos, separandolos con una coma.

# Alias con "as":
# "Import (módulo) as (nuevo nombre)"
# Para cambiarle el nombre a los módulos que importemos se utiliza "as", sirve para evitar conflicos con nombres largos.

# Importar algo específico con "from":
# "from (módulo) import (función/variable especifica)"
# Si solo queremos importar una función o variable especifica, utilizamos "from" para llamar unicamente a esta y no todos los archivos.

# Importar con "from" y "as":
# "from (módulo) import (función/variable especifica) as (nombre nuevo)"
# También podemos cambiar el nombre a ese dato especifico que llamamos.

# Importar todo con "*". (----menos recomendado----)
# "from (módulo) import *"
# Se utiliza el asterisco "*" para llamar a todas las funciones y variables del módulo directamente.
# Esto puede hacer que sea más difícil rastrear el origen de las funciones.
# Puede causar conflictos de nombres si hay funciones con nombres similares en otros módulos importados.

# Importar Clases:
# "from (módulo) import (clase)"
# Puedes importar clases específicas desde un módulo y utilizarlas para crear objetos y llamar a sus métodos.

# Importación Condicional con "if __name__ == '__main__'":
# "if __name__ == __main__: "
#      Código que se ejecuta solo cuando se ejecuta este archivo directamente
# El código bajo esta estructura solo se ejecuta cuando el archivo se ejecuta directamente y no cuando se importa como un módulo.
