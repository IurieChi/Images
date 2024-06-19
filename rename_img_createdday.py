#Look on directory check metata data and rename photo with created day, month,  year 

from datetime import datetime
import os
from pathlib import Path


def generate_created_date(path,data_format):
    stat_result = path.stat()
    creation_day = stat_result.st_birthtime
    # Windows --> stat_result.st_ctime
	# Other Unix --> stat_result.st_ctime (last modification date)
	# Other Linux --> stat_result.st_mtime (last modification date)
    timestamp = datetime.utcfromtimestamp(creation_day)
    # print(timestamp.strftime(data_format))
    return timestamp.strftime(data_format)

def rename_image(image_folder, type_file,data_format):
    os.chdir(image_folder)
    counter=0
    for path in Path(image_folder).iterdir():
        
        if path.is_file()and path.suffix in type_file:
            print(f"Rename {path.stem}" )
            date = generate_created_date(path,data_format)
            new_name = Path(date+str(counter)+path.suffix)#+ path.stem 
            path.rename(new_name)
        counter+=1
            

# ('images')    


