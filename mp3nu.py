# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:56:34 2020

@author: daanv98
"""

#Importing modules 
import os 
import shutil
from os.path import expanduser
import subprocess
from pathlib import Path

#Directories
music=expanduser('~\\Music\\')
mp3nu='mp3nu'
mp3_before='mp3_before'
mp3_after='mp3_after'
mp3_temp='mp3_temp'  

#Colours and styles for printing
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

#Funtion to set up folders
def folders():
    Path(os.path.join(music, mp3nu)).mkdir(exist_ok=True)
    Path(os.path.join(music, mp3nu, mp3_before)).mkdir(exist_ok=True)
    Path(os.path.join(music, mp3nu, mp3_after)).mkdir(exist_ok=True)
       
    if os.path.exists(os.path.join(music, mp3nu, mp3_before)) == True:
        compare()
    else:
        print('Er is iets fout gegaan bij het instellen van de mappen!')

#Function to check if mp3_before files already exist in mp3_after            
def compare():
    loc=os.path.join(music, mp3nu) 
    src=os.path.join(loc, mp3_before)
    src_files=os.listdir(src) 
    dst=os.path.join(loc, mp3_after)
    dst_files=os.listdir(dst)
    
    for dst_name in dst_files:
        if dst_name[5:] in src_files:
            print(style.YELLOW+dst_name[5:]+style.RESET,'bestaat al in mp3_after met nummer:',style.GREEN+dst_name[0:4]+style.RESET)
            continue           
    copy()
        
#Function to copy multiple files
def copy():
    loc=os.path.join(music, mp3nu)
    src=os.path.join(loc, mp3_before)
    dst=os.path.join(loc, mp3_temp)   
    src_files=os.listdir(src)
    
    if len(src_files) == 0:
        print('Plaats bestanden in de mp3_before map!')
        subprocess.Popen(f'explorer {os.path.realpath(src)}')  
    else:
        Path(os.path.join(music, loc, mp3_temp)).mkdir(exist_ok=True)
        
        global startnr
        startnr=input('Vanaf welk cijfer moet er geteld worden?\n')
        
        for file_name in src_files:
              full_file_name = os.path.join(src, file_name)
              if os.path.isfile(full_file_name) and full_file_name.endswith('.mp3'):
                  shutil.copy(full_file_name, dst)           
        rename()

#Function to rename multiple files 
def rename():   
    loc=os.path.join(music, mp3nu)
    src=os.path.join(loc, mp3_temp)
    dst=os.path.join(loc, mp3_after)
    
    for count, file_name in enumerate(os.listdir(src), start = int(startnr)): 
        try:
            temp_file=os.path.join(src, file_name)
            new_name='{} '.format(str(count).zfill(4))+file_name      
            after_file=os.path.join(dst, new_name)
            os.rename(temp_file, after_file)
            print(new_name)
        except FileExistsError:
            print(style.YELLOW+new_name[5:]+style.RESET,'bestaat al met dit nummer:',style.GREEN+new_name[0:4]+style.RESET)
            os.remove(temp_file)
            continue
        
    os.rmdir(src)   
    subprocess.Popen(f'explorer {os.path.realpath(dst)}') 

os.system("")   
folders()
os.system("pause")