import pandas as pd
from datetime import datetime

class SalesDataLoader:
    """Clase para cargar y limpiar los datos de ventas desde un archivo Excel."""
    
    def __init__(self, file_path: str):
        """
        Inicializa la instancia de SalesDataLoader.

        Args:
            file_path (str): La ruta del archivo Excel que contiene los datos de ventas.
        """
        self.file_path = file_path
        self.df = None

    def load_data(self) -> pd.DataFrame:
        """
        Carga los datos en un DataFrame y maneja valores faltantes.

        Returns:
            pd.DataFrame: Un DataFrame con los datos de ventas limpios y procesados.
        """
        self.df = pd.read_excel(self.file_path)

        # En caso de ser nulo llena total_venta con la multiplicación de cantidad por precio unitario
        self.df['Total_Venta'] = self.df['Total_Venta'].fillna(self.df['Cantidad'] * self.df['Precio_Unitario'])

        # Convertir 'Fecha' a tipo datetime
        self.df['Fecha'] = pd.to_datetime(self.df['Fecha'], errors='coerce')

        # filtro de 2023
        self.df = self.df[self.df['Fecha'].dt.year == 2023]

        # Agregar columna 'Mes' 
        self.df['Mes'] = self.df['Fecha'].dt.month
        return self.df



