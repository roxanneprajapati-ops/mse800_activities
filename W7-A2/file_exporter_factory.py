# factory.py
from file_exporter import CSVExporter, JSONExporter, XMLExporter, Exporter


class FileExporterFactory:
    @staticmethod
    def create_exporter(export_type: str) -> Exporter:
        export_type = export_type.strip().lower()

        if export_type == "csv":
            return CSVExporter()
        if export_type == "json":
            return JSONExporter()
        if export_type == "xml":
            return XMLExporter()

        raise ValueError("Invalid export type. Use: csv, json, xml")
