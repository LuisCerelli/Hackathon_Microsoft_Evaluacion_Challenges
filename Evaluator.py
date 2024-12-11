import matplotlib
matplotlib.use('Agg')  # Usar backend sin interfaz gráfica para guardar archivos
import matplotlib.pyplot as plt
import os

# Agregar los datos de los 7 desafíos
desafios = [
    "Accesibilidad para sitios web",
    "Innovación en búsquedas",
    "Corrección automática y validación rápida",
    "Detección de alucinaciones",
    "Observabilidad para sistemas de IA",
    "Filtrado de contenido basado en roles",
    "Voz RAG",
]
calificaciones_actualizadas = {
    "Accesibilidad para sitios web": {"Viabilidad": 3, "Rendimiento": 2.5, "Innovación": 2.5, "Amplitud": 3},
    "Innovación en búsquedas": {"Viabilidad": 2.5, "Rendimiento": 3, "Innovación": 3, "Amplitud": 2.5},
    "Corrección automática y validación rápida": {"Viabilidad": 2, "Rendimiento": 2.5, "Innovación": 2.5, "Amplitud": 2.5},
    "Detección de alucinaciones": {"Viabilidad": 2.5, "Rendimiento": 2.5, "Innovación": 3, "Amplitud": 2.5},
    "Observabilidad para sistemas de IA": {"Viabilidad": 3, "Rendimiento": 2.5, "Innovación": 2.5, "Amplitud": 3},
    "Filtrado de contenido basado en roles": {"Viabilidad": 1.5, "Rendimiento": 2, "Innovación": 2, "Amplitud": 1.5},
    "Voz RAG": {"Viabilidad": 2.5, "Rendimiento": 3, "Innovación": 3, "Amplitud": 2},
}

# Ordenar los desafíos según la calificación promedio
promedios = {desafio: sum(calificaciones_actualizadas[desafio].values()) / 4 for desafio in desafios}
desafios_ordenados = sorted(promedios.keys(), key=lambda x: promedios[x], reverse=True)

# Preparar datos ordenados
viabilidad_ordenada = [calificaciones_actualizadas[d]["Viabilidad"] for d in desafios_ordenados]
rendimiento_ordenado = [calificaciones_actualizadas[d]["Rendimiento"] for d in desafios_ordenados]
innovacion_ordenada = [calificaciones_actualizadas[d]["Innovación"] for d in desafios_ordenados]
amplitud_ordenada = [calificaciones_actualizadas[d]["Amplitud"] for d in desafios_ordenados]

# Crear el gráfico con colores más contrastados
plt.figure(figsize=(12, 6))

# Configurar colores contrastados
colores = ["red", "blue", "green", "orange"]

# Graficar cada criterio
plt.plot(desafios_ordenados, viabilidad_ordenada, marker='o', label="Viabilidad", color=colores[0])
plt.plot(desafios_ordenados, rendimiento_ordenado, marker='o', label="Rendimiento", color=colores[1])
plt.plot(desafios_ordenados, innovacion_ordenada, marker='o', label="Innovación", color=colores[2])
plt.plot(desafios_ordenados, amplitud_ordenada, marker='o', label="Amplitud", color=colores[3])

# Etiquetas y diseño
plt.title("Evaluaciones de los desafíos ejecutivos (ordenados por mejor promedio)", fontsize=14)
plt.xlabel("Desafíos", fontsize=12)
plt.ylabel("Calificación (1.5 a 3)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.ylim(1.5, 3)
plt.legend(title="Criterios", fontsize=10, loc="lower left")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Obtener la ruta del directorio actual (donde está Evaluator.py)
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Crear la carpeta de imágenes dentro del directorio actual
carpeta_imagenes = os.path.join(directorio_actual, "imagenes")
os.makedirs(carpeta_imagenes, exist_ok=True)

# Guardar el gráfico como PDF
ruta_pdf = os.path.join(carpeta_imagenes, "evaluacion_desafios.pdf")
plt.savefig(ruta_pdf)

print(f"Gráfico guardado en {ruta_pdf}")















