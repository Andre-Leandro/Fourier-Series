def crear_funcion_desde_cadena(cadena):
    try:
        # Evalúa la cadena y crea una función
        funcion = eval(f"lambda x: {cadena}")
        return funcion
    except:
        # En caso de error, devuelve None
        return None

# Lee una cadena desde la terminal
expresion = input("Ingresa la expresión matemática (ejemplo: x**2): ")

# Crea la función a partir de la cadena
mi_funcion = crear_funcion_desde_cadena(expresion)

if mi_funcion:
    # Prueba la función
    x = 2
    resultado = mi_funcion(x)
    print(f"El resultado de la función para x={x} es: {resultado}")
else:
    print("La expresión ingresada no es válida.")