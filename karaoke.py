#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


def printElements(dicElements):
    for tags in dicElements:
        attrs_list = []
        for tag in tags:
            if tag != 'Tag' and tags[tag] !='':
                attrs_list += ('\t', tag, '=', '"', tags[tag], '"')
        print(tags['Tag'], "".join(attrs_list))

def changeFormat(dicElements, fichsmil):
    fichjson = fichsmil.split('.')[0] + '.json'
    json.dump(dicElements, open(fichjson, 'w'), separators=(',', ':'), indent=4)

def dowloandElements(dicElements):
    for tags in dicElements:
        for tag in tags:
            if tag == 'src' and tags[tag].startswith('http://'):
                print(tags[tag])


if __name__ == "__main__":
    try:
        fichsmil = (sys.argv[1])
    except ValueError or IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    parser = make_parser()
    SmilHandler = SmallSMILHandler()
    parser.setContentHandler(SmilHandler)
    parser.parse(open(fichsmil))
    printElements(SmilHandler.get_tags())
    changeFormat(SmilHandler.get_tags(), fichsmil)
    dowloandElements(SmilHandler.get_tags())
