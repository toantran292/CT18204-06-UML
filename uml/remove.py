import os
from fnmatch import fnmatch
from bs4 import BeautifulSoup

def get_svg_files(folder_path):
    contents = os.listdir(folder_path)
    files = [file for file in contents if os.path.isfile(os.path.join(folder_path, file)) and file.endswith(".svg")]
    return files

def delete_text(svg_content):
    soup = BeautifulSoup(svg_content, 'xml') 
    elements = soup.find_all(string='UNREGISTERED')  
    for element in elements:
        parent = element.parent
        if parent.name == 'text':
            parent.decompose() 
    return str(soup)

def edit_svg_file(file_path): 
    with open(file_path, 'r') as file:
        svg_content = file.read()
    modified_svg_content = delete_text(svg_content)
    with open(file_path, 'w') as file:
        file.write(modified_svg_content)

# file = 'UseCaseTongQuat.svg'

root = os.path.dirname(os.path.realpath(__file__))
# files = get_svg_files(current_path)

# for file in files:
#     file_path = os.path.join(current_path, file)
#     edit_svg_file(file_path)
#     print(f"{file} edited successfully")
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "*.svg"):
            fpath = os.path.join(path, name)
            edit_svg_file(fpath)
            print(f"{name} edited successfully")

