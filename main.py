from tkinter import *
import os
from PIL import Image
import tkinter as ttk
import tkinter.filedialog as fd
import math

root = NONE
mf = NONE
txt = NONE
WIDTH = 800
HEIGHT = 1280


def openImage():
    dirName = txt.get()
    if(dirName == ""):
        return
    files = fd.askopenfilenames(parent=root, title='Choose a pages', filetypes=(("JPEG", "*.jpg"),("PNG", "*.png")))
    pageCount = 1
    for imgFile in files:
        imgPath = imgFile
        filename, file_extension = os.path.splitext(imgPath)


        dir = os.path.dirname(imgPath)
        path = os.path.join(dir,dirName)
        if(os.path.exists(path) == False):
            os.mkdir(path)
        img = Image.open(imgPath)
        w = math.ceil(img.size[1]/HEIGHT)
        for i in range(w):
            imgName = dirName + "_" + str(pageCount) + file_extension
            imgNewPath = os.path.join(path,imgName)
            box = (0, i*HEIGHT, WIDTH,(i+1)*HEIGHT)
            crop = img.crop(box)
            crop.save(imgNewPath)
            pageCount += 1





def main():
    text = StringVar(value = "CHOOSE IMAGES")
    ttk.Label(mf, textvariable=text).place(relx = 0.5, rely=0.2, anchor = CENTER)



    text = StringVar(value="GIVE NAME")
    ttk.Label(mf, textvariable=text).place(relx=0.5, rely=0.5, anchor=CENTER)
    global txt
    txt = StringVar(value="PAGES")
    folderName = Entry(mf, width=15, textvariable=txt)
    folderName.place(relx=0.5, rely=0.6, anchor=CENTER)

    b = Button(mf, text="SELECT IMAGES", command=openImage)
    b.place(relx=0.5, rely=0.3, anchor=CENTER)



if __name__ == "__main__":
    root = Tk()
    root.title("WEBTOON PAGE SPLITTER")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.minsize(300,250)
    root.maxsize(300,250)
    mf = ttk.Frame(root)
    mf.grid(column=0, row=0, sticky=(N, W, E, S))
    main()

    root.mainloop()