from abc import ABC, abstractmethod
import csv
import json
import os
import xml.etree.ElementTree as ET


class Exporter(ABC):
    @abstractmethod
    def export(self, data: list[dict], file_path: str) -> None:
        pass


class CSVExporter(Exporter):
    def export(self, data: list[dict], file_path: str) -> None:
        if not data:
            raise ValueError("No data to export.")

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class JSONExporter(Exporter):
    def export(self, data: list[dict], file_path: str) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)


class XMLExporter(Exporter):
    def export(self, data: list[dict], file_path: str) -> None:
        root = ET.Element("records")

        for item in data:
            record = ET.SubElement(root, "record")
            for key, value in item.items():
                field = ET.SubElement(record, key)
                field.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
