#!/usr/bin/env python
# Tor node Parser
# Scrapes https://www.dan.me.uk/torlist for ip list import into SIEM via CEF/Syslog
# bobbyhouse at gmail.com
# https://github.com/bobbyhouse/ip-parser
# Dan updates his list every 30 minutes
# Keep in mind he will block anyone that exceeds once every 30 min
#----------------------------------------------------------------------------
# 
#Copyright 2012 Bobby House
#
import os
import sys
import urllib2
import re
from datetime import datetime


URI = 'https://www.dan.me.uk/torlist'

message= "CEF:0|Tor Node|Tor Node |0.0.7|1|Suspect Tor Node |7|src={0} "

ip_regex = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")
        self.cr_pattern = re.compile("^.*\r", re.M)
        self.bs_pattern = re.compile(".\b")

    def write(self, message):
        self.terminal.write(message)
        message = self.bs_pattern.sub('', self.cr_pattern.sub('', message))
        self.log.write(message)

sys.stdout = Logger("Torlist.csv")
def main():

    try:
        # Get the data from the server
        resp = urllib2.urlopen(URI).read()
        ips = resp.split('\n')
        for ip in ips:
            if ip_regex.match(ip):
                print message.format(ip)

    except urllib2.HTTPError, e:
        print e
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()

