# -*- coding: utf-8 -*-
"""Product packaging renders for the Xingzhou site."""
import os
import sys
import math

sys.path.insert(0, r"D:\Users\Song\Documents\deepseek-harness\default-workspace\xingzhou-logo\src")
from render import Canvas, rrect_pts, rect_pts, xf  # noqa
import final as F
from final import TEAL, GOLD, INK, MUTED, WHITE, mark_a

OUT = r"D:\Users\Song\Documents\deepseek-harness\default-workspace\xingzhou-site\assets\img"
PAPER = (253, 250, 243)
AMBER = (176, 118, 52)
GREEN = (38, 94, 72)
SLATE = (36, 70, 92)
LINE = (222, 214, 198)


def carton(cv, x, y, w, h, dx=54, dy=40, band=TEAL, band_h=112, title="阿咖酚散",
           latin="A K FEN POWDER", spec="3 g × 20 袋", footer="解热镇痛类", mark_white=True,
           body=PAPER):
    cv.shadow(x, y, w, h, r=2, blur=14, alpha=44, dy=14)
    cv.poly([(x, y), (x + dx, y - dy), (x + w + dx, y - dy), (x + w, y)], (255, 255, 255))
    cv.poly([(x + w, y), (x + w + dx, y - dy), (x + w + dx, y + h - dy), (x + w, y + h)],
            (236, 232, 222))
    cv.poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], body)
    cv.poly([(x, y), (x + w, y), (x + w, y + band_h), (x, y + band_h)], band)
    # logo on band
    ms = 46
    mark_a(cv, x + 34 + ms / 2, y + 50, ms / 200.0, WHITE)
    cv.text_l(x + 92, y + 42, "星洲药业", "noto_serif", 26, WHITE, tracking=2.6, weight="Black")
    cv.text_l(x + 94, y + 72, "XINGZHOU PHARMA", "yahei", 8.4, (196, 220, 216), tracking=2.6)
    # title
    ty = y + band_h + 62
    n = max(1, len(title))
    ts = min(46.0, (w - 60) / (n + 0.065 * (n - 1)))
    cv.text_l(x + 26, ty, title, "noto_serif", ts, INK, tracking=ts * 0.065, weight="Black")
    cv.text_l(x + 28, ty + 34, latin, "yahei", 9, MUTED, tracking=3.4)
    cv.line([(x + 26, ty + 62), (x + w - 26, ty + 62)], (214, 186, 140), 1.4)
    cv.text_l(x + 26, ty + 86, spec, "yahei", 12, INK, tracking=0.8)
    cv.text_l(x + 26, ty + 108, footer, "yahei", 11, (110, 122, 114), tracking=0.8)
    # barcode
    yy = y + h - 66
    xp = x + 26
    widths = [1.4, 1.4, 2.6, 1.4, 3.6, 1.4, 1.4, 2.6, 1.4, 3.6, 1.4, 2.6, 1.4, 1.4, 3.6, 1.4]
    for i, wb in enumerate(widths):
        cv.line([(xp, yy), (xp, yy + 34)], INK, wb)
        xp += wb + (2.6 if i % 3 else 4.0)
    cv.text_l(x + 26, yy + 44, "6 901234 567890", "yahei", 7, MUTED, tracking=0.8)
    cv.text_r(x + w - 24, y + h - 22, "OTC", "yahei_b", 13, band, tracking=1.2)


def sachet(cv, x, y, w, h, band=TEAL, title="阿咖酚散", spec="3 g"):
    amp = 9
    pts = [(x + 8, y)]
    xx = x + 8
    up = True
    while xx < x + w - 8:
        pts.append((xx + amp / 2, y - amp if up else y))
        xx += amp
        up = not up
    pts += [(x + w - 8, y), (x + w, y + 10), (x + w, y + h - 10)]
    xx = x + w - 8
    up = True
    while xx > x + 8:
        pts.append((xx - amp / 2, y + h + amp if up else y + h))
        xx -= amp
        up = not up
    pts += [(x + 8, y + h), (x, y + h - 10), (x, y + 10)]
    cv.shadow(x, y, w, h, r=4, blur=10, alpha=38, dy=8)
    cv.poly(pts, PAPER)
    cv.poly([(x + 4, y + 12), (x + w - 4, y + 12), (x + w - 4, y + 62), (x + 4, y + 62)], band)
    mark_a(cv, x + w / 2, y + 34, 0.085, WHITE)
    cv.text_c(x + w / 2, y + 96, title, "noto_serif", 30, INK, tracking=2, weight="Black")
    cv.text_c(x + w / 2, y + 126, "解热镇痛", "yahei", 8, MUTED, tracking=2)
    cv.text_c(x + w / 2, y + h - 34, spec, "yahei_b", 11, band, tracking=1)


