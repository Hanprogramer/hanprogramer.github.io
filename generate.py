# Generator for my website hanprogramer.github.io
import os
import glob
import sys
import markdown2

# Reads the template file
f = open("index.template.html", "r")
content = f.readlines()
f.close()

# List all available posts
TOOLS = os.listdir("posts/tools")
ADDONS = os.listdir("posts/addons")

f = open("index.html", "w")
for line in content:
    raw = line.strip()
    if(raw == "<div class=\"GENERATED\"></div>"):
        for tool in TOOLS:
            if(not os.path.exists("posts/tools/%s/post.md" % tool)):
                continue
            # Genereate the posts
            template = """
                        <a class="post" href="posts/tools/%s/post.html">
                            <img src="posts/tools/%s/thumb.png">
                        </a>\n""" % (tool, tool)
            f.write(template)

            # Generate the individual post html
            html = """<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="../../../index.css">
        <!-- <link rel="stylesheet" href="../../../nav.css"> -->
        <link rel="icon" type="image/png" href="../../../logo.png">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
        <script data-ad-client="ca-pub-9638544368327690" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <title>Hanprogramer</title>
    </head>
    <body>
        <script>
            CSS.paintWorklet.addModule('../../../bubblePaint.js')
        </script>
        <div class="navbar">
            <img class="round-icon" src="../../../favicon.ico">
            <div class="titletext" href="https://youtube.com/Hanprogramer" target="_blank">
                <a>Hanprogramer</a>
                <a href="https://youtube.com/Hanprogramer" target="_blank" class="subtitle">youtube.com/Hanprogramer</a>
            </div>
            <div style="flex-grow: 1"></div>
            <button>Tools</button>
            <button>Addons</button>
        </div>

        <div class="content">"""
            html += (markdown2.markdown_path("posts/tools/%s/post.md" % tool))
            html += """        </div>
    </body>
</html>"""
            post = open("posts/tools/%s/post.html" % tool, "w")
            post.write(html)
            post.close()
        continue
    f.write(line)
f.close()