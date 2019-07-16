import os
import string
import tkinter
from os.path import splitext
from tkinter import filedialog
from pathlib import Path, PurePath

def sentenceCase(upperCaseString):
    #fixedString = upperCaseString.capitalize()
    fixedString = (upperCaseString.title()).replace(".","").replace(",","")
    return fixedString
        

def main():
    tkinter.Tk().withdraw()
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to edit file names...'))
    for path, _, files in os.walk(dirPath):
        for capsFile in files:
            fixedFile = sentenceCase(splitext(capsFile)[0]) + splitext(capsFile)[1]
            os.rename(PurePath(path) / capsFile, PurePath(path) /fixedFile)
if(__name__ == "__main__"):
    main()
