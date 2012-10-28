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
URI = 'http://localhost:3000'


"""
TorParser is a class that overrides the default HTMLParser
implementation to write IP addresses to a file

"""
class TorParser(HTMLParser):

    """
    Keep a reference to the file stream
    """
    def __init__(self, f):
        self.__f = f
        HTMLParser.__init__(self)

    def __isIP(self, string):
        regex = r'^[0-9]+(?:\.[0-9]+){3}$'
        return re.match(regex, string) == True

    """
    Write IP address to a file
    """
    def handle_data(self, data):
        line = "{0}\n".format(data)

        if self.__isIP(data):
            print "+ {0}".format(data)
            self.__f.write(data)


def main():

    # Get the current date time and format
    # i.e. Month-Day-YearTHour:Minute:Second
    timestamp = datetime.now().strftime("%m-%d-%yT%H:%M:%S")

    # Use the constants defined earlier to create our filename
    file_name = "{0}-{1}.{2}".format(FILE, timestamp, FILETYPE)

    # Use the constants defined earlier to get the absolute path of the file
    # that we will write to
    path_to_file = os.path.join(os.path.abspath(PATH), file_name)

    # Open a file for writing
    # If the file already exists it will be overwritten
    f = open(path_to_file, 'w')

    # Write the header of the file
    f.write("Addy\n")

    # Get the data from the server
    resp = urllib2.urlopen(URI).read()

    # Stop doing work if we don't get back any data and exit
    if not resp
        print "Didn't get a response from the server"
        sys.exit(0)

    # Create a new instance of our parser function and give it a handle
    # to our file
    torParser = TorParser(f)

    # Invoke parse
    torParser.feed(resp)

    # Close stream to open file
    f.close()


if __name__ == "__main__":
    main()
