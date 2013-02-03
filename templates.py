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
