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

from math import cos, sin, pi, degrees

# Handy constant. Number of radians in a full circle.
tau = 2 * pi

class Radial:
    """
    Layout slides in a radial fashion.

    The title slide is in the center. Sections are distributed around a circle
    with each slide in the section extending out from the edge of the circle. A
    summary slide is presented at the bottom of the circle.
    """

    def __init__(self, sections=6, radius=1000):
        self.angle = tau/sections
        self.radius = radius
        self.sections = sections

    def title_loc(self):
        """title located in the center, no rotation"""
        return (0, 0, 0, 0);

    def overview_loc(self):
       return (0, 0, 0, degrees(self.angle * self.sections))

    def summary_loc(self):
        """summary located at the bottom, rotated 90 degrees around the x
        axis"""
        return (0, self.radius * 3, -1000,
                degrees(self.angle * self.sections), -90)

    def slide_loc(self, section, slide):
        angle = self.angle * section
        radius = self.radius * slide
        x = int(radius * cos(angle))
        y = int(radius * sin(angle))
        r = degrees(angle)

        return (x, y, 0, r)
