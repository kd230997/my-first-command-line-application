from selenium import webdriver


# Set up Chrome options
chrome_options = webdriver.ChromeOptions()

# Configure Chrome to download files automatically
prefs = {
    "download.default_directory": "N:\YoutubeDownload",  # Change this path
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
chrome_options.add_argument("--enable-logging")
chrome_options.add_argument("--v=1")  # Increase verbosity

ssyoutube_url = "https://ssyoutube.online"

driver = webdriver.Chrome(options=chrome_options)


# def download(url):
#     # Open the website
#     driver.get(f"{ssyoutube_url}")

#     # Find the download URL input field and download button
#     download_url = driver.find_element(By.ID, "videoURL")
#     download_url.send_keys(url)
#     download_button = driver.find_element(By.ID, "download")
#     download_button.click()

#     mp4_download_btn = driver.find_element(
#         By.CSS_SELECTOR,
#         "#content > div > div.row > div.col-md-12.results > table > tbody > tr:nth-child(14) > td:nth-child(3) > span > button",
#     )
#     if mp4_download_btn:
#         click.echo("Found button " + mp4_download_btn.text)
#     else:
#         click.echo("not found")

#     mp4_download_btn.click()

#     audio_download_btn = driver.find_element(By.CLASS_NAME, "download-audio-button")
#     video_download_btn = driver.find_element(By.CLASS_NAME, "download-video-button")
#     file_name = driver.find_element(By.CLASS_NAME, "videoTitle").text
#     if file_name is not None:
#         file_name = re.sub(r"[^\w\s]", "", file_name.lower()).replace(" ", "_")

#     url_download_video = video_download_btn.get_attribute("data-url")
#     url_download_audio = audio_download_btn.get_attribute("data-url")

#     completed_download = download_file(
#         url=url_download_video, file_name=f"{file_name}.mp4"
#     )
#     completed_download = download_file(url_download_audio, f"{file_name}.m4a")

#     if completed_download:
#         click.echo("Download complete!")
#     else:
#         click.echo("Download failed!")
