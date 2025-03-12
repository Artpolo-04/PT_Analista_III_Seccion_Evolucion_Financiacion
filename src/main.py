from SalesDataLoader import SalesDataLoader

if __name__ == "__main__":
    file_path = "input\datos_ventas.xlsx"
    output_file = "resumen_ventas.xlsx"

    # 1️⃣ Cargar y limpiar los datos.
    loader = SalesDataLoader(file_path)
    df = loader.load_data()
    print(df.head())
