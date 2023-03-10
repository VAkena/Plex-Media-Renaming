# Author: VAkena
# Date: Janurary 9, 2023

# DESCRIPTION

# This script uses Filebot to mass rename Plex media, you will need a valid Filebot license
# Place this script inside a movies library, sample outputs of the file names have been provided
# Use the Filebot commandline documentation to customise the naming scheme to your liking

import os
import re
import logging

# Configure logging to file
logging.basicConfig(level=logging.DEBUG, filename="log.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - Line number: %(lineno)d - %(message)s', filemode='w')


def get_file_count(dir_path: str, pattern: str) -> int:
    """
    Args:
        dir_path: The location of the Plex library
        pattern: A regex pattern to match media files (.mkv and .mp4)
    """
    count = 0
    regex = re.compile(pattern)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if regex.match(file):
                count += 1
    return count


def get_files():
    media = re.compile(r'.*\.(mp4|mkv)')
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if media.match(file):
                logging.info(file)


def run_filebot_scan():
    # Expected output: She's Not Here (2023) (2160p HDR10 x265 20Mbps) (Dolby Digital 5.1).mkv
    # Expected output: She's Not Here (2023) (1080p x264 10Mbps) (AAC 2.0).mkv
    logging.info("Filebot has started renaming your files...")
    os.system(
        'filebot -rename *.mkv *.mp4 --db TheMovieDB  --format "{n} ({y}) ({vf} {hdr} {vc} {bitrate}) ({aco} {channels})" -non-strict --apply refresh')


def main():
    count = get_file_count("./", ".*\.(mp4|mkv)")

    logging.info("We found %d files", count)

    logging.info("Here are those file(s)")

    get_files()

    run_filebot_scan()

    logging.info("Here are your new file(s)")

    get_files()


if __name__ == "__main__":
    main()
