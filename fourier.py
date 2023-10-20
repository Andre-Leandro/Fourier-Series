from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# La mitad del período
l = 2.0

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
funcion = crear_funcion_desde_cadena(expresion)

# Define la función que deseas integrar

# Calcular a0
result, error = quad(funcion, -l, l)
a0 = (1/l) * result

# Calcular ai
def ai(n):
    def aux(x):
        return np.cos((n/l)*np.pi*x) * funcion(x)
    result, error = quad(aux, -l, l)
    result = (1/l) * result
    return result

# Calcular bi
def bi(n):
    def aux(x):
        return np.sin((n/l)*np.pi*x) * funcion(x)
    result, error = quad(aux, -l, l)
    result = (1/l) * result
    return result

# Imprime los resultados de los coeficientes
print("a0:", a0)
print("ai:", ai(1))
print("bi:", bi)

def serie_fourier(x, n, a0, ai, bi):
    # Término constante (a0)
    suma = a0 / 2.0

    # Suma para i desde 1 hasta n
    for i in range(1, n + 1):
        suma += ai(i) * np.cos((i/l)*np.pi*x) + bi(i) * np.sin((i/l)*np.pi*x)

    return suma

# Crear una ventana emergente para ingresar el valor de n
from tkinter.simpledialog import askinteger

n = askinteger("Valor de n", "Ingrese el valor de n:")
t = askinteger("Valor del periodo", "Ingrese el valor del periodo:")
l = t/2

# Verificar que se haya ingresado un valor válido para n
if n is not None:
    x_values = np.linspace(-2*l, 2*l, 1000)
    y_values = [serie_fourier(x, n, a0, ai, bi) for x in x_values]
    y_original = [funcion(x) for x in x_values]

    # Crear un gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f'Suma parcial (n={n})', color='b')
    plt.plot(x_values, y_original, label='Coseno 2', linestyle=':', color='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Serie de Fourier')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-2*l, 2*l)
    plt.show()
