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

class Element(object):
    def __init__(self, name, attrs = {}):
        self.name = name
        self.attrs = attrs
        self.content = []

    def __str__(self):
        attr = "".join([" %s=\"%s\""%(k,v) for k,v in self.attrs.iteritems()])
        content = "\n".join(map(str,self.content))
        return "<%s%s>\n%s\n</%s>\n" % (self.name, attr, content, self.name)

    def add(self, elem):
        self.content.append(elem)

class HTML(Element):
    def __init__(self):
        super(HTML,self).__init__("html")

    def __str__(self):
        return """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd">
""" + super(HTML,self).__str__()

class Head(Element):
    def __init__(self):
        super(Head,self).__init__("head")

class Title(Element):
    def __init__(self):
        super(Title,self).__init__("title")

class Body(Element):
    def __init__(self, attrs={}):
        super(Body,self).__init__("body", attrs)

class Div(Element):
    def __init__(self, attrs={}):
        super(Div,self).__init__("div", attrs)

class Para(Element):
    def __init__(self, attrs={}):
        super(Para,self).__init__("p", attrs)

#                                Unit tests                                  #
# -------------------------------------------------------------------------- #
import unittest

class Test(unittest.TestCase):
    def test_HTML(self):
        expected = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd">
<html>

</html>
"""
        actual = str(HTML())
        self.assertEqual(expected, actual)

    def test_Head(self):
        expected = "<head>\n\n</head>\n"
        actual = str(Head())
        self.assertEqual(expected, actual)

    def test_Title(self):
        expected = "<title>\n\n</title>\n"
        actual = str(Title())
        self.assertEqual(expected, actual)

    def test_Body(self):
        expected = "<body>\n\n</body>\n"
        actual = str(Body())
        self.assertEqual(expected, actual)

    def test_Div(self):
        expected = "<div>\n\n</div>\n"
        actual = str(Div())
        self.assertEqual(expected, actual)

    def test_Para(self):
        expected = "<p>\n\n</p>\n"
        actual = str(Para())
        self.assertEqual(expected, actual)

    def test_Div_with_attrs(self):
        expected = '<div class="foo" id="bar">\n\n</div>\n'
        actual = str(Div({"class":"foo","id":"bar"}))
        self.assertEqual(expected, actual)

    def test_Html_document(self):
        expected = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>
This is a test
</title>

</head>

<body>
<div class="test">
<p>
This is a test
</p>

</div>

</body>

</html>
"""
        html = HTML()
        head = Head()
        title = Title()
        title.add("This is a test")
        body = Body()
        div = Div({"class":"test"})
        p = Para()
        p.add("This is a test")
        html.add(head)
        head.add(title)
        html.add(body)
        body.add(div)
        div.add(p)
        actual = str(html)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
