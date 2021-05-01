"""
ytdlmusic batch
"""

import csv
import sys
from ytdlmusic.ytdlmusic import job
from ytdlmusic.print import print_error_batch
from ytdlmusic.params import is_verbose, is_auto
from ytdlmusic.log import print_debug


def launch_batch(param):
    """
    batch launcher
    """
    try:
        batch(param)
    except Exception as err:
        print_error_batch(err)
        sys.exit(1)


def batch(
    params
):
    """
    batch job
    """
    file_path=params[0]
    has_header=params[1]
    separator=params[2]
    search = ""

    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(
            csvfile, delimiter=separator, quotechar="|"
        )
        if has_header == "True":
            next(reader, None)
        for row in reader:
                search=""
                if is_verbose():
                    print_debug(
                        str(reader.line_num) + " en cours : " + str(row)
                    )
                for element in range(3, len(params)):
                    search = search + " " +row[int(params[element]) - 1]    
                job(search.replace(" ","",1))
