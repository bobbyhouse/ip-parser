#!/usr/bin/env python
# Tor node Parser
# Scrapes https://www.dan.me.uk/torlist for ip list import into SIEM via CEF/Syslog
# bobbyhouse at gmail.com
# https://github.com/bobbyhouse/ip-parser
#
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
