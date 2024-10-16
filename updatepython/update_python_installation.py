import requests
import os
import re
from bs4 import BeautifulSoup

PYTHON_DL_PAGE = "https://www.python.org/ftp/python"
PYTHON_VERSIONS = "python-versions.html"


def download_file(url, destination):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        # Open the destination file in binary write mode
        with open(destination, 'wb') as file:
            # Write the content in chunks to avoid using too much memory
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File downloaded successfully: {destination}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")


def extract_latest_version(html_file):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    latest_version = ""
    try:
        # Open and read the HTML file
        with open(html_file, 'r', encoding='utf-8') as file:
            content = file.read().splitlines()
        for line in content:
            date_str = re.findall(r'>(\d+\.\d+\.\d+.)/<', line)
            if (date_str):
                latest_version = date_str
                print(f"latest python version: {latest_version}\n")
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    download_file(PYTHON_DL_PAGE, PYTHON_VERSIONS)
    extract_latest_version(PYTHON_VERSIONS)


if __name__ == "__main__":
    main()
