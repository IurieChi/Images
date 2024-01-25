# Simple app that remove backgroun from image
# For this app to run is required to install "rembg" and 'PIL'

from rembg import remove  
from PIL import Image

image_input =Image.open('/Users/svetlanachigai/Python /Work with Images/curency.png') #add path
output = remove(image_input)
output.save('/Users/svetlanachigai/Python /Work with Images/curency_.png')#add path
