from os import listdir, remove
from os.path import isfile, join
from pathlib import Path

ROOT = Path(".").cwd()
MIRRORS = ROOT.joinpath("mirrors")

def get_mirror_path(mirror_name: str) -> Path:
    return MIRRORS.joinpath(f"{mirror_name}.mirror")

def is_mirror_file(filename: str):
    return isfile(join(MIRRORS, filename)) and filename.endswith('.mirror')

def get_mirror_files():
    return [file.replace('.mirror', '') for file in listdir(MIRRORS) if is_mirror_file(file)]

def delete_mirror_file(mirror_name: str):
    remove(get_mirror_path(mirror_name))