from tkinter import *
from PIL import Image
import os
import subprocess

root = Tk()

#menu = Menu(root)
#item = Menu(menu)
#item.add_command(label='Website')
#menu.add_cascade(label='Help', menu=item)
#root.config(menu=menu)
root.title("SrcFlow")

title = Label(root, text="SrcFlow 6.9.24")

def confload():
    try:
        confi = open("config.txt","r")
    except FileNotFoundError:
        confi = open("config.txt","w+")
        confi.write("C:\\;C:\\;C:\\;")
    else:
        pass
    curdir = ""
    directs = []
    k = 0
    j = 0

    confl = confi.read()
    print(confl)
    print("parse")
    for i in confl:
        j = j + 1
        if (i == ";"):
            directs.append(curdir)
            curdir = ""
        else:
            curdir = curdir + i
    directs.append(curdir)
    return(directs)
def confsave():
    print("Saving conf")
    confi = open("config.txt", "w")
    confi.write(imgdirf.get() + ";" + qlumpydirf.get() + ";" + waddirf.get())
def funcexport():
    print("Exporting")
    idir = imgdirf.get()
    files = os.listdir(idir)
    # Thanks G4G
    files = [f for f in files if os.path.isfile(idir+'/'+f)]
       
    for i in files:
        try:
            
            currentimage = Image.open(idir + '/' + i)
            currentimage = currentimage.convert("P", palette=Image.ADAPTIVE, colors=8)
            try:
                os.mkdir(idir + '\\8bit\\')
            except:
                pass
            
            currentimage.save(idir + '\\8bit\\' + os.path.splitext(i)[0] + ".bmp")
            print(i + " processed successfully")
        except:
            print(i + " was not processed")
    spargs = (idir + "\\8bit\\" + " " + waddirf.get() + " " + idir + "\\8bit\\" + "script.ls")
    print(spargs)
    subprocess.run(qlumpydirf.get() + "\\makels.exe " + spargs)
    subprocess.run(qlumpydirf.get() + "\\qlumpy.exe " + idir + "\\8bit\\" + "script.ls")


imgdirl = Label(root, text="Image directory: e.g. C:\\Images")
imgdirf = Entry(root)
qlumpydirl = Label(root, text = "HLSDK Texture Tools directory: e.g. C:\\HLSDK\\Texture Wad Tools")
qlumpydirf = Entry(root)
waddirl = Label(root, text="WAD output directory: e.g. C:\\Half-Life\\mymod\\textures")
waddirf = Entry(root)
export = Button(root, text="Export to WAD", command = funcexport)
savetoconf = Button(root, text="Save to Config", command = confsave)

saveddirectories = confload()
print(saveddirectories)
imgdirf.delete(0,END)
imgdirf.insert(0, saveddirectories[0])
qlumpydirf.insert(0, saveddirectories[1])
waddirf.delete(0,END)
waddirf.insert(0, saveddirectories[2])

title.grid(row=0, column=0)
imgdirl.grid(row=1, column=0, sticky="w")
imgdirf.grid(row=1, column=1, ipadx=200)
qlumpydirl.grid(row=2, column=0, sticky="w")
qlumpydirf.grid(row=2, column=1, ipadx=200)
waddirl.grid(row=3, column=0, sticky="w")
waddirf.grid(row=3,column=1, ipadx=200)
export.grid(row=5, column=0)
savetoconf.grid(row=5, column=1)
root.mainloop()