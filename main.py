__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import os.path
import shutil
from zipfile import ZipFile   
import pathlib

base_path = os.getcwd()
cache_path = os.path.join(base_path, "files", "cache")
zip_path = os.path.join(base_path, "files", "data.zip")

def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.makedirs(cache_path)

def cache_zip(zip_path, cache_dir):
    with ZipFile(zip_path, "r") as f:
        f.extractall(cache_dir)
        return cache_dir

def cached_files():
    only_files = []
    for file in os.listdir(cache_path):
        os.chdir(cache_path)
        if os.path.isfile(file):
            only_files.append(os.path.abspath(file))
            os.chdir(base_path)
    return only_files

the_list = cached_files()

def find_password(the_list):
    for file in the_list:
        with open(file, "r") as document:
            text = document.readlines()
            for line in text:
                if "password" in line:
                    password = line.strip().split(": ")[1]
                    return password
                    


#print(base_path) 
#print(cache_path)
#print(zip_path)
#print(clean_cache())
#print(cache_zip(zip_path,cache_path))
#print(cached_files())
print(find_password(the_list))