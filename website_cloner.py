import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited_urls = set()  # To keep track of visited pages
output_dir = "cloned_website"  # Directory to save the cloned website


def clone_website(base_url, current_url):
    """
    Clone a website by fetching and saving all linked pages within the same domain.
    """
    if current_url in visited_urls:
        return  # Skip if already visited

    try:
        # Fetch the page content
        print(f"Cloning: {current_url}")
        response = requests.get(current_url)
        response.raise_for_status()
        visited_urls.add(current_url)

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Save the HTML to a local file
        save_html(base_url, current_url, soup)

        # Find and process all linked pages
        for link in soup.find_all("a", href=True):
            href = link['href']
            absolute_url = urljoin(base_url, href)

            # Only follow URLs within the same domain
            if is_valid_url(absolute_url, base_url):
                clone_website(base_url, absolute_url)

    except Exception as e:
        print(f"Failed to clone {current_url}: {e}")


def save_html(base_url, current_url, soup):
    """
    Save the HTML content of the current page to the output directory.
    """
    # Convert URL to a file path
    parsed_url = urlparse(current_url)
    file_path = os.path.join(
        output_dir,
        parsed_url.netloc,
        parsed_url.path.lstrip('/')
    )

    # If the URL ends with a '/', save it as 'index.html'
    if not os.path.basename(file_path):
        file_path = os.path.join(file_path, "index.html")

    # Create directories if they don't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Rewrite links in the HTML to be relative
    for tag in soup.find_all(["a", "link", "script", "img"]):
        attr = "href" if tag.name in ["a", "link"] else "src"
        if tag.has_attr(attr):
            tag[attr] = urljoin(base_url, tag[attr])

    # Save the HTML content
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(soup))


def is_valid_url(url, base_url):
    """
    Check if a URL is valid and within the same domain as the base URL.
    """
    parsed_url = urlparse(url)
    parsed_base = urlparse(base_url)
    return (
        parsed_url.scheme in ["http", "https"]
        and parsed_url.netloc == parsed_base.netloc
    )


if __name__ == "__main__":
    # Get the website URL from the user
    base_url = input("Enter the website URL to clone (e.g., https://example.com): ").strip()

    # Validate the input URL
    if not base_url.startswith(("http://", "https://")):
        print("Invalid URL. Please include 'http://' or 'https://'.")
    else:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Start cloning the website
        clone_website(base_url, base_url)

        print(f"\nCloning complete! The website is saved in the '{output_dir}' directory.")
