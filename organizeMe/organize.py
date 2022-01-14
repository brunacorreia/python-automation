import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    print(f"value is {value}")
    for category, suffixes in SUBDIRECTORIES.items():
        print(f"category is {category} and suffixes is {suffixes}")
        for suffix in suffixes:
            print(f"suffix is {suffix}")
            if suffix == value:
                print(f"suffix is {suffix}, value is {value}")
                return category
    return 'MISC' # If filetype does not exist in the dictionary

def organizeDirectory():
    for item in os.scandir():
        print(f"item is {item}")
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower() #returns the file extension
        directory = pickDirectory(filetype) #directory should be equal to the category the file belongs to
        directoryPath = Path(directory)
        print(f"directoryPath is {directoryPath}")
        if directoryPath.is_dir() != True: #if the directory the file matches to does not exist, the script will create a new one w/ that name
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
        
organizeDirectory()