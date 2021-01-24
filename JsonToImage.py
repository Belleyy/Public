import json
import os
import sys
import base64
from PIL import Image


path = 'D:\Stash\metadata\scenes'
# D:\Stash\metadata\performers D:\Stash\metadata\scenes
# sys.exit()
print("Path : ", path)

#"""
with os.scandir(path) as it:
    for entry in it:  # Found Files
        if entry.name.endswith(".json"):  # Il s'agit d'un .JSON
            with open(entry.path, "r+", encoding="utf8") as f:  # Read/Write Files
                try:
                    jsondata = json.load(f)
                    jsondata_tags = jsondata['tags']
                    jsondata_images = jsondata['cover']
                    jsondata_hash = jsondata['checksum']  # checksum / oshash
                    # if "1. Anime" in jsondata_tags:
                    #print("Extration de l'image...")
                    image = open("imagescenes\\" +
                                 jsondata_hash + ".jpg", "wb")
                    image.write(base64.b64decode(jsondata_images))
                    image.close()
                    im = Image.open("imagescenes\\" + jsondata_hash + ".jpg")
                    w, h = im.size
                    im.close()
                    if h > 700:
                        os.remove("imagescenes\\" + jsondata_hash + ".jpg")
                    else:
                        print("Fichier : ", entry.path)
                    # os.system("pause")
                    #    continue
                    # else:
                    #    continue
                except KeyError:
                    # print("Fichier : ",entry.path)
                    # print("Ne contient pas de cover")
                    continue
sys.exit()
"""
path = 'D:\Stash\metadata\performers'
# D:\Stash\metadata\performers D:\Stash\metadata\scenes
# sys.exit()
print("Path : ", path)

with os.scandir(path) as it:
    for entry in it:  # Found Files
        if entry.name.endswith(".json"):  # Il s'agit d'un .JSON
            with open(entry.path, "r+", encoding="utf8") as f:  # Read/Write Files
                try:
                    print("Fichier : ", entry.path)
                    jsondata = json.load(f)
                    jsondata_images = jsondata['image']
                    jsondata_hash = entry.name.replace(".json","")
                    image = open("imagescenes\\" + jsondata_hash + ".jpeg", "wb")
                    image.write(base64.b64decode(jsondata_images))
                    image.close()
                except KeyError:
                    # print("Fichier : ",entry.path)
                    # print("Ne contient pas de cover")
                    continue
sys.exit()
"""
