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

header = """
<!doctype html>

<html>
    <head>
        <meta name="viewport" content="width=1024" />
        <link href="impress/css/impress-demo.css" rel="stylesheet" />
    </head>

    <body class="impress-not-supported">

        <div class="fallback-message">
            <p>Your browser <b>doesn\'t support the features required</b> by
            impress.js, so you are presented with a simplified version of this
            presentation.</p>
        </div>

        <div id="impress">
"""
footer="""
        </div>

    </div>

    <!-- load up impress.js -->
    <script src="impress/js/impress.js"></script>
    <script>impress().init();</script>
</body>
</html>
"""

title_tmpl = '<div class="step" data-x="%(x)d" data-y="%(y)d">'
slide_tmpl = '<div class="step" data-x="%(x)d" data-y="%(y)d" data-rotate="%(r).1f">'
overview_tmpl = '<div id="overview" class="step" data-scale="5" data-x="%(x)d" data-y="%(y)d" data-rotate="%(r).1f">'
summary_tmpl = '<div class="step" data-x="%(x)d" data-y="%(y)d" data-z="%(z)d" data-rotate="%(r).1f", data-rotate-x="%(rx)d">'
