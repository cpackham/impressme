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

class Flat:
    """
    Layout slides in a Flat fashion.

    Slide sections are distributed vertically, slides within a section
    horizontally.
    """

    def __init__(self, sections=6, dist=1000):
        self.dist = dist
        self.sections = sections

    def title_loc(self):
        """title located in the center, no rotation"""
        return {'data-x':'0',
            'data-y':'0',
            'data-z':'0'};

    def overview_loc(self):
        return {'data-x':'0',
            'data-y':'%d' % ((self.dist*self.sections)/2),
            'data-z':'0',
            'data-scale':'5'}

    def summary_loc(self):
        """summary located at the bottom, rotated 90 degrees around the x
        axis"""
        return {'data-x':'0',
            'data-y':'%d' % (self.dist*self.sections),
            'data-z':'-1000',
            'data-rotate-x':'-90',
            'data-scale':'5'}

    def slide_loc(self, section, slide):
        return {'data-x':'%d' % ((slide-1) * self.dist),
            'data-y':'%d' % (section * self.dist),
            'data-z':'0'}
