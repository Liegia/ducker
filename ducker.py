#!/usr/bin/env python3

"""
small script to search with duckduckgo
created 2020-07-30
k.heidenborg.se
"""

# Use chmod +x ducker.py
# Then cp ducker.py /bin/ducker

# Usage: ducker search-string

import webbrowser
import sys
import argparse

parser = argparse.ArgumentParser('open a website')
parser.add_argument("url", type=str, help="type webaddress")
user_input = ' '.join(sys.argv[1:])
webbrowser.open_new_tab("www.duckduckgo.com/" + user_input)

#print('Opening ' + user_input)
