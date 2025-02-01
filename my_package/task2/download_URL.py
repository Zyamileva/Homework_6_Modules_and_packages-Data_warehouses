import requests


def download_page(url, filename):
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
    file_name = "russian_food_recipes.html"
    download_page(url_page, file_name)
