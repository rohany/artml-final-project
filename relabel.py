import sys
import os
import shutil

folder = sys.argv[1]
outdir = sys.argv[2]

if not os.path.exists(outdir):
  os.makedirs(outdir)

for i, f in enumerate(os.listdir(folder)):
  shutil.copy2(os.path.join(folder, f), os.path.join(outdir, "image-" + str(i) + ".jpg"))
