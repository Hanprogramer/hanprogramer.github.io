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

# Template header for all files
header = """<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&display=swap" rel="stylesheet">
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
            <div class="titletext">
                <a href="../../../index.html">HANPROGRAMER</a>
                <!-- <a href="https://youtube.com/Hanprogramer" target="_blank" class="subtitle">youtube.com/Hanprogramer</a> -->
            </div>
            <div style="flex-grow: 1"></div>
            <button class="button" onclick="window.location = '../../../tools.html'">Tools</a>
            <button class="button" onclick="window.location = '../../../addons.html'">Addons</a>
        </div>

        <div class="content">"""
header_root = """<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="index.css">
        <!-- <link rel="stylesheet" href="nav.css"> -->
        <link rel="icon" type="image/png" href="logo.png">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
        <script data-ad-client="ca-pub-9638544368327690" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <title>Hanprogramer</title>
    </head>
    <body>
        <script>
            CSS.paintWorklet.addModule('bubblePaint.js')
        </script>
        <div class="navbar">
            <img class="round-icon" src="favicon.ico">
            <div class="titletext">
                <a href="index.html">HANPROGRAMER</a>
                <!-- <a href="https://youtube.com/Hanprogramer" target="_blank" class="subtitle">youtube.com/Hanprogramer</a> -->
            </div>
            <div style="flex-grow: 1"></div>
            <button class="button" onclick="window.location = './tools.html'">Tools</a>
            <button class="button" onclick="window.location = './addons.html'">Addons</a>
        </div>
        <div class="content">
        %s
        <div class="post-container">"""
footer = """        </div>
    </body>
</html>"""
f = open("index.html", "w")
for line in content:
    raw = line.strip()
    if(raw == "<div class=\"GENERATED\"></div>"):
        #########################################
        #      TOOLS CONTENT GENERATOR
        #########################################
        f.write("<h1>Tools</h1>")
        f.write('<div class="post-container">')
        f_tool = open("tools.html", "w")
        f_tool.write(header_root % ("<h1>Tools</h1>"))
        for tool in TOOLS:
            if(not os.path.exists("posts/tools/%s/post.md" % tool)):
                continue
            # Genereate the posts
            template = """
                        <a class="post" href="posts/tools/%s/post.html">
                            <img src="posts/tools/%s/thumb.png">
                        </a>\n""" % (tool, tool)
            f.write(template)
            f_tool.write(template)

            # Generate the individual post html
            html = header
            html += (markdown2.markdown_path("posts/tools/%s/post.md" % tool))
            html += footer

            post = open("posts/tools/%s/post.html" % tool, "w")
            post.write(html)
            post.close()
        f.write('</div>')
        f_tool.write(footer)
        f_tool.close()
        
        #########################################
        #      ADDONS CONTENT GENERATOR
        #########################################
        f.write("<h1>Addons</h1>")
        f.write('<div class="post-container">')
        f_tool = open("addons.html", "w")
        f_tool.write(header_root % ("<h1>Addons</h1>"))
        for tool in ADDONS:
            if(not os.path.exists("posts/addons/%s/post.md" % tool)):
                continue
            # Genereate the posts
            template = """
                        <a class="post" href="posts/addons/%s/post.html">
                            <img src="posts/addons/%s/thumb.png">
                        </a>\n""" % (tool, tool)
            f.write(template)
            f_tool.write(template)

            # Generate the individual post html
            html = header
            html += (markdown2.markdown_path("posts/addons/%s/post.md" % tool))
            html += footer

            post = open("posts/addons/%s/post.html" % tool, "w")
            post.write(html)
            post.close()
        f.write('</div>')
        f_tool.write(footer)
        f_tool.close()
        continue
    f.write(line)
f.close()