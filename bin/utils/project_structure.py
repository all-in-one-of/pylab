import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askdirectory()
folders = ['houdini', 'maya', 'meshes', 'reference', 'textures', 'unreal']
houdini_folders = ['geo', 'hda', 'scripts', 'tex']

def make_project_dir():
    houdini_dir = os.path.join((file_path +'/' + folders[0]))
    for f in folders:
        folder_path = os.path.join((file_path +'/' + f))
        try:
            os.mkdir(folder_path)
            print ('Creating ' + f + ' folders...')
        except FileExistsError:
            print ('Folder already exists!')
    for sub in houdini_folders:
        houdini_sub_dir = os.path.join((houdini_dir +'/' +  sub))
        try:
            os.mkdir(houdini_sub_dir)
            print ('Creating ' + sub + ' folders...')
        except FileExistsError:
            print ('Folder already exists!')

make_project_dir()