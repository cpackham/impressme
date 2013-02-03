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

    def title_loc(self):
        """title located in the center, no rotation"""
        return (0,0,0);

    def summary_loc(self):
        """summary located at the bottom, rotated 90 degrees around the x
        axis"""
        return (0, self.radius * 3, -self.radius, -90)

    def slide_loc(self, section, slide):
        angle = self.angle * section
        radius = self.radius * slide
        x = int(radius * cos(angle))
        y = int(radius * sin(angle))
        r = degrees(angle)

        return (x,y,r)
