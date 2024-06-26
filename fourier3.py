from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# La mitad del período
l = 2.0

# Define la función que deseas integrar
def funcion(x):
    if -2 <= x < 0:
        return 0
    elif 0 <= x < 2:
        return 1
    else:
        return 0

# Calcular a0
result, error = quad(funcion, -l, l)
a0 = -np.pi/2

# Calcular ai
def ai(n):
    result = (((-1)**n)-1)/(np.pi*(n**2))
    return result

# Calcular bi
def bi(n):
    result = ((1-2*((-1)**n)))/n
    return result

# Imprime los resultados de los coeficientes
print("a0:", a0)
print("ai:", ai(1))
print("bi:", bi)

def serie_fourier(x, n, a0, ai, bi):
    # Término constante (a0)
    suma = (1/4)

    # Suma para i desde 1 hasta n
    for i in range(1, n + 1):
        suma += (4/((np.pi)**2))*(1/i**2)*(1-np.cos((i*np.pi)/2))*((np.cos((i*np.pi*x)/2)))
    return suma

# Crear una ventana emergente para ingresar el valor de n
from tkinter.simpledialog import askinteger

n = askinteger("Valor de n", "Ingrese el valor de n:")
# t = askinteger("Valor del periodo", "Ingrese el valor del periodo:")
t = 2*np.pi
l = t/2

# Verificar que se haya ingresado un valor válido para n
if n is not None:
    x_values = np.linspace(-2*l, 2*l, 1000)
    y_values = [serie_fourier(x, n, a0, ai, bi) for x in x_values]
    # y_original = [funcion(x) for x in x_values]

    # Crear un gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f'Suma parcial (n={n})', color='b')
    # plt.plot(x_values, y_original, label='Coseno 2', linestyle=':', color='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Serie de Fourier')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-2*l, 2*l)
    plt.show()
