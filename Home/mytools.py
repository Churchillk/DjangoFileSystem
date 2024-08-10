from django.shortcuts import render
from argparse import ArgumentParser
from os import system, chdir, getcwd, walk
from pathlib import Path
from colorama import Fore, Style

def arguments():
    parser = ArgumentParser("Django Haphswa Automation")
    parser.add_argument("-n", "--name", type=str, help="enter project name")
    args = parser.parse_args()
    return args

def FileCreation(filelist):
    for filename in filelist:
        with open(filename, 'w') as file:
            if filename == "urls.py":
                file.write("from django.urls import path\nfrom . import views as HomeViews")
            elif filename == "forms.py":
                file.write("from django import forms\nfrom . import models as HomeModels")

def checkAvailability(folderx):
    value = False
    for path, dir, files in walk(getcwd()):
        if folderx in dir:
            value = True
        
    return value

def append_line(filename, insertion):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    #write into file
    with open(filename, 'w') as file:
        i = 0
        while i < len(lines):
            file.write(lines[i])
            for target_line, text_to_append in insertion.items():
                if target_line in lines[i]:
                    file.write(text_to_append)
                    break
            i += 1
