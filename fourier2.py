from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# Ingresar el valor de los coeficientes a0, an, bn y el valor de w0
w0 = 1
a0 = -np.pi/2

# Ingresar an
def ai(n):
    a = (((-1)**n)-1)/((n**2)*np.pi)
    return a

# Ingresar bn
def bi(n):
    b = (1-(2*((-1)**n)))/n
    return b

# Imprime los resultados de los coeficientes
print("a0:", a0)
print("ai:", ai(1))
print("bi:", bi)

def serie_fourier(x, n, a0, ai, bi):
    # Término constante (a0)
    suma = a0 / 2.0

    # Suma para i desde 1 hasta n
    for i in range(1, n + 1):
        suma += ai(i) * np.cos(w0*i*x) + bi(i) * np.sin(w0*i*x)
    return suma

# Crear una ventana emergente para ingresar el valor de n
from tkinter.simpledialog import askinteger

n = askinteger("Valor de n", "Ingrese el valor de n:")
t = 2*np.pi/w0
l = t/2

# Verificar que se haya ingresado un valor válido para n
if n is not None:
    x_values = np.linspace(-2*l, 2*l, 1000)
    y_values = [serie_fourier(x, n, a0, ai, bi) for x in x_values]

    # Crear un gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f'Suma parcial (n={n})', color='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Serie de Fourier')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-2*l, 2*l)
    plt.show()
