# --- MIS EXCEPCIONES ---


# Si bien Python proporciona muchas excepciones predefinidas, a veces es útil crear tus propias excepciones personalizadas para manejar situaciones específicas de tu programa de manera más efectiva.
# Puedes definir excepciones personalizadas para reflejar problemas o situaciones únicas en tu aplicación.


# "raise"
# La palabra clave "raise" se utiliza para generar una excepción manualmente en Python.
# Permite que el programador genere una excepción específica cuando se cumple cierta condición.
# La sintaxis básica de "raise" es:
# "raise Exception("Mensaje de error")"

# - "raise": La palabra clave utilizada para levantar una excepción.
# - "Exception": El tipo de excepción que se está creando. En este caso, estamos utilizando la clase base "Exception".
# - "Mensaje de error": Un mensaje opcional que proporciona información adicional sobre la excepción.


# Clase "Exception"
# En Python, todas las excepciones son subclases de la clase base "Exception".
# Esto significa que puedes crear tus propias excepciones personalizadas extendiendo la clase "Exception".
# La estructura básica para definir una excepción personalizada es:
class MiExcepcionEjemplo(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# - "MiExcepcion": El nombre de la excepción personalizada que estás creando.
# - "Exception": Indica que tu excepción personalizada es una subclase de "Exception".
# - "__init__(self, mensaje)": El método constructor de la excepción personalizada, que toma un argumento "mensaje" para proporcionar información adicional sobre la excepción.
# - super().__init__(self.mensaje): Llama al constructor de la clase base Exception y pasa el mensaje como argumento para inicializar correctamente la excepción.


# Ejemplo:
# Definir una excepción personalizada
class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Función que simula una operación que podría generar la excepción personalizada
def dividir(a, b):
    if b == 0:
        raise MiExcepcion("No es posible dividir por cero")
    return a / b

# Uso de la excepción personalizada
try:
    numerador = 10
    divisor = 0
    resultado = dividir(numerador, divisor)
except MiExcepcion as e:
    print(f"Se ha producido una excepción personalizada: {e}")
else:
    print(f"El resultado de la división es: {resultado}")

# Definimos una excepción personalizada llamada "MiExcepcion" que hereda de la clase base "Exception".
# Esta excepción tiene un mensaje personalizado que se puede configurar al crear una instancia de la excepción.
# Creamos una función "dividir(a, b)" que toma dos argumentos y verifica si "b" es igual a cero.
# Si "b" es cero, levanta la excepción personalizada "MiExcepcion" con el mensaje "No es posible dividir por cero".
# De lo contrario, realiza la operación de división y devuelve el resultado.
# En el bloque "try"..."except", intentamos realizar una división con un divisor igual a cero, lo que debería generar nuestra excepción personalizada.
# Si se levanta la excepción, capturamos la instancia de la excepción en la variable "e" y mostramos el mensaje personalizado.
# Si no se levanta ninguna excepción, es decir, si la división se realiza con éxito, imprimimos el resultado.


# Este ejemplo ilustra cómo crear, levantar y manejar una excepción personalizada en Python.
# La excepción "MiExcepcion" nos permite comunicar de manera efectiva un problema específico (división por cero en este caso) y controlar cómo se maneja este error en nuestro código.
