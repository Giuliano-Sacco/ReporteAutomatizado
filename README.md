# 📊 Reporte Automatizado de Ventas

Este proyecto permite generar automáticamente reportes de ventas a partir de un archivo Excel, con un resumen diario de cantidades y montos, además de un gráfico visual de las ventas por día.

Ideal para automatizar tareas administrativas, análisis de ventas, o aprender a trabajar con `pandas`, `matplotlib` y archivos Excel en Python.

---

## 🧪 Instrucciones de Uso

### ⚙️ Requisitos

Asegurate de tener Python 3 instalado y luego ejecutá:

```bash
pip install -r requirements.txt
```

---

### 📁 Estructura del Proyecto

```
ReporteAutomatizado/
├── data/
│   └── ventas.xlsx        # Archivo de entrada con datos de ventas
├── output/                # Carpeta generada automáticamente con los reportes y gráficos
├── src/
│   └── main.py            # Script principal
├── requirements.txt       # Lista de dependencias del proyecto
└── README.md
```

---

### 📄 Formato del archivo `ventas.xlsx`

Debe estar ubicado en `data/ventas.xlsx` y tener las siguientes columnas:

| Fecha       | Cantidad | Precio Unitario |
|-------------|----------|------------------|
| 2025-05-25  | 2        | 100              |
| 2025-05-25  | 1        | 200              |
| 2025-05-26  | 3        | 150              |

> ⚠️ Las columnas deben llamarse **exactamente**: `Fecha`, `Cantidad`, `Precio Unitario`.

---

### 🚀 Cómo Ejecutar el Script

1. Abrí una terminal.
2. Navegá a la carpeta `src` del proyecto:

```bash
cd src
```

3. Ejecutá el script:

```bash
python3 main.py
```

---

### 📦 ¿Qué se genera?

Al correr el script, se crean dos archivos nuevos dentro de la carpeta `output/`:

- 📊 `reporte_YYYY-MM-DD.xlsx`: archivo Excel con el resumen total de ventas por día.
- 📈 `grafico_YYYY-MM-DD.png`: gráfico de las ventas totales por fecha.

---

### 🛠️ Tecnologías Utilizadas

- [Python 3](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)

---

## ✨ Autor

**Giuliano Sacco**  
[GitHub](https://github.com/Giuliano-Sacco)
