# -*- coding: utf-8 -*-
"""Download final photo set, apply a consistent brand grade, export to assets/img/photo."""
import json
import os
import urllib.request

from PIL import Image, ImageEnhance, ImageOps

ROOT = r"D:\Users\Song\Documents\deepseek-harness\default-workspace\xingzhou-site"
RAW = os.path.join(ROOT, "tools", "_raw")
OUT = os.path.join(ROOT, "assets", "img", "photo")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36", "Referer": "https://commons.wikimedia.org/"}
BURST_UA = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")}

# (output name, source url, target width, header)
ITEMS = [
    ("hero-guizhou", "https://upload.wikimedia.org/wikipedia/commons/9/9b/Landscape_Scenery_in_Liupanshui%2C_Guizhou%2C_China.jpg", 2400, UA),
    ("port", "https://upload.wikimedia.org/wikipedia/commons/7/7d/Port_Jersey_container_ship_sunset_2018.jpg", 2400, UA),
    ("lab", "https://burst.shopifycdn.com/photos/female-scientist-at-work-in-lab.jpg?width=2000", 2000, BURST_UA),
    ("qc", "https://burst.shopifycdn.com/photos/scientist-at-work.jpg?width=2000", 2000, BURST_UA),
    ("plant", "https://burst.shopifycdn.com/photos/an-industrial-complex-underneath-a-grey-sky.jpg?width=2000", 2000, BURST_UA),
]


def fetch(url, path, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as f:
        f.write(r.read())


def grade(im, sat=0.70, contrast=1.07, duo_blend=0.22):
    im = im.convert("RGB")
    im = ImageEnhance.Color(im).enhance(sat)
    im = ImageEnhance.Contrast(im).enhance(contrast)
    lum = im.convert("L")
    duo = ImageOps.colorize(lum, black=(12, 30, 32), white=(247, 243, 236))
    return Image.blend(im, duo, duo_blend)


if __name__ == "__main__":
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    for name, url, w, hdr in ITEMS:
        raw = os.path.join(RAW, name + ".jpg")
        try:
            if not os.path.exists(raw):
                fetch(url, raw, hdr)
            im = Image.open(raw)
            if im.width > w:
                im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            out = grade(im)
            out.save(os.path.join(OUT, name + ".jpg"), quality=84, optimize=True, progressive=True)
            print(name, im.size, os.path.getsize(os.path.join(OUT, name + ".jpg")))
        except Exception as e:
            print("FAIL", name, e)
