from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from tkinter import IntVar

def crear_funcion_desde_cadena(cadena):
    try:
        # Evalúa la cadena y crea una función
        funcion = eval(f"lambda x: {cadena}")
        return funcion
    except:
        # En caso de error, devuelve None
        return None

def obtener_datos():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter

    dialog = tk.Toplevel()
    dialog.title("Ingrese los datos")

    expresion_label = tk.Label(dialog, text="Expresión (ejemplo x**2):")
    expresion_entry = tk.Entry(dialog)
    expresion_label.pack()
    expresion_entry.pack()

    enable_expresion2 = IntVar()
    expresion2_label = tk.Label(dialog, text="Segunda expresión:")
    expresion2_entry = tk.Entry(dialog, state="disabled")
    expresion2_label.pack()
    expresion2_entry.pack()

    def habilitar_expresion2():
        if enable_expresion2.get() == 1:
            expresion2_entry["state"] = "normal"
        else:
            expresion2_entry["state"] = "disabled"

    radio_button = tk.Checkbutton(dialog, text="Habilitar segunda expresión", variable=enable_expresion2, command=habilitar_expresion2)
    radio_button.pack()

    n_label = tk.Label(dialog, text="Valor de n:")
    n_entry = tk.Entry(dialog)
    n_label.pack()
    n_entry.pack()

    t_label = tk.Label(dialog, text="Valor del periodo:")
    t_entry = tk.Entry(dialog)
    t_label.pack()
    t_entry.pack()

    aceptar_button = tk.Button(dialog, text="Aceptar", command=dialog.quit)
    aceptar_button.pack()

    dialog.mainloop()

    expresion = expresion_entry.get()
    expresion2 = expresion2_entry.get()
    n = int(n_entry.get())
    t = int(t_entry.get())

    dialog.destroy()

    return expresion, expresion2, n, t

def main():
    expresion, expresion2, n, t = obtener_datos()

    # Crea la función a partir de la cadena
    funcion = crear_funcion_desde_cadena(expresion)

    # La mitad del período
    l = t / 2.0

    # Calcular a0
    result, error = quad(funcion, -l, l)
    a0 = (1 / l) * result

    # Calcular ai
    def ai(n):
        def aux(x):
            return np.cos((n / l) * np.pi * x) * funcion(x)

        result, error = quad(aux, -l, l)
        result = (1 / l) * result
        return result

    # Calcular bi
    def bi(n):
        def aux(x):
            return np.sin((n / l) * np.pi * x) * funcion(x)

        result, error = quad(aux, -l, l)
        result = (1 / l) * result
        return result

    # Imprime los resultados de los coeficientes
    print("a0:", a0)
    print("ai:", ai(1))
    print("bi:", bi(1))

    def serie_fourier(x, n, a0, ai, bi):
        # Término constante (a0)
        suma = a0 / 2.0

        # Suma para i desde 1 hasta n
        for i in range(1, n + 1):
            suma += ai(i) * np.cos((i / l) * np.pi * x) + bi(i) * np.sin((i / l) * np.pi * x)

        return suma

    x_values = np.linspace(-2 * l, 2 * l, 1000)
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
    plt.xlim(-2 * l, 2 * l)
    plt.show()

if __name__ == "__main__":
    main()
