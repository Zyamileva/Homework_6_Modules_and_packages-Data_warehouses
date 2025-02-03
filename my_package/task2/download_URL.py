import requests


def download_page(url: str, filename: str) -> None:
    """Download a web page and save it to a file.
    This function retrieves the content of a given URL and writes it to a specified file.
    It handles potential HTTP errors and general request exceptions during the process.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        with open(filename, "w", encoding="utf8") as file:
            file.write(response.text)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading page: {e}")


if __name__ == "__main__":
    url_page = "https://www.russianfood.com/recipes/bytype/?fid=1023"
    file_name = "russian_food_recipe.html"
    download_page(url_page, file_name)
