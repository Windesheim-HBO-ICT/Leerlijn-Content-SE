# Imports
import os, re, shutil
from pathlib import Path

# Variables
from config import failedImages

# Constants
from config import FAIL_CROSS, NOT_NECESSARY, IGNORE_FOLDERS, ERROR_IMAGE_NOT_USED, ERROR_NO_4CID_COMPONENT, ERROR_IMAGE_NOT_FOUND

# Functions
from report.table import generateMarkdownTable


"""
Search for image links in the markdown content, and copy the images from the source/
folder to the build/ folder, preserving the folder structure.

Args:
    content (str): Content of the markdown file.
    src_dir_name (str): Source directory (only the name of the folder itself)
    dest_dir_name (str): Destination directory (only the name of the folder itself)
"""
def copyImages(content, src_dir, dest_dir):
    errors = []
    if content is None:
        return errors
    
    image_links = re.findall(r'!\[\[([^\]]+)\]\]|\!\[([^\]]*)\]\(([^)]+)\)', content)

    for image_link in image_links:
        if image_link[0]:
            image_path = image_link[0].strip()
        elif image_link[2]:
            image_path = image_link[2].strip()

        if not image_path:
            continue

        if image_path.startswith('http://') or image_path.startswith('https://'):
            continue

        found_image_path = None
        for root, dirs, files in os.walk(src_dir):
            if image_path in files:
                found_image_path = Path(root) / image_path
                break

        if found_image_path and found_image_path.exists():
            relativePath = found_image_path.relative_to(src_dir)
            new_image_path = dest_dir / relativePath
            new_image_path.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.copy(found_image_path, new_image_path)
        else:
            print(ERROR_IMAGE_NOT_FOUND + image_path)
            errors.append(ERROR_IMAGE_NOT_FOUND + ' `' + image_path + '` ')

    return errors

# Create a row for the image report table
def createImageTableTow(status, filePath, src_dir, error):
    return {
        "status" : status,
        "image": filePath.stem,
        "path": str(filePath.relative_to(src_dir)),
        "error": error,
    }

# Format the image report table with specific headers and rows
def formatImageReportTable(image_report):
    headers = ["Status", "Image", "Path", "Error"]
    rows = [[
        file['status'], 
        file['image'], 
        file['path'],
        file['error']
    ] for file in image_report]

    table = generateMarkdownTable(headers, rows)
    return table

"""
Fills the image Report with data from the images in the folders
Every unique TC3 and TC1 combination will be added to the Report 2 data.
"""
def fillFailedImages(SRC_DIR, DEST_DIR):
    src_dir = Path(SRC_DIR).resolve()
    dest_dir = Path(DEST_DIR).resolve()
    
    src_images = getImagesInFolder(src_dir)
    dest_images = getImagesInFolder(dest_dir)
    
    for image in dest_images:
        if not str(image.stem).startswith(("PI", "OI", "LT", "DT")):
            failedImages.append(createImageTableTow(FAIL_CROSS, image, dest_dir, ERROR_NO_4CID_COMPONENT))

    for image in src_images: 
        if str(image.stem) not in {str(img.stem) for img in dest_images}:
            failedImages.append(createImageTableTow(NOT_NECESSARY, image, src_dir, ERROR_IMAGE_NOT_USED))    

# Helper method to populate the image report
def getImagesInFolder(dir):
    folders = [folder for folder in Path(dir).rglob("src") if folder.is_dir()]

    images = set()
    
    for folder in folders:
        # Skip curtain folders
        if any(ignore_folder in str(folder) for ignore_folder in IGNORE_FOLDERS):
            continue
        
        # Skip deprecated folders
        if "deprecated" in str(folder):
            continue
        
        images.update(filePath for filePath in folder.rglob("*")) 
    return images
