import os
from file_exporter_factory import FileExporterFactory

def main():
    cars_data = [
        {"id": 1, "name": "Toyota Corolla", "year": 2020, "price_per_day": 55},
        {"id": 2, "name": "Honda Civic", "year": 2019, "price_per_day": 50},
        {"id": 3, "name": "Mazda 3", "year": 2021, "price_per_day": 60},
    ]
    export_type = input("Select export format (csv/json/xml): ").strip().lower()

    # implementing the factory pattern
    exporter = FileExporterFactory.create_exporter(export_type)

    file_path = f"exports/dataset.{export_type}"
    result = exporter.export(cars_data, file_path)
    print(result)
    print(f"Export complete: {file_path}")

if __name__ == "__main__":
    main()