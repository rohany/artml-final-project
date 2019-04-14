import sys
import urllib2
import urllib
# import dryscrape
from bs4 import BeautifulSoup as bs
import re
import os
from tqdm import tqdm

webpage = "https://www.spacetelescope.org/images"


def process_page(url):
  page = urllib2.urlopen(url)
  soup = bs(page, "html.parser")
  pattern = re.compile(r"https://cdn.spacetelescope.org/archives/images/.*/.*.jpg")
  return pattern.findall(soup.get_text())

def download(url, outname):
  newUrl = url.replace("thumb300y", "screen")
  urllib.urlretrieve(newUrl, outname)

build = []
for i in range(0, 10):
  url = webpage
  if i != 0:
    url = url + "/page/" + str(i) + "/"
  build += process_page(url)

for i, url in tqdm(enumerate(build)):
  download(url, os.path.join(sys.argv[1], "image-" + str(i) + ".jpg"))
