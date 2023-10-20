from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets
from IPython.display import display

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

def serie_fourier(x, n, a0, ai, bi):
    suma = a0 / 2.0
    for i in range(1, n + 1):
        suma += ai(i) * np.cos((i/l)*np.pi*x) + bi(i) * np.sin((i/l)*np.pi*x)
    return suma

def update_plot(n=15):
    x_values = np.linspace(-2*l, 2*l, 1000)
    y_values = [serie_fourier(x, n, a0, ai, bi) for x in x_values]
    y_original = [funcion(x) for x in x_values]

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

# Crea un widget interactivo para modificar n
interact(update_plot, n=widgets.IntSlider(min=1, max=30, step=1, value=15))

# Muestra el gráfico inicial
update_plot(15)
