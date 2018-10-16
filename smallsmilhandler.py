#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.tags = ['root-layout', 'region', 'img', 'audio', 'textstream']
        self.dicAttrs = {'root-layout': ['width', 'height',
                                'background-color'],
                                'region': ['id', 'top', 'left'],
                                'img': ['src', 'region', 'begin', 'dur'],
                                'audio': ['src', 'begin', 'dur'],
                                'textstream': ['src', 'begin']}
        self.tagsList = []

    def startElement(self, name, attrs):
        if name in self.tags:
            dicAttrs = {}
            dicAttrs["Tag"] = name
            for atribute in self.dicAttrs[name]:
                dicAttrs[atribute] = attrs.get(atribute, "")
            self.tagsList.append(dicAttrs)

    def get_tags(self):
        return self.tagsList


if __name__ == "__main__":
    parser = make_parser()
    SmilHandler = SmallSMILHandler()
    parser.setContentHandler(SmilHandler)
    parser.parse(open('karaoke.smil'))
