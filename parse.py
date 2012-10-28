#!/usr/bin/env python

import os
import re
import sys
import urllib2
from datetime import datetime
from HTMLParser import HTMLParser


# Globals
# -------
PATH = './'
FILE = 'tor-ips'
FILETYPE = 'csv'
URI = 'https://www.dan.me.uk/torlist'


def main():

    # Get the current date time and format
    # i.e. Month-Day-YearTHour:Minute:Second
    timestamp = datetime.now().strftime("%m-%d-%yT%H:%M:%S")

    # Use the constants defined earlier to create our filename
    file_name = "{0}-{1}.{2}".format(FILE, timestamp, FILETYPE)

    # Use the constants defined earlier to get the absolute path of the file
    # that we will write to
    path_to_file = os.path.join(os.path.abspath(PATH), file_name)


    try:
        # Get the data from the server
        resp = urllib2.urlopen(URI).read()

        # Open a file for writing
        # If the file already exists it will be overwritten
        f = open(path_to_file, 'w')

        # Write the header of the file
        f.write("Addy\n")

        # Write the data to the file
        f.write(resp)

        # Close stream to open file
        f.close()

    except urllib2.HTTPError, e:
        print e
        sys.exit(1)


    sys.exit(0)



if __name__ == "__main__":
    main()
