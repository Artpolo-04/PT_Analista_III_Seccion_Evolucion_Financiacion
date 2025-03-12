from SalesDataLoader import SalesDataLoader
from SalesProcessor import SalesProcessor

if __name__ == "__main__":
    file_path = "input\datos_ventas.xlsx"
    output_file = "resumen_ventas.xlsx"

    # 1️⃣ Cargar y limpiar los datos.
    loader = SalesDataLoader(file_path)
    df = loader.load_data()


    # 2️⃣ Procesar los datos
    processor = SalesProcessor(df)
    sales_by_seller = processor.get_sales_by_seller()
    sales_by_month = processor.get_sales_by_month()
    print("Ventas por vendedor:\n", sales_by_seller.head())
    print("Ventas por mes:\n", sales_by_month.head())