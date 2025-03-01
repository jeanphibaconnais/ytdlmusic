"""
search utils scripts
"""
from termcolor import colored
from ytdlmusic.log import print_debug
from ytdlmusic.params import param_number

try:
    from youtubesearchpython import VideosSearch
except ImportError:
    print_debug("youtubesearchpython import problem")


def search(keywords):
    """
    search the items with youtube-search-python
    return a json with 5 entries of YouTube results
    param : the artist and the song
    """

    print_debug("search : " + keywords)
    print(
        colored(
            'search "' + keywords + '" with youtube-search-python',
            "green",
        )
    )
    my_limit = int(param_number())
    return VideosSearch(keywords, limit=my_limit)
