import pandas as pd

class SalesReportGenerator:
    """Clase para generar un archivo Excel con los resúmenes de ventas.

    Atributos:
        sales_by_seller (DataFrame): DataFrame con el total de ventas por vendedor.
        sales_by_month (DataFrame): DataFrame con el total de ventas por mes.
        output_file (str): Ruta del archivo Excel de salida.
    """

    def __init__(self, sales_by_seller, sales_by_month, output_file):
        """
        Inicializa la clase SalesReportGenerator con los datos de ventas y el archivo de salida.

        Args:
            sales_by_seller (DataFrame): DataFrame con el total de ventas por vendedor.
            sales_by_month (DataFrame): DataFrame con el total de ventas por mes.
            output_file (str): Ruta del archivo Excel de salida.
        """
        self.sales_by_seller = sales_by_seller
        self.sales_by_month = sales_by_month
        self.output_file = output_file

    def generate_excel_report(self):
        """
        Guarda los datos en un archivo Excel con hojas separadas.

        Crea un archivo Excel con dos hojas: una para el resumen de ventas por vendedor
        y otra para el resumen de ventas por mes.

        Returns:
            None
        """
        with pd.ExcelWriter(self.output_file) as writer:
            self.sales_by_seller.to_excel(writer, sheet_name="Resumen_Ventas", index=False)
            self.sales_by_month.to_excel(writer, sheet_name="Ventas_Mensuales", index=False)

        print(f"Archivo generado: {self.output_file}")