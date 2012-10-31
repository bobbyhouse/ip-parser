#!/usr/bin/env python

import os
import sys
import urllib2
import re
from datetime import datetime


URI = 'https://www.dan.me.uk/torlist'

message= "CEF:0|Tor Node|Tor Nodes 0.1|100|1|Malicious {0}|1|shost={0} cs1={0} \
cs1Label=Source  cs2={0} cs2Label=ConfidenceLevel cs3={0} \
cs3Label=Description"

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
