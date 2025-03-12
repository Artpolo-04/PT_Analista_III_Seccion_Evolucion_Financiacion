class SalesProcessor:
    """Clase para procesar y calcular métricas de ventas.

    Atributos:
        df (DataFrame): DataFrame que contiene los datos de ventas.
    """

    def __init__(self, df):
        """
        Inicializa la clase SalesProcessor con un DataFrame.

        Args:
            df (DataFrame): DataFrame que contiene los datos de ventas.
        """
        self.df = df

    def get_sales_by_seller(self):
        """
        Calcula el total de ventas por vendedor.

        Returns:
            DataFrame: DataFrame con el total de ventas por vendedor.
        """
        return self.df.groupby('Vendedor')['Total_Venta'].sum().reset_index()

    def get_sales_by_month(self):
        """
        Calcula el total de ventas por mes.

        Returns:
            DataFrame: DataFrame con el total de ventas por mes.
        """
        return self.df.groupby('Mes')['Total_Venta'].sum().reset_index()