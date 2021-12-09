import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png'],
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'
print(pickDirectory('.pdf'))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir:
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower() #returns the file extension
        directory = pickDirectory(filetype) #directory should be equal to the category the file belongs to
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True: #if the directory the file matches to does not exist, the script will create a new one w/ that name
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()