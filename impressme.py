#!/usr/bin/env python
#
# Copyright 2013 Chris Packham
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
from argparse import ArgumentParser
from xml.dom.minidom import parse

from html import *
from layout.radial import Radial
from layout.flat import Flat

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType in [node.TEXT_NODE, node.CDATA_SECTION_NODE]:
            rc.append(node.data)
        else:
            rc.append(node.toxml())
    return ''.join(rc)

def generate_slides(file_, cls, stylesheet, out=sys.stdout):
    try:
        doc = parse(file_)
    except IOError as e:
        print >>sys.stderr, "error: %s" % str(e)

    presentation = HTML()
    head = Head()
    head.add('<meta name="viewport" content="width=1024" />')
    head.add('<link href="%s" rel="stylesheet" />' % stylesheet)
    presentation.add(head)
    body = Body({'class':'impress-not-supported'})
    presentation.add(body)
    fb_div = Div({'class':'fallback-message'})
    fb_div.add("""<p>Your browser <b>doesn\'t support the features
        required</b> by impress.js, so you are presented with a simplified
        version of this presentation.</p>""")
    body.add(fb_div)
    impress_div = Div({'id':'impress'})
    body.add(impress_div)
    body.add('<!-- load up impress.js -->')
    body.add('<script src="impress/js/impress.js"></script>')
    body.add('<script>impress().init();</script>')

    sections = doc.getElementsByTagName("section")
    layout = cls(len(sections))

    # Title page
    try:
        title = doc.getElementsByTagName("title")[0]
        attr = {'class':'step'}
        attr.update(layout.title_loc())
        div = Div(attr)
        div.add(getText(title.childNodes))
        impress_div.add(div)
    except IndexError:
        pass

    # Slides
    i = 1
    for section in sections:
        j=1
        for slide in section.getElementsByTagName("slide"):
            attr = {'class':'step'}
            attr.update(layout.slide_loc(i,j))
            div = Div(attr)
            div.add(getText(slide.childNodes))
            impress_div.add(div)
            j += 1
        i += 1

    # Overview
    attr = {'class':'step'}
    attr.update(layout.overview_loc())
    div = Div(attr)
    impress_div.add(div)

    # Summary
    try :
        summary = doc.getElementsByTagName("summary")[0]
        attr = {'class':'step'}
        attr.update(layout.summary_loc())
        div = Div(attr)
        div.add(getText(summary.childNodes))
        impress_div.add(div)
    except IndexError:
        pass

    out.write(str(presentation))


if __name__ == "__main__":
    parser = ArgumentParser(
            description="Generate a presentation using impress.js")
    parser.add_argument('--stylesheet', type=str, metavar="CSS",
            default="impress/css/impress-demo.css",
            help="use a different CSS stylesheet")
    parser.add_argument('--layout', type=str,
            choices=['radial','flat'], default='flat',
            help="layout for presentation")
    parser.add_argument('file', type=file, metavar='FILE',
            help="XML file to process")

    try:
        args = parser.parse_args()
    except IOError as e:
        print >>sys.stderr, str(e)
        sys.exit(-1)

    for cls in [Radial, Flat]:
        if cls.__name__.lower() == args.layout:
            break

    generate_slides(args.file, cls, args.stylesheet)
