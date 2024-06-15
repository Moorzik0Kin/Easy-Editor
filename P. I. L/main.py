from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel,\
      QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
import os
from PIL import Image,ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
app=QApplication([])
win=QWidget()
win.resize(700,500)
win.setWindowTitle("Editor")

file=QPushButton("Папка")
N_List=QListWidget()

picture=QLabel("Зображення")

#||||||||||||||||||||||||||||||||||||
L_Pic=QPushButton("Вліво")
R_Pic=QPushButton("Вправо")
Rew_Pic=QPushButton("Розвернути")
Sharp_Pic=QPushButton("Різкість")
B_W_Pic=QPushButton("Чорно/Білий")
#||||||||||||||||||||||||||||||||||||

row=QHBoxLayout()
col_1=QVBoxLayout()
col_2=QVBoxLayout()
btn_col=QHBoxLayout()

btn_col.addWidget(L_Pic)
btn_col.addWidget(R_Pic)
btn_col.addWidget(Rew_Pic)
btn_col.addWidget(Sharp_Pic)
btn_col.addWidget(B_W_Pic)

col_1.addWidget(file)
col_1.addWidget(N_List)
col_2.addWidget(picture)
col_2.addLayout(btn_col)

row.addLayout(col_1, 7)
row.addLayout(col_2, 21)

win.setLayout(row)


def filter(files,extepsions):
    result=[]
    for f in files:
        for e in extepsions:
            if f.endswith(e):
                result.append(f)
    return result

dir=""

def showList():
    global dir
    extepsions=["png",".jpg",".webp",".gif",".bmp",".jpeg"]
    dir=QFileDialog.getExistingDirectory()
    files=filter(os.listdir(dir),extepsions)
    N_List.clear()
    N_List.addItems(files)
    
    
file.clicked.connect(showList)

class ImageProcessor():
    def __init__(self):
        self.image=None
        self.dir=None
        self.filename=None
        self.save_dir="Edited/"
    def load_image(self,dir,filename):
        self.dir=dir
        self.filename=filename
        path=os.path.join(dir,filename)
        self.image=Image.open(path)
    def show_image(self,path):
        picture.hide()
        image=QPixmap(path)
        w, h=picture.width(),picture.height()
        image=image.scaled(w, h, Qt.KeepAspectRatio)
        picture.setPixmap(image)
        picture.show()
    def save_image(self):
        path=os.path.join(dir,self.save_dir)
        if not os.path.exists(path) and not os.path.isdir(path):
            os.mkdir(path)
        fullname=os.path.join(path, self.filename)
        self.image.save(fullname)
    def left(self):
        self.image=self.image.transpose(Image.ROTATE_90)
        self.save_image()
        path=os.path.join(dir,self.save_dir,self.filename)
        self.show_image(path)
    def right(self):
        self.image=self.image.transpose(Image.ROTATE_270)
        self.save_image()
        path=os.path.join(dir,self.save_dir,self.filename)
        self.show_image(path)
    def nige(self):
        self.image=self.image.convert("L")
        self.save_image()
        path=os.path.join(dir,self.save_dir,self.filename)
        self.show_image(path)
    def rewerse(self):
        self.image=self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.save_image()
        path=os.path.join(dir,self.save_dir,self.filename)
        self.show_image(path)
    def sharpen(self):
        self.image=self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        path=os.path.join(dir,self.save_dir,self.filename)
        self.show_image(path)


processor=ImageProcessor()

def show_chosen_image():
    if N_List.currentRow()>=0:
        filename=N_List.currentItem().text()
        processor.load_image(dir,filename)
        path=os.path.join(processor.dir,processor.filename)
        processor.show_image(path)

N_List.currentRowChanged.connect(show_chosen_image)
L_Pic.clicked.connect(processor.left)
R_Pic.clicked.connect(processor.right)
B_W_Pic.clicked.connect(processor.nige)
Sharp_Pic.clicked.connect(processor.sharpen)
Rew_Pic.clicked.connect(processor.rewerse)

win.show()
app.exec()

# from PIL import Image, ImageFilter

# with Image.open("Dash.jpg") as pic:
#     print("Size:",pic.size)
#     print("Format:",pic.format)
#     pic.show()

#     pic_niger=pic.convert("L")
#     pic_niger.save("niger.jpg")
#     pic_niger.show()

#     pic_centhore=pic.filter(ImageFilter.GaussianBlur(radius=100))
#     pic_centhore.save("centhore.png")
#     pic_centhore.show()

#     pic_0=pic.transpose(Image.Transpose.ROTATE_180)
#     pic_0.save("0_0.png")
#     pic_0.show()

#     pic_rotate=pic.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
#     pic_rotate.save("rotate.png")
#     pic_rotate.show()

#     box=[0,0,200,200]
#     pic_cropped=pic.crop(box)
#     pic_cropped.save("crop_guk.png")
#     pic_cropped.show()