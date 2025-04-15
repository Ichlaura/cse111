import tkinter as tk
from tkinter import filedialog, messagebox
import pytesseract
from PIL import Image
import pandas as pd

# Configurar pytesseract (si es necesario indicar la ruta de instalación)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ruta en Windows

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Evaluación de Respuestas")
root.geometry("500x600")  # Tamaño de la ventana

# Establecer color de fondo y fuente
root.config(bg="#f0f0f0")
font = ("Helvetica", 12)

# Variables para almacenar las respuestas
respuestas_estudiantes = []
respuestas_profesor = []

# Crear un Frame para organizar los elementos
frame_principal = tk.Frame(root, bg="#f0f0f0")
frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

# Función para cargar las respuestas de los estudiantes
def cargar_respuestas_estudiantes():
    filepaths = filedialog.askopenfilenames(title="Seleccionar hojas de respuestas de estudiantes", filetypes=[("Imagen", "*.png;*.jpg;*.jpeg")])
    if filepaths:
        respuestas_estudiantes.clear()
        respuestas_estudiantes.extend(filepaths)  # Guardar las rutas de los archivos
        messagebox.showinfo("Éxito", f"{len(filepaths)} respuestas de estudiantes cargadas correctamente.")

# Función para cargar la hoja de respuesta del profesor
def cargar_respuesta_profesor():
    filepath = filedialog.askopenfilename(title="Seleccionar hoja de respuesta del profesor", filetypes=[("Imagen", "*.png;*.jpg;*.jpeg")])
    if filepath:
        respuestas_profesor.clear()
        respuestas_profesor.append(filepath)  # Guardar la ruta de la respuesta del profesor
        messagebox.showinfo("Éxito", "Hoja de respuestas del profesor cargada correctamente.")

# Función para realizar el análisis OCR de las respuestas
def analizar_respuestas():
    if not respuestas_estudiantes or not respuestas_profesor:
        messagebox.showerror("Error", "Por favor, cargue las respuestas de los estudiantes y la respuesta correcta primero.")
        return

    # Cargar la respuesta correcta (del profesor)
    respuesta_profesor_img = Image.open(respuestas_profesor[0])
    respuesta_profesor_text = pytesseract.image_to_string(respuesta_profesor_img)

    # Agregar depuración para verificar el texto extraído del profesor
    print("Respuesta Profesor: ", respuesta_profesor_text)  # Debugging line

    # Simulando la comparación con las respuestas de los estudiantes
    estudiantes = []
    puntajes = []
    for filepath in respuestas_estudiantes:
        estudiante_img = Image.open(filepath)
        estudiante_text = pytesseract.image_to_string(estudiante_img)

        # Agregar depuración para verificar el texto de cada estudiante
        print(f"Respuesta Estudiante ({filepath}): ", estudiante_text)  # Debugging line

        # Aquí iría la comparación real con las respuestas correctas
        puntaje = 90 if estudiante_text.strip() == respuesta_profesor_text.strip() else 70
        estudiantes.append(filepath.split("/")[-1])  # Nombre del archivo como identificador
        puntajes.append(puntaje)

    # Crear DataFrame para los resultados
    resultados = pd.DataFrame({
        "Estudiante": estudiantes,
        "Puntaje": puntajes
    })

    # Mostrar los resultados en una nueva ventana
    ventana_resultados = tk.Toplevel(root)
    ventana_resultados.title("Resultados")
    text_area = tk.Text(ventana_resultados, wrap="word", height=10, width=50)
    text_area.insert(tk.END, resultados.to_string(index=False))
    text_area.pack(padx=10, pady=10)

# Función para mostrar estadísticas (simulada)
def mostrar_estadisticas():
    if not respuestas_estudiantes or not respuestas_profesor:
        messagebox.showerror("Error", "Por favor, cargue las respuestas de los estudiantes y la respuesta correcta primero.")
        return

    # Agregar depuración para mostrar las respuestas cargadas
    print("Respuestas de estudiantes: ", respuestas_estudiantes)
    print("Respuesta del profesor: ", respuestas_profesor)

    # Estadísticas simuladas (por ejemplo, promedio de puntajes)
    promedio = sum([90, 85, 95]) / 3  # Ejemplo de promedio
    estadisticas = f"Promedio de los estudiantes: {promedio:.2f}"

    # Mostrar las estadísticas en una nueva ventana
    ventana_estadisticas = tk.Toplevel(root)
    ventana_estadisticas.title("Estadísticas")
    text_area = tk.Text(ventana_estadisticas, wrap="word", height=5, width=40)
    text_area.insert(tk.END, estadisticas)
    text_area.pack(padx=10, pady=10)

# Función para descargar las hojas de respuestas (simulando)
def descargar_hoja_respuestas(tipo="pequeño"):
    # Aquí puedes agregar la lógica para descargar el PDF o archivo correspondiente
    messagebox.showinfo("Descarga", f"Hoja de respuestas {tipo} descargada.")

# Crear un Frame para los botones de carga y análisis
frame_botones = tk.Frame(frame_principal, bg="#f0f0f0")
frame_botones.pack(fill="x", pady=10)

# Botones de cargar y analizar
boton_cargar_respuestas_estudiantes = tk.Button(frame_botones, text="Cargar Respuestas Estudiantes", command=cargar_respuestas_estudiantes, width=30, height=2, bg="#4CAF50", fg="white", font=font)
boton_cargar_respuestas_estudiantes.pack(pady=5)

boton_cargar_respuesta_profesor = tk.Button(frame_botones, text="Cargar Respuesta Profesor", command=cargar_respuesta_profesor, width=30, height=2, bg="#4CAF50", fg="white", font=font)
boton_cargar_respuesta_profesor.pack(pady=5)

boton_analizar_respuestas = tk.Button(frame_botones, text="Analizar Respuestas", command=analizar_respuestas, width=30, height=2, bg="#2196F3", fg="white", font=font)
boton_analizar_respuestas.pack(pady=5)

boton_mostrar_estadisticas = tk.Button(frame_botones, text="Mostrar Estadísticas", command=mostrar_estadisticas, width=30, height=2, bg="#FFC107", fg="white", font=font)
boton_mostrar_estadisticas.pack(pady=5)

# Crear un Frame para los botones de descarga de hojas
frame_descarga = tk.Frame(frame_principal, bg="#f0f0f0")
frame_descarga.pack(fill="x", pady=10)

# Botones de descarga
boton_descargar_pequeno = tk.Button(frame_descarga, text="Descargar Hoja Pequeña", command=lambda: descargar_hoja_respuestas("pequeña"), width=30, height=2, bg="#FF5722", fg="white", font=font)
boton_descargar_pequeno.pack(pady=5)

boton_descargar_mediano = tk.Button(frame_descarga, text="Descargar Hoja Mediana", command=lambda: descargar_hoja_respuestas("mediana"), width=30, height=2, bg="#FF5722", fg="white", font=font)
boton_descargar_mediano.pack(pady=5)

boton_descargar_grande = tk.Button(frame_descarga, text="Descargar Hoja Grande", command=lambda: descargar_hoja_respuestas("grande"), width=30, height=2, bg="#FF5722", fg="white", font=font)
boton_descargar_grande.pack(pady=5)

# Iniciar la interfaz gráfica
root.mainloop()
