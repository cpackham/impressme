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

from templates import *
from layout.radial import Radial

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType in [node.TEXT_NODE, node.CDATA_SECTION_NODE]:
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
        x,y,z,r = l.title_loc()
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
            x,y,z,r = l.slide_loc(i,j)
            out.write(slide_tmpl % {'x':x, 'y':y, 'r':r})
            out.write(getText(slide.childNodes))
            out.write('\n</div>\n')
            j += 1
        i += 1

    # Overview
    x,y,z,r = l.overview_loc()
    out.write(overview_tmpl % {'x':x, 'y':y, 'r':r})
    out.write('\n</div>\n')

    # Summary
    try :
        summary = doc.getElementsByTagName("summary")[0]
        x,y,z,r,rx = l.summary_loc()
        out.write(summary_tmpl % {'x':x, 'y':y, 'z':z, 'r': r, 'rx': rx})
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
