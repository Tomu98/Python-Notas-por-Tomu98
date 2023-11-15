# --- CONDICIONALES ---

# IF - ELSE
# Es un pedazo de codigo que si se cumple, ejecuta una determinada tarea.
# Ejemplo de sintaxis con una edad:
edad = 19

if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")

# Ejemplo de contraseña:
contraseña_almacenada = "abeltomas02"
contraseña_escrita = "abeltomas02"

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESIÓN...")
else:
    print("CONTRASEÑA INCORRECTA, INTENTE DE NUEVO")


# IF - ELIF - ELSE
# En Python "else if" se escribe "elif".
# Si la primer condición no se cumple, NO vamos al "else" sino a una condición siguiente.
# Podemos agregar muchas otras condiciones con "elif".
# Podemos anidar tantos "if" como "elif" necesitemos.
# Ejemplo en un salario:
ingreso_mensual = 2000
gasto_mensual = 1000

if ingreso_mensual - gasto_mensual < 0:
    print("Estas en deficit locooo")
elif ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual >= 3000:
        print("Estas muy bien en cualquier parte del mundo")
    else:
        print("Estas gastando mucho")
elif ingreso_mensual >= 1000:
    if ingreso_mensual - gasto_mensual >= 400:
        print("Estas bien en Latinoamérica")
    else:
        print("Estas gastando bastante")
elif ingreso_mensual >= 500:
    if ingreso_mensual - gasto_mensual >= 200:
        print("Estas bien en Argentina")
    else:
        print("Estas en Argentina pero gastas mucho loco")
elif ingreso_mensual >= 250:
    if ingreso_mensual - gasto_mensual >= 65:
        print("Estas en Venezuela chico sos rico")
    else:
        print("EXPROPIECE")
else:
    print("Sos pobre X'D")


# MATCH
# Toma una expreción y la compara con diferentes casos con sus respectivos patrones a cumplir.
# Es similar a "switch" de C, Java o Javascript y muchos otros lenguajes.
# Agregamos la cantidad de casos posibles para ejecutar con "case".
# El ultimo "case" se pone "_" que actua como comodín y si ningún caso coincide, éste se ejecuta.
error_http = 400

match error_http:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")

# Tambien se pueden combinar muchos patrones en un solo case usando | ("or"):
error = 404
match error:
    case 401 | 403 | 404:
        print("Not allowed")
