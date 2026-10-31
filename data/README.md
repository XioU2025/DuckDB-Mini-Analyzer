# DuckDB Mini Analyzer

Aplicación web sencilla para analizar archivos CSV mediante consultas SQL utilizando **Python, DuckDB y Streamlit**.

## Descripción del proyecto

DuckDB Mini Analyzer es una aplicación que permite cargar archivos CSV, visualizar sus registros y ejecutar consultas SQL para analizar información.

El proyecto fue desarrollado como una demostración práctica del funcionamiento de DuckDB y su capacidad para realizar análisis de datos locales sin necesidad de configurar un servidor de bases de datos tradicional.

## Tecnologías utilizadas

- **Python:** lenguaje de programación principal.
- **DuckDB:** motor de base de datos analítica para ejecutar consultas SQL.
- **Streamlit:** herramienta para crear la interfaz web.
- **Pandas:** procesamiento y visualización de datos.

## Funcionalidades

- Visualización de datos de ejemplo.
- Carga de archivos CSV desde la computadora.
- Ejecución de consultas SQL.
- Visualización de resultados en tablas.
- Agrupación y cálculo de datos mediante SQL.
- Manejo de errores en las consultas.

## Estructura del proyecto

```
DuckDB_Mini_Analyzer/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── ventas.csv
│
└── README.md
```

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DE_TU_REPOSITORIO
```

### 2. Entrar a la carpeta

```bash
cd DuckDB_Mini_Analyzer
```

### 3. Crear un entorno virtual

```bash
py -m venv .venv
```

### 4. Activar el entorno virtual

En Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 6. Ejecutar la aplicación

```bash
python -m streamlit run app.py
```

La aplicación estará disponible en:

http://localhost:8501

## Ejemplos de consultas SQL

**Consultar todos los registros:**

```sql
SELECT * FROM ventas;
```

**Calcular las ventas por producto:**

```sql
SELECT
    producto,
    SUM(total) AS ventas_totales
FROM ventas
GROUP BY producto
ORDER BY ventas_totales DESC;
```

**Consultar productos de una categoría:**

```sql
SELECT *
FROM ventas
WHERE categoria = 'Accesorios';
```

## Ejemplo de funcionamiento

La aplicación utiliza un conjunto de datos de ventas que contiene información como:

- Fecha de venta.
- Nombre del producto.
- Categoría.
- Cantidad.
- Precio.
- Total de venta.

Estos datos pueden analizarse mediante consultas SQL ejecutadas con DuckDB.

## Objetivo académico

Demostrar el funcionamiento de DuckDB como herramienta de análisis SQL de datos locales, comprendiendo cómo se pueden consultar, filtrar y agrupar archivos CSV mediante una aplicación web sencilla.