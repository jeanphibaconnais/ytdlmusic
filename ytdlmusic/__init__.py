"""
ytdlmusic scripts
"""

import sys
from ytdlmusic.ytdlmusic import job
from ytdlmusic.update import update, fullupdate
from ytdlmusic.batch import launch_batch
from ytdlmusic.print import (
    print_error,
    print_version_ytdlmusic,
    print_version_dependencies,
    print_licence,
)
from ytdlmusic.params import (
    is_fullupdate,
    is_update,
    is_version,
    is_batch,
    param_batch,
    param_search,
)


def ytdlmusic():

    """
    entry point from ytdlmusic
    """
    try:
        if is_update():
            update()
        elif is_fullupdate():
            fullupdate()
        elif is_version():
            print_version_ytdlmusic()
            print_version_dependencies()
            print_licence()
        elif is_batch():
            launch_batch(param_batch())
        else:
            job(param_search())
        sys.exit(0)
    except Exception as err:
        print_error(err)
        sys.exit(1)
