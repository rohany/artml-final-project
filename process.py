import argparse
import sys
import numpy as np
import cv2 as cv
import os

# from matplotlib import pyplot as plt

# code adapted from article -- http://creativemorphometrics.co.vu/blog/2014/08/05/automated-outlines-with-opencv-in-python/

def getContours(f, indir, outpath):
    filename = os.path.join(indir, f)
    img = cv.imread(filename)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # ret, thresh1 = cv.threshold(img, 10, 255, cv.THRESH_BINARY)
    thresh1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY, 11, 2)
    kernel = np.ones((2,2), np.uint8)
    erosion = cv.erode(thresh1, kernel, iterations=1)
    opening = cv.morphologyEx(erosion, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
    contours, _ = cv.findContours(closing, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(closing, contours, -1, (255, 255, 255), 4)
    out = os.path.join(outpath, f)
    cv.imwrite(out, closing)

def getBlackWhite(f, indir, outpath):
   filename = os.path.join(indir, f)
   img = cv.imread(filename)
   img = cv.cvtColor(img.cv.COLOR_BGR2GRAY)
   out = os.path.join(outpath, f)
   cv.imwrite(out, img)

def resize(f, indir, outpath):
    filename = os.path.join(indir, f)
    img = cv.imread(filename)
    resized = cv.resize(img, (512,512))
    out = os.path.join(outpath, f)
    cv.imwrite(out, resized)

folder = sys.argv[1]
outdir = sys.argv[2]
op = sys.argv[3]

if not os.path.exists(outdir):
    os.mkdir(outdir)

for filename in os.listdir(folder):
    if op == 'contour':
        getContours(filename, folder, outdir)
    elif op == 'blackandwhite':
        getBlackWhite(filename, folder, outdir)
    else:
	resize(filename, folder, outdir)
