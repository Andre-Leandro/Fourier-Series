import math
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import IntVar

def crear_funcion_desde_cadena(cadena):
    cadena = cadena.lower() 
    if cadena in ['sen(x)', 'sin(x)', 'cos(x)']:
        if cadena in ['sen(x)', 'sin(x)']:
            funcion = lambda x: math.sin(x)
        else:
            funcion = lambda x: math.cos(x)
        return funcion
    else:
        try:
            funcion = eval(f"lambda x: {cadena}")
            return funcion
        except:
            return None

def obtener_datos():
    root = tk.Tk()
    root.withdraw()  
    dialog = tk.Toplevel()
    dialog.title("Ingrese los datos")
    expresion_label = tk.Label(dialog, text="Ingrese la función f(x)")
    expresion_entry = tk.Entry(dialog)
    expresion_label.pack()
    expresion_entry.pack()
    enable_expresion2 = IntVar()
    expresion2_label = tk.Label(dialog, text="Segundo tramo")
    expresion2_entry = tk.Entry(dialog, state="disabled")
    expresion2_label.pack()
    expresion2_entry.pack()
    def habilitar_expresion2():
        if enable_expresion2.get() == 1:
            expresion2_entry["state"] = "normal"
        else:
            expresion2_entry["state"] = "disabled"
    radio_button = tk.Checkbutton(dialog, text="Habilitar segundo tramo", variable=enable_expresion2, command=habilitar_expresion2)
    radio_button.pack()
    n_label = tk.Label(dialog, text="Valor de n")
    n_entry = tk.Entry(dialog)
    n_label.pack()
    n_entry.pack()
    t_label = tk.Label(dialog, text="Valor del período")
    t_entry = tk.Entry(dialog)
    t_label.pack()
    t_entry.pack()
    aceptar_button = tk.Button(dialog, text="Aceptar", command=dialog.quit)
    aceptar_button.pack()
    dialog.mainloop()
    expresion = expresion_entry.get()
    expresion2 = expresion2_entry.get()
    n = int(n_entry.get())
    t = float(t_entry.get())
    dialog.destroy()
    return expresion, expresion2, n, t

def main():
    expresion, expresion2, n, t = obtener_datos()
    # Crea la función a partir de la cadena
    funcion2 = 0
    if (expresion2):
       funcion2 = crear_funcion_desde_cadena(expresion2)
    funcion = crear_funcion_desde_cadena(expresion)
    
    # La mitad del período
    l = t / 2.0
    result = 0
    if (expresion2):
        result1, error = quad(funcion, -l, 0)
        result2, error = quad(funcion2, 0, l)
        result = result1 + result2
    else:
        result, error = quad(funcion, -l, l)
    a0 = (1 / l) * result

    # Calcular ai
    def ai(n):
        def aux1(x):
            return np.cos((n / l) * np.pi * x) * funcion(x)
        def aux2(x):
            return np.cos((n / l) * np.pi * x) * funcion2(x)
        result = 0
        if (expresion2):
            result1, error = quad(aux1, -l, 0)
            result2, error = quad(aux2, 0, l)
            result = (1 / l) * (result1 + result2)
        else:
            result, error = quad(aux1, -l, l)
            result = (1 / l) * result
        return result

    # Calcular bi
    def bi(n):
        def aux1(x):
            return np.sin((n / l) * np.pi * x) * funcion(x)
        def aux2(x):
            return np.sin((n / l) * np.pi * x) * funcion2(x)
        result = 0
        if (expresion2):
            result1, error = quad(aux1, -l, 0)
            result2, error = quad(aux2, 0, l)
            result = (1 / l) * (result1 + result2)
        else:
            result, error = quad(aux1, -l, l)
            result = (1 / l) * result
        return result

    def serie_fourier(x, n, a0, ai, bi):
        suma = a0 / 2.0
        # Suma para i desde 1 hasta n
        for i in range(1, n + 1):
            suma += ai(i) * np.cos((i / l) * np.pi * x) + bi(i) * np.sin((i / l) * np.pi * x)
        return suma
    
    x_values = np.linspace(-6 * l, 6 * l, 1000)
    y_values = [serie_fourier(x, n, a0, ai, bi) for x in x_values]
    y_original = [funcion(x) for x in x_values]
    y_original2 = []
    # Crear un gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f'Suma parcial (n={n})', color='b')
    plt.plot(x_values, y_original, label='f1', linestyle=':', color='r')
    if (expresion2):
        y_original2 = [funcion2(x) for x in x_values]
        plt.plot(x_values, y_original2, label='f2', linestyle=':', color='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Serie de Fourier')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-2 * l, 2 * l)
    plt.show()
if __name__ == "__main__":
    main()