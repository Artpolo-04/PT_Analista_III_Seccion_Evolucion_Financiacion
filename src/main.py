from SalesDataLoader import SalesDataLoader
from SalesProcessor import SalesProcessor
from SalesReportGenerator import SalesReportGenerator

if __name__ == "__main__":
    file_path = "input\datos_ventas.xlsx"
    output_file = "output\\resumen_ventas.xlsx"

    # 1️⃣ Cargar y limpiar los datos.
    loader = SalesDataLoader(file_path)
    df = loader.load_data()


    # 2️⃣ Procesar los datos
    processor = SalesProcessor(df)
    sales_by_seller = processor.get_sales_by_seller()
    sales_by_month = processor.get_sales_by_month()

    # 3️⃣ Generar el reporte en Excel
    report = SalesReportGenerator(sales_by_seller, sales_by_month, output_file)
    report.generate_excel_report()
