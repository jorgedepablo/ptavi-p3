#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler



if __name__ == "__main__":
    try:
        fichsmil = (sys.argv[1])
        ext = fichsmil.split('.')
    except ValueError or IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    parser = make_parser()
    SmilHandler = SmallSMILHandler()
    parser.setContentHandler(SmilHandler)
    parser.parse(open(fichsmil))
    print(SmilHandler.get_tags())
