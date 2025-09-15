import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for URL
    url = input("Enter the URL of the image: ").strip()

    # Directory to store images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Try fetching the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raise HTTP errors if any

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        save_path = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(save_path, "wb") as file:
            file.write(response.content)

        print(f"✅ Image saved successfully at: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Failed to fetch image: {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_image()
