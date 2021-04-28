"""
main class ytdlmusic
"""

import sys
from ytdlmusic.search import search
from ytdlmusic.choice import choice
from ytdlmusic.file import (
    determine_filename,
    determine_finame_from_tag,
)
from ytdlmusic.download import download_song
from ytdlmusic.print import print_error
from ytdlmusic.params import compute_args, is_tag
import os


def job(keywords):
    """
    principale use case
    auto : True if not interactive choice
    """
    try:
        results = search(keywords)
        answer = choice(results)
        if answer != 0:
            item = results.result()["result"][answer - 1]
            filename = determine_filename(keywords, item["title"])
            download_song(
                item["link"],
                filename,
            )
            if is_tag():
                newfilename = determine_finame_from_tag(filename)
                os.rename(filename, newfilename)
                filename = newfilename
            print(filename + " is ready")
    except Exception as err:
        print_error(err)
        sys.exit(1)
