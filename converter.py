# import OS module
import os
# import necessary libraries
from PIL import Image
from pillow_heif import register_heif_opener

# Get the list of all files and directories
windows_type_path = "C:\\Users\\...\\Images" # Example Path
linux_type_path = "c:/Users/.../Images" # Example Path

## WINDOWS USERS COMMENT THE LINE BELOW
linux_type_path = windows_type_path

# Get files
files = os.listdir(path)
register_heif_opener()

for file in files: 
		# import the image 
    im = Image.open(linpath+file)
		# remove the old file
    os.remove(linpath+file)
    rgb_im = im.convert("RGB")
    rgb_im.save(linpath+file.split('.')[0]+'.jpg')

