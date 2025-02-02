import json
import xml.etree.ElementTree as ET

JSON_FILE = "file_products.json"
XML_FILE = "file_products.xml"


def parse_element(element):
    """Recursively parses the XML file and transforms its dictionary"""
    parsed_data = {}

    for child in element:
        if len(child) > 0:
            value = parse_element(child)
        else:
            value = child.text

        if child.tag in parsed_data:
            if isinstance(parsed_data[child.tag], list):
                parsed_data[child.tag].append(value)
            else:
                parsed_data[child.tag] = [parsed_data[child.tag], value]
        else:
            parsed_data[child.tag] = value

    return parsed_data


def converter():
    """Converts XML у JSON"""
    try:
        tree = ET.parse(XML_FILE)
        root = tree.getroot()

        data = {root.tag: parse_element(root)}

        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"File {XML_FILE} successfully converted to {JSON_FILE}")

    except ET.ParseError:
        print("Parsing error XML")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    converter()
