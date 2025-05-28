import pandas as pd
from datetime import datetime

# Leer archivo
df = pd.read_excel("../data/ventas.xlsx", engine="openpyxl")


# Agregar columna total por venta
df["Total"] = df["Cantidad"] * df["Precio Unitario"]

# Agrupar por fecha
resumen = df.groupby("Fecha").agg({
    "Cantidad": "sum",
    "Total": "sum"
}).reset_index()

# Guardar resultado
fecha_actual = datetime.now().strftime("%Y-%m-%d")
resumen.to_excel(f"../output/reporte_{fecha_actual}.xlsx", index=False)

print("Reporte generado correctamente.")


import matplotlib.pyplot as plt

# Gráfico
plt.figure(figsize=(8,4))
plt.plot(resumen["Fecha"], resumen["Total"], marker='o')
plt.title("Ventas Totales por Día")
plt.xlabel("Fecha")
plt.ylabel("Total ($)")
plt.grid(True)

# Guardar gráfico
plt.savefig(f"../output/grafico_{fecha_actual}.png")
