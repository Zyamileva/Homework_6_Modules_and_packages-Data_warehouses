import xml.etree.ElementTree as ET

XML_FILE = "file_products.xml"
tree = ET.parse(XML_FILE)
root = tree.getroot()
products = []


def get_info_products() -> list:
    """Get products from XML"""
    for product in root.findall("product"):
        dict_product = {
            "name": product.find("name").text,
            "price": product.find("price").text,
            "quantity": product.find("quantity").text,
        }
        products.append(dict_product)
    return products


def update_product_quantity():
    """
    Changes the quantity of the product in the XML file.
    """
    found = False
    product_name = input("Enter product name: ")
    for product in root.findall("product"):
        name = product.find("name").text
        if name == product_name:
            product.find("quantity").text = str(input("Enter new quantity: "))
            found = True
            break
    if found:
        tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)
        print(f"The product {product_name} quantity has been changed.")
    else:
        print(f"Product  {product_name}not found.")


if __name__ == "__main__":
    products = get_info_products()
    print("Products:")
    print(*products, sep=", ")

    update_product_quantity()
    products_new = get_info_products()
