from setuptools import setup

setup(
    name="yt-utility",
    version="1.0",
    py_modules=["yt-utility"],
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "yt-download=src.cli.youtube_cli:download",
        ],
    },
)