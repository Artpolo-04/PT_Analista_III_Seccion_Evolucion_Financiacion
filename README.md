# 📊 PT_Analista_III_Seccion_Evolucion_Financiacion

## 📝 Descripción

Este proyecto tiene como objetivo procesar y analizar datos de ventas, generando reportes en formato Excel con resúmenes de ventas por vendedor y por mes. El proyecto está compuesto por varias clases que se encargan de cargar, procesar y generar los reportes de ventas.

## 📂 Estructura del Proyecto

- 📁 `input/` → Carpeta que contiene el archivo de datos de ventas en formato Excel.
- 📁 `output/` → Carpeta donde se guardará el archivo Excel generado con los resúmenes de ventas.
- 📁 `src/` → Carpeta que contiene el código fuente del proyecto.
  - 📜 `SalesDataLoader.py` → Clase para cargar y limpiar los datos de ventas desde un archivo Excel.
  - 📜 `SalesProcessor.py` → Clase para procesar y calcular métricas de ventas.
  - 📜 `SalesReportGenerator.py` → Clase para generar un archivo Excel con los resúmenes de ventas.
  - 🚀 `main.py` → Script principal que coordina la carga, procesamiento y generación de reportes.

## ⚙️ Instalación

1️⃣ Clonar este repositorio en tu máquina local.

2️⃣ Crear un entorno virtual y activarlo:

    python -m venv venv
    venv\Scripts\activate

3️⃣ Instalar las dependencias necesarias:

    pip install -r requirements.txt

## ▶️ Uso

    Ejecuta el archivo principal main.py

## 🏗️ Clases

### 📌 SalesDataLoader
        📥 Clase para cargar y limpiar los datos de las ventas del archivo Excel.

### 📌 SalesProcessor
        📊 Clase para procesar y calcular las métricas de total de ventas por vendedor y total de ventas por mes.

### 📌 SalesReportGenerator
        📑 Clase para generar el archivo resultante en la carpeta output/.