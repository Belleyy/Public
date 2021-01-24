import json
import os
import sys
import base64
import sqlite3
import shutil



path = 'E:\Programmation\Python\imagescenes'
pathJson = 'D:\Stash\metadata\scenes'
pathScreen = 'D:\Stash\Preview\screenshots'
print("Path : ", path)

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

with os.scandir(path) as it:
    for entry in it:  # Found Files
        if entry.name.endswith("upscale.jpg"):
            base64pic = get_base64_encoded_image(entry.path)
            shutil.copy2(entry.path, 'G:/Stash/Preview/screenshots/' + entry.name.replace("-upscale",""))
            jsonfile = pathJson + "\\" + entry.name.replace("-upscale.jpg",".json")
            with open(jsonfile, "r+", encoding="utf8") as f:  # Read/Write Files
                print("Fichier : ",jsonfile)
                try:
                    jsondata = json.load(f)
                    jsondata_images = jsondata['cover']
                    jsondata['cover'] = base64pic
                    f.seek(0)
                    json.dump(jsondata, f, indent=4)
                    f.truncate()
                    continue
                except KeyError:
                    print("Fichier : ",entry.path)
                    print("Ne contient pas de cover ???")
                    continue
sys.exit()

