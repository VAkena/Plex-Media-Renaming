# Author: VAkena
# Date: Janurary 9, 2023

# DESCRIPTION

# This script uses Filebot to mass rename Plex media, you will need a valid Filebot license
# Place this script inside a movies library sample outputs of the file names have been provided
# Use the Filebot commandline documentation to customise naming scheme

import os
import fnmatch
import re
import logging
import glob

# Configure logging to file
logging.basicConfig(level=logging.DEBUG, filename="log.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - Line number: %(lineno)d - %(message)s', filemode='w')


def get_file_count(dir_path: str, pattern: str) -> int:
    """
    Args:
        dir_path: The directory where the Plex media is stored
        pattern: A regex pattern to match the file names.
    """
    count = 0
    regex = re.compile(pattern)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if regex.match(file):
                count += 1
    return count


def files_before_renaming():
    logging.info("Here are those file(s)")
    # Log media files before tagging
    files_found = glob.glob('./*.m*')

    for f in files_found:
        logging.info(f)


def files_after_renaming():
    logging.info("Here are your new file(s)")
    # Log media files before tagging
    files_found = glob.glob('./*.m*')

    for f in files_found:
        logging.info(f)


def run_filebot_scan():
    # Expected output: She's Not Here (2023) [2160p HDR10 x265 20Mbps] [Dolby Digital 5.1].mkv
    # Expected output: She's Not Here (2023) [1080p x264 10Mbps] [AAC 2.0].mkv
    logging.info("Filebot has started renaming your files...")
    os.system(
        'filebot -rename *.mkv *.mp4 --db TheMovieDB  --format "{n} ({y}) ({vf} {hdr} {vc} {bitrate}) ({aco} {channels})" -non-strict --apply refresh')


def main():
    count = get_file_count("./", ".*\.(mp4|mkv)")
    logging.info("We found %d files", count)

    files_before_renaming()

    run_filebot_scan()

    files_after_renaming()


if __name__ == "__main__":
    main()
