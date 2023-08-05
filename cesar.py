import tkinter as tk

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            mayuscula = letra.isupper()
            letra = letra.upper()
            ascii_code = ord(letra)
            desplazado = (ascii_code - 65 + desplazamiento) % 26 + 65
            if not mayuscula:
                desplazado = chr(desplazado).lower()
            else:
                desplazado = chr(desplazado)
            resultado += desplazado
        else:
            resultado += letra
    return resultado

def cifrar_texto():
    texto_original = entrada_texto.get()
    desplazamiento_texto = entrada_desplazamiento.get()

    if not desplazamiento_texto.isdigit():
        etiqueta_resultado.config(text="Error: Ingresa un número válido para el desplazamiento", fg="red", font=("Arial", 12, "bold"))
        return

    desplazamiento = int(desplazamiento_texto)
    texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
    etiqueta_resultado.config(text="Texto cifrado: " + texto_cifrado, fg="blue", font=("Arial", 16))

# Crear la ventana
ventana = tk.Tk()
ventana.title("Cifrado César")
ventana.geometry("400x300")  # Tamaño de la ventana

# Crear widgets
etiqueta_instrucciones = tk.Label(ventana, text="Ingresa el texto a cifrar y el desplazamiento:", font=("Arial", 14))
etiqueta_instrucciones.pack()

entrada_texto = tk.Entry(ventana, font=("Arial", 14))
entrada_texto.pack()

entrada_desplazamiento = tk.Entry(ventana, font=("Arial", 14))
entrada_desplazamiento.pack()

boton_cifrar = tk.Button(ventana, text="Cifrar", font=("Arial", 14), command=cifrar_texto, bg="green", fg="white")
boton_cifrar.pack()

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 16))
etiqueta_resultado.pack()

ventana.mainloop()
