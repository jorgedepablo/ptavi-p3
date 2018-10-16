#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve


class KaraokeLocal():

    def __init__(self, fichsmil):
        parser = make_parser()
        SmilHandler = SmallSMILHandler()
        parser.setContentHandler(SmilHandler)
        parser.parse(open(fichsmil))
        self.elements = SmilHandler.get_tags()

    def __str__(self):
        for tags in self.elements:
            attrs_list = []
            for tag in tags:
                if tag != 'Tag' and tags[tag] !='':
                    attrs_list += ('\t', tag, '=', '"', tags[tag], '"')
            print(tags['Tag'], "".join(attrs_list))

    def to_json(self, fichsmil, fichjson):
        if fichjson == '':
            fichjson = fichsmil.split('.')[0] + '.json'
        json.dump(self.elements, open(fichjson, 'w'), separators=(',', ':'), indent=4)

    def do_local(self):
        for tags in self.elements:
            for tag in tags:
                if tag == 'src' and tags[tag].startswith('http://'):
                    location = tags[tag].split('/')[-1]
                    urlretrieve(tags[tag], location)
                    tags[tag] = location


if __name__ == "__main__":
    try:
        fichsmil = (sys.argv[1])
    except ValueError or IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    karaoke = KaraokeLocal(fichsmil)
    karaoke.__str__()
    karaoke.to_json(fichsmil, '')
    karaoke.do_local()
    karaoke.to_json(fichsmil, 'local.json')
    karaoke.__str__()
