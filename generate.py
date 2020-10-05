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
POSTS = {}
for i in os.listdir("posts"):
    POSTS[i] = os.listdir("posts/%s" % i)

# Template header for all files
header = """<!DOCTYPE html>
<html>
    <head>
        <meta property="og:title" content="Hanprogramer's Website" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="http://hanprogramer.github.io" />
        <meta property="og:image" content="https://hanprogramer.github.io/banner.png" />
        <meta property="og:description" content="Come check out my stuffs :3" />
        <meta name="theme-color" content="#FF0000">

        <!-- Include this to make the og:image larger -->
        <meta name="twitter:card" content="summary_large_image">
        
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

        <div style="margin-bottom: 56px"></div>
        <div class="maindivider" style="position: relative">
        <div class="content">"""
header_root = """<!DOCTYPE html>
<html>
    <head>
        <meta property="og:title" content="Hanprogramer's Website" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="http://hanprogramer.github.io" />
        <meta property="og:image" content="https://hanprogramer.github.io/banner.png" />
        <meta property="og:description" content="Come check out my stuffs :3" />
        <meta name="theme-color" content="#FF0000">

        <!-- Include this to make the og:image larger -->
        <meta name="twitter:card" content="summary_large_image">

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
        <div style="margin-bottom: 56px"></div>
        
        <div class="maindivider" style="position: relative">
        <div class="content">
        %s
        <div class="post-container">"""
footer = """<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <!-- github.io -->
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-9638544368327690"
             data-ad-slot="9490828740"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
        
                <div class="tweets">
                        <a class="twitter-timeline" data-height="512" data-dnt="true" data-theme="dark" href="https://twitter.com/Hanprogramer123?ref_src=twsrc%5Etfw">Tweets by Hanprogramer123</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                </div></div></div>
    </body>
</html>"""
f = open("index.html", "w")
# Generator
for line in content:
    raw = line.strip()
    if(raw == "<div class=\"GENERATED\"></div>"):
        for key in POSTS.keys():
            #########################################
            #      POSTS CONTENT GENERATOR
            #########################################
            f.write("<h1>%s</h1>" % key.title())
            f.write('<div class="post-container">')
            f_category = open("%s.html" % key, "w")
            f_category.write(header_root % ("<h1>%s</h1>" % key.title()))
            for post in POSTS[key]:
                if(not os.path.exists("posts/%s/%s/post.md" % (key,post))):
                    continue
                # Genereate the posts
                template = """
                            <a class="post" href="posts/%s/%s/post.html">
                                <img src="posts/%s/%s/thumb.png">
                            </a>\n""" % (key, post, key, post)
                f.write(template)
                f_category.write(template)

                # Generate the individual post html
                html = header
                html += (markdown2.markdown_path("posts/%s/%s/post.md" %(key, post)))
                html += footer

                f_post = open("posts/%s/%s/post.html" % (key,post), "w")
                f_post.write(html)
                f_post.close()
            f.write('</div>')
            f_category.write(footer)
            f_category.close()
        continue
    f.write(line)
f.close()