def bottle(cv, x, y, w, h, band=AMBER, title="维生素 C 片", spec="0.1 g × 100 片"):
    cv.shadow(x, y, w, h, r=26, blur=16, alpha=44, dy=16)
    # cap
    cv.rrect(x + w * 0.085, y + h * 0.035, w * 0.83, h * 0.145, 7, fill=(30, 62, 58))
    cv.rrect(x + w * 0.085 + 5, y + h * 0.035 + 5, w * 0.83 - 10, h * 0.145 - 10, 5, fill=(46, 86, 80))
    # body
    cv.rrect(x, y + h * 0.11, w, h * 0.89, 26, fill=(250, 247, 239))
    cv.rrect(x, y + h * 0.11, w, h * 0.89, 26, outline=(228, 220, 205), width=1)
    # label
    ly0 = y + h * 0.30
    ly1 = y + h * 0.80
    cv.poly([(x, ly0), (x + w, ly0), (x + w, ly1), (x, ly1)], (255, 255, 255))
    cv.poly([(x, ly0), (x + w, ly0), (x + w, ly0 + 10), (x, ly0 + 10)], band)
    cv.poly([(x, ly1 - 6), (x + w, ly1 - 6), (x + w, ly1), (x, ly1)], band)
    mark_a(cv, x + w / 2, ly0 + 44, 0.115, band)
    cv.text_c(x + w / 2, ly0 + 96, title, "noto_serif", 30, INK, tracking=2, weight="Black")
    cv.text_c(x + w / 2, ly0 + 124, "VITAMIN C  TABLETS", "yahei", 7.4, MUTED, tracking=2.4)
    cv.text_c(x + w / 2, ly0 + 156, spec, "yahei", 9.6, INK)
    cv.text_c(x + w / 2, ly0 + 178, "星洲药业", "noto_serif", 11, band, tracking=2, weight="Bold")



def blister(cv, x, y, w, h, band=TEAL):
    cv.shadow(x, y, w, h, r=8, blur=12, alpha=36, dy=10)
    cv.rrect(x, y, w, h, 8, fill=(228, 234, 231), outline=(206, 214, 210), width=1)
    cols, rows = 3, 5
    for r in range(rows):
        for c in range(cols):
            cx = x + 22 + c * (w - 44) / (cols - 1 or 1)
            cy = y + 22 + r * (h - 44) / (rows - 1 or 1)
            cv.ellipse(cx, cy, 15, fill=(255, 255, 255), outline=(200, 210, 206), width=1)
            cv.ellipse(cx, cy, 8, fill=(244, 247, 244))
    cv.text_c(x + w / 2, y + h - 12, "星洲药业", "noto_serif", 9, band, tracking=1.6, weight="Bold")


def render(name, fn):
    cv = Canvas(1000, 1000, ss=2)
    fn(cv)
    cv.save(os.path.join(OUT, name))
    print(name)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)

    def akafen(cv):
        sachet(cv, 692, 318, 132, 268, TEAL, "阿咖酚散", "3 g")
        carton(cv, 280, 282, 340, 440, 58, 42, TEAL, 112, "阿咖酚散",
               "A K FEN  POWDER", "3 g × 20 袋 / 盒", "解热镇痛类 · 复方散剂")
        sachet(cv, 148, 578, 132, 268, TEAL, "阿咖酚散", "3 g")

    def paracetamol(cv):
        blister(cv, 668, 330, 210, 330, SLATE)
        carton(cv, 250, 282, 340, 440, 58, 42, SLATE, 112, "对乙酰氨基酚片",
               "PARACETAMOL  TABLETS", "0.5 g × 20 片 / 盒", "解热镇痛类 · 片剂")

    def vitc(cv):
        bottle(cv, 370, 250, 260, 500, AMBER, "维生素 C 片", "0.1 g × 100 片")

    def glycyrrhiza(cv):
        blister(cv, 668, 340, 200, 320, GREEN)
        carton(cv, 250, 282, 340, 440, 58, 42, GREEN, 112, "复方甘草片",
               "COMPOUND  LIQUORICE", "100 片 / 瓶", "镇咳祛痰类 · 片剂")

    render("product-akafen.png", akafen)
    render("product-paracetamol.png", paracetamol)
    render("product-vitc.png", vitc)
    render("product-glycyrrhiza.png", glycyrrhiza)
