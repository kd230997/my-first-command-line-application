import click
import yt_dlp


def download_ydl(url, file_name):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Download highest video + audio quality
        "merge_output_format": "mp4",  # Ensure MP4 output
        "outtmpl": f"N:\YoutubeDownload\{file_name}.%(ext)s",  # Output filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


@click.command()
@click.option("-u", "--url", default="", help="Provide the URL of the video")
@click.option("-n", "--name", default="", help="Provide the file name")
def download(url, name):
    click.echo(f"Downloading {url}!")
    download_ydl(url, name)
