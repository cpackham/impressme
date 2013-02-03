#!/usr/bin/env python
import sys
from argparse import ArgumentParser
from xml.dom.minidom import parse

from templates import *
from layout.radial import Radial

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        else:
            rc.append(node.toxml())
    return ''.join(rc)

def generate_slides(file_, layout, out=sys.stdout):
    try:
        doc = parse(file_)
    except IOError as e:
        print >>sys.stderr, "error: %s" % str(e)

    sections = doc.getElementsByTagName("section")
    l = layout(len(sections))

    out.write(header)

    # Title page
    try:
        title = doc.getElementsByTagName("title")[0]
        x,y,r = l.title_loc()
        out.write(title_tmpl % {'x':x, 'y':y})
        out.write(getText(title.childNodes))
        out.write('\n</div>\n')
    except IndexError:
        pass

    # Slides
    i = 1
    for section in sections:
        j=1
        for slide in section.getElementsByTagName("slide"):
            x,y,r = l.slide_loc(i,j)
            out.write(slide_tmpl % {'x':x, 'y':y, 'r':r})
            out.write(getText(slide.childNodes))
            out.write('\n</div>\n')
            j += 1
        i += 1

    # Summary
    try :
        summary = doc.getElementsByTagName("summary")[0]
        x,y,z,rx = l.summary_loc()
        out.write(title_tmpl % {'x':x, 'y':y})
        out.write(getText(summary.childNodes))
        out.write('\n</div>\n')
    except IndexError:
        pass

    out.write(footer)


if __name__ == "__main__":
    parser = ArgumentParser(
            description="Generate a presentation using impress.js")
    parser.add_argument('file', type=file, metavar='FILE')
    
    args = parser.parse_args()
    generate_slides(args.file, Radial)
