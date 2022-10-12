from PIL import Image
from glob import glob
from os import mkdir
from os import rename
from os.path import exists
from os.path import isfile
from os.path import isdir
from os.path import basename

multi = False
bulk = []

location = input("Please enter folder or file name:\n")
if (exists(location) and isdir(location)):
    bulk = glob(location + "/*.webp")
    mkdir(location + "\png")
    multi = True
elif (exists(location) and isfile(location)):
    if (basename(location).split(".")[-1].lower() == "webp"):
        webp = location
        if (basename(webp).split(".")[-1] != "webp"):
            webp_new = "".join(webp.split('.')[:-1]) + ".webp"
            rename(webp, webp_new)
            wepb = webp_new
        file = Image.open(webp)
    else:
        print("Error: Invalid file format.")
else:
    print("Error: Invalid or empty input.")
    exit(0)

if (multi):
    for webp in bulk:
        file = Image.open(webp)
        png = location + "\png\\" + basename(webp).replace(".webp", ".png")
        file.save(png, format="png", lossless=True)
else:
    png = webp.replace(".webp", ".png")
    file.save(png, format="png", lossless=True)
print("Finished.")