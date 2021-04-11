from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ytdlmusic",
    version="0.1.8",
    description="With ytdlmusic, you can download from youtube a mp3 music without use browser. 5 choices are available with small summary to facilitate the choice. You can also use auto mode to download the first item.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thib1984/ytdlmusic",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="mit",
    packages=["ytdlmusic"],
    install_requires=["setuptools", "youtube-search-python", "youtube_dl"],
    zip_safe=False,
    entry_points={
        "console_scripts": ["ytdlmusic=ytdlmusic.__ytdlmusic__:ytdlmusic"],
    },
)
