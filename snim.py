import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import glob
import sys

gui = Tk()
gui.geometry("400x120")
gui.title("Find Tag")


path = []
results = []

def checkFolderPath():
    if(os.path.isfile("folder_path.txt")):
        f = open("folder_path.txt", "r")
        folder_selected = f.readline()
        f.close()
        return folder_selected


def getFolderPath():
    folder_selected = filedialog.askdirectory()
    f = open("folder_path.txt", "w")
    f.write(folder_selected)
    f.close()
    folderPath.set(folder_selected)
    folder = "{}/**/".format(folder_selected)
    global path
    path = glob.glob(folder+"*.yang", recursive=TRUE)


def search():
    global results
    for f in path:
        files = open(f, "r", encoding="utf-8", errors="ignore")
        listOfLines = []
        line = 1
        flag = False
        while True:
            content = files.readline()            
            if content == "":
                if flag == True:
                    results.append(f+" --------- "+str(listOfLines))
                    results.append("  ")
                break
            if str(E2.get()) in content:
                flag = True
                listOfLines.append(line)
            line = line + 1
        files.close()            
    resultsOfSearch()


def resultsOfSearch():
    resultsList = Tk()
    scrollbary = tkinter.Scrollbar(resultsList, orient="vertical")
    scrollbarx = tkinter.Scrollbar(resultsList, orient="horizontal")
    listbox = Listbox(resultsList, font = 'TkFixedFont', selectmode=EXTENDED)
    listbox.config(width=160, height=50, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
   # listbox.bind("<Double-Button-1>", self.ok)
    scrollbary.config(command=listbox.yview)
    scrollbary.pack(side="right", fill="y")
    scrollbarx.config(command=listbox.xview)
    scrollbarx.pack(side="bottom", fill="x")
    listbox.pack(side="left",fill="both", expand=True)
    listbox.insert(END, "Results for "+str(E2.get())+":")
    for item in results:
        listbox.insert(END, item)
    
    mainloop()


folderPath = StringVar()
folderPath.set(checkFolderPath())
a = Label(gui ,text="Folder Path")
a.grid(row=0,column = 0)
E = Entry(gui,textvariable=folderPath)
E.grid(row=0,column=1)
E2 = Entry(gui)
E2.grid(row=2, column=1)

btnFind = ttk.Button(gui, text="Browse Folder",command=getFolderPath)
btnFind.grid(row=0,column=2)

c = ttk.Button(gui ,text="Search", command=search)
c.grid(row=2,column=2)

gui.mainloop()
