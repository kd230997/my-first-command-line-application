# Function to check if the download is complete
import os
import time
import click
import requests

download_folder_config = "N:\YoutubeDownload"


def wait_for_download_complete(download_folder, timeout=60):
    end_time = time.time() + timeout
    while time.time() < end_time:
        files = os.listdir(download_folder)
        click.echo(f"Files in the directory: {files}")

        # Look for incomplete files (e.g., ".crdownload" for Chrome)
        if any(file.endswith(".crdownload") for file in files):
            click.echo("Download in progress...")
            time.sleep(1)  # Wait and check again
        else:
            return True  # Download is complete
    return False  # Timeout reached


def download_file(url, file_name):
    # Send a GET request to download the file
    response = requests.get(url, stream=True)

    file_path = os.path.join(download_folder_config, file_name)
    # Save the file
    with open(file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    print("Download complete:", file_name)
    return True
