# --- OPERADORES DE COMPARACION ---

# Valor - operador - valor
# Los operadores de comparación nos devuelven "True" o "False".

igual_que = 5 == 6       # Nos da "False" porque 5 no es igual que 6.
distinto_de = 5 != 6     # Nos da "True" porque 5 es distinto a 6.
mayor_que = 5 > 6        # Nos da "False" porque 5 no es mayor que 6.
menor_que = 5 < 6        # Nos da "True" porque 5 es menor que 6.
mayor_o_igual = 5 >= 6   # Nos da "False" porque 5 no es mayor o igual que 6.
menor_o_igual = 5 <= 6   # Nos da "True" porque 5 es menor aunque no igual que 6.


# Tambien podemos combinar distintos comparadores.
# Ejemplo con cálculos combinados:
a = 5
b = 10
c = 20
comparacion = a + b < c  # Nos dara "True" porque a+b es 15 y es menor que 20.
print(comparacion)


# Podemos comparar variables.
# Ejemplo de comparar usuario y contraseña:
contraseña_almacenada = "abeltomas02"
contraseña_escrita = "abeltomas00"
print(contraseña_almacenada == contraseña_escrita)  # Nos dara "False"
