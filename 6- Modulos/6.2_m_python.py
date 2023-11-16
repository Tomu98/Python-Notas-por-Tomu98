# MÓDULOS DE PYTHON

# Python cuenta con una amplia variedad de módulos incorporados que proporcionan funciones y características adicionales.
# Algunos de estos módulos son:

# math: Este módulo proporciona funciones matemáticas más avanzadas que las ya incluidas.
# Contiene funciones para realizar operaciones matemáticas más complejas, como funciones trigonométricas, exponenciales, logaritmos, etc.
import  math
# Abajo una lista de muchas funciones que contiene este módulo.
# Funciones trigonométricas:
seno = math.sin(10)          # Calcula el seno del ángulo x en radianes.
coseno = math.cos(40)        # Calcula el coseno del ángulo x en radianes.
tangente = math.tan(20)      # Calcula la tangente del ángulo x en radianes.
radianes = math.radians(40)  # Convierte grados a radianes.
# Funciones exponenciales y logarítmicas:
potencia_base_e = math.exp(5)    # Calcula el valor de exponenciales utilizando la base e.
logaritmo_natural = math.log(5)  # Calcula el logaritmo natural (base e) de x.
logaritmo_base = math.log10(10)  # Calcula el logaritmo base 10 de x.
# Funciones de redondeo:
ceil = math.ceil(5.6)       # Redondea x al entero más cercano hacia arriba.
floor = math.floor(5.4)     # Redondea x al entero más cercano hacia abajo.
trunc = math.trunc(5.73)    # Trunca x eliminando la parte decimal.
# Funciones de raíz y potenciación:
raiz = math.sqrt(25)          # Calcula la raíz cuadrada de x.
potencia = math.pow(3, 4)     # Calcula x elevado a la potencia y.
raiz_entera = math.isqrt(49)  # Calcula la raíz cuadrada entera de x.
# Funciones hiperbólicas:
seno_hiperbolico = math.sinh(40)     # Calcula el seno hiperbólico de x.
coseno_hiperbolico = math.cosh(40)   # Calcula el coseno hiperbólico de x.
tangente_hiperbolica = math.tanh(50) # Calcula la tangente hiperbólica de x.
# Funciones especiales:
factorial = math.factorial(30)   # Calcula el factorial de x.
gamma = math.gamma(30)           # Calcula la función gamma de x.
funcion_error = math.erf(30)     # Calcula la función de error de x.



# random: Este módulo es esencial para generar números aleatorios y realizar selecciones aleatorias.
import random
# Abajo una lista de algunas de las funciones que contiene.
# Generación de números aleatorios:
randomm = random.random()       # Genera un número aleatorio en el rango del 0 al 1.
uniform = random.uniform(1, 9)  # Genera un número float aleatorio en el rango (a, b).
randint = random.randint(1, 9)  # Genera un número entero aleatorio en el rango (a, b), ambos extremos incluidos.
# Selecciones aleatorias:
num = [1,2,3,4,5,6,7,8,9]
choice = random.choice(num)    # Elige un elemento aleatorio de la secuencia proporcionada.
random.shuffle(num)  # Mezcla la secuencia en su lugar (in-place), reorganizando los elementos en orden aleatorio.
sample = random.sample(num, 3) # Genera una muestra aleatoria sin reemplazo de tamaño x de la secuencia proporcionada (iterable, cantidad).
# Semilla de generador de números aleatorios:
random.seed(23) # Inicializa el generador de números aleatorios con una semilla dada.
# Usar la misma semilla produce la misma secuencia de números aleatorios.



# datetime: Permite realizar operaciones relacionadas con la manipulación de fechas, como crear, comparar, formatear y realizar cálculos con fechas y horas.
import datetime
# "datetime.date": Esta clase se utiliza para representar fechas sin información de hora. Puedes crear objetos "date" con año, mes y día.
# Por ejemplo, "datetime.date(2023, 9, 27)" representa el 27 de septiembre de 2023.
date = datetime.date(2023,9,27)
# "datetime.time": Esta clase se utiliza para representar horas, minutos, segundos y microsegundos.
# Puedes crear objetos "time" con información de hora, por ejemplo, "datetime.time(14, 30, 0)" representa las 2:30 PM.
datet_time = datetime.time(14,6,0)
# "datetime.datetime": Esta clase combina información de fecha y hora.
# Puedes crear objetos "datetime" especificando año, mes, día, hora, minutos, segundos y microsegundos.
# "datetime.timedelta": Esta clase se utiliza para representar una duración, es decir, una diferencia entre dos fechas o tiempos.
# Puedes realizar operaciones matemáticas con "timedelta", como sumar o restar días, horas, minutos, etc., a una fecha o tiempo.



# time: Este módulo proporciona funciones para trabajar con el tiempo y medir el tiempo transcurrido en tus programas. 
import time
# Algunas de sus funciones:
tiempo = time.time()  # Retorna el tiempo actual en segundos desde la época (1 de enero de 1970).
sleep = time.sleep(1) # Detiene la ejecución del programa durante el número especificado de segundos.
tiempo_actual = time.localtime() # Retorna la hora local actual como una tupla.
tiempo_actual_utc = time.gmtime() # Retorna la hora UTC (Tiempo Universal Coordinado) actual como una tupla.



# sys: Este módulo  proporciona funcionalidades que permiten interactuar con el intérprete de Python y el sistema operativo subyacente.
# Sin embargo, ten en cuenta que algunas de sus funciones son sensibles al sistema y pueden variar en diferentes plataformas.
import sys
# sys.argv:         Una lista que contiene los argumentos pasados al script desde la línea de comandos.
# sys.path:         Una lista de rutas de directorio donde Python busca módulos importables.
# sys.stdout:       El flujo estándar de salida (por defecto, la consola).
# sys.stderr:       El flujo estándar de error (por defecto, la consola).
# sys.exit(codigo): Sale del programa. Si se proporciona un código, se considera como un código de salida. El valor por defecto es 0.
# sys.getrecursionlimit():         Retorna el límite máximo de recursión.
# sys.setrecursionlimit(limite):   Establece el límite máximo de recursión.
sistema = sys.platform      # El nombre del sistema operativo subyacente.
py_version = sys.version    # La versión de Python.
# sys.stdin: El flujo estándar de entrada (por defecto, la consola).



# csv: csv: Este módulo proporciona funcionalidad para trabajar con archivos CSV (Comma-Separated Values), que son comunes para el intercambio de datos tabulares.
# import csv


# requests: Es un módulo popular para realizar solicitudes HTTP a través de la web, lo que lo hace ideal para interactuar con APIs y obtener datos de internet.
# import requests
# get = requests.get()  # Realiza una solicitud GET a la URL proporcionada.
# response.headers: Accede a los encabezados de la respuesta.
# response.status_code: Obtiene el código de estado de la respuesta.
# response.json(): Convierte el contenido JSON de la respuesta en un diccionario de Python.