from  PIL import Image
import os
import zipfile
import shutil
import cv2
from pathlib import Path
import image_util as imgutil


IMAGE_EXT = [
    'png',
    'jpeg',
    'jpg'
]

class Converter():
    def __init__(self, target_width, target_height, only_shrink):
        self.target_width = target_width
        self.target_height = target_height
        self.only_shrink = only_shrink


    def convert_all(self, src_dir, dest_dir):
        for file_name in os.listdir(src_dir):
            if file_name[-4:] != '.zip':
                continue

            fp = src_dir + '/' + file_name
            with zipfile.ZipFile(fp, 'r') as inputFile:
                for info in inputFile.infolist():
                    if info.is_dir():
                        self.convert_all_in_dir(info.filename, os.path.join(dest_dir, info.filename))
                    else:
                        _, ext = os.path.splitext(info.filename)
                        if ext in IMAGE_EXT:
                            img = Image.open(os.path.join())
                            imgutil.resize()


    def convert_all_in_dir(self, src_dir, dest_dir):
        for f in os.listdir(src_dir):
            _, ext = os.path.splitext(info.filename)
            if ext in IMAGE_EXT:
                img = resize(os.path.join(src_dir, info.filename))
                img.save(os.path.join(dest_dir, info.filename))


    def resize(path):
        img = Image.open(path)
        return imgutil.resize(img, self.target_width, self.target_height, 'INSCRIBE', true)


