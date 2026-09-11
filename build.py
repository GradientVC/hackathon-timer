#!/usr/bin/env python3
"""Wrap timer.html (the artifact source, no document skeleton) into a standalone index.html
that opens from disk or any static host. Run after editing timer.html."""
import pathlib
here = pathlib.Path(__file__).parent
src = (here / "timer.html").read_text()
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
       '<meta name="theme-color" content="#11191F">\n</head>\n<body>\n' + src + '\n</body>\n</html>\n')
(here / "index.html").write_text(out)
print("wrote index.html", len(out), "bytes")
