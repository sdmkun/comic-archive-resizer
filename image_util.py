from  PIL import Image
import os
import shutil
import cv2
from pathlib import Path

RESIZE_METHOD = {
    INSCRIBE: 'INSCRIBE'  # 内接
}

def resize(image: Image, target_width, target_height, resize_method, only_shrink=true):
    if resize_method == RESIZE_METHOD.INSCRIBE:
        dest_width, dest_height = get_rect_inscribe(image.width, image.height, target_width, target_height, only_shrink)
        return image.resize((dest_width, dest_height))
    return image

# 内接するサイズを返す
def get_rect_inscribe(width, height, target_width, target_height, only_shrink=true):
    # if width == 0 or height == 0 or target_width == 0 or target_height == 0:
    #    return 0, 0

    if only_shrink and
    width < target_width and
    height < target_height:
        return width, height

    factor = min(target_width / width, target_height / height)
    return width * factor, height * factor





class IMG():
    def __init__(self,dic):
        """初期化時には画像を置いてるディレクトリのパスをいれる"""
        self.directory=dic

    def convert(self,suffix):
        """拡張子を任意の拡張子に変更するメソッド
        引数には.(ドット)を除いた拡張子をいれる"""
        for i in os.listdir(self.directory):
            fp = self.directory + '/' + i
            img=cv2.imread(fp)
            file_Path=Path(fp)
            cv2.imwrite(self.directory + '/' +file_Path.stem + '.' + suffix,img)
            if file_Path.suffix != '.jpg':
                os.remove(fp)
        return self


    def rename(self,new_file):
        """ファイル名を任意をファイル名に変更するメソッド
        引数には変更したいファイル名をいれる"""
        data=os.listdir(self.directory)
        for i, old_name in enumerate(data):
            path = self.directory + '/' + old_name
            # ファイル名の決定
            new_name = new_file + "_{0:03d}.jpg".format(i + 1)
            new_path= self.directory + '/' +new_name
            # ファイル名の変更
            os.rename(path, new_path)
        return self

    def resize(self,width,height):
        """ファイルサイズを任意のサイズに変更するメソッド
        引数には幅、高さをいれる"""
        for i in os.listdir(self.directory):
            path= self.directory + '/' + i
            img = cv2.imread(path)
            img_resize = cv2.resize(img,(width, height))
            cv2.imwrite(path,img_resize)
        return self

    def make_zip(self,zip_name):
        """ディレクトリの画像をzip化するメソッド
        引数には作成するzipファイル名をいれる"""
        shutil.make_archive(zip_name, 'zip', root_dir = self.directory)
