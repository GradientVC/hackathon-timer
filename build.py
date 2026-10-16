#!/usr/bin/env python3
"""Wrap the artifact sources (no document skeleton) into standalone pages for disk or any static host.
timer.html -> index.html, stopwatch.html -> stopwatch/index.html. Run after editing either source."""
import pathlib
here = pathlib.Path(__file__).parent
PAGES = {"timer.html": "index.html", "stopwatch.html": "stopwatch/index.html"}
for src_name, out_name in PAGES.items():
    src = (here / src_name).read_text()
    out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
           '<meta name="theme-color" content="#11191F">\n</head>\n<body>\n' + src + '\n</body>\n</html>\n')
    dest = here / out_name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out)
    print("wrote", out_name, len(out), "bytes")
