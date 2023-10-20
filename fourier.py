from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

#la mitad del periodo
l = 2.0

# Define la función que deseas integrar
def funcion(x):
    if -2 <= x < 0:
        return 0
    elif 0 <= x < 2:
        return 1
    else:
        # Fuera de los intervalos especificados, puedes retornar otro valor si es necesario
        return 0  # En este caso, se retorna 0 fuera de los intervalos

# Calcular a0
result, error = quad(funcion, -l, l)
a0 = (1/l) * result

# Calcular ai
def ai(n):
    def aux(x):
        return np.cos( (n/l)*np.pi*x) * funcion(x)
    result, error = quad(aux, -l, l)
    result = (1/l) * result
    return result

# Calcular bi
def bi(n):
    def aux(x):
        return np.sin( (n/l)*np.pi*x) * funcion(x)
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
        suma += ai(i) * np.cos((i/l)*np.pi*x) + bi(i) * np.sin((i/l)* np.pi* x)

    return suma


# Crea un rango de valores para el eje x (por ejemplo, de 0 a 4π)
n = 15
x_values = np.linspace(-2*l, 2*l, 1000)
y_values = [serie_fourier(x, n, a0, ai, bi) for x in x_values]
y_original = [funcion(x) for x in x_values]

# Calcula la suma de los dos cosenos

# Crea un gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=f'Suma parcial (n={n})', color='b')
plt.plot(x_values, y_original, label='Coseno 2', linestyle=':', color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Serie de Fourier')
plt.legend()
plt.grid(True)

# Muestra el gráfico
plt.show()