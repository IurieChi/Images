#Look on directory check metata data and rename photo with created day

from datetime import datetime
from pathlib import Path

import PySimpleGUI as sg
import os

def generate_created_date(path):
    stat_result = path.stat()
    creation_day = stat_result.st_birthtime
    # Windows --> stat_result.st_ctime
	# Other Unix --> stat_result.st_ctime (last modification date)
	# Other Linux --> stat_result.st_mtime (last modification date)
    utc_timestamp = datetime.utcfromtimestamp(creation_day)
    return utc_timestamp.strftime('%d_%m_%y')

def rename_image(image_folder):
    type_file = ['.png','.svg']
    for path in Path(image_folder).iterdir():
        if path.is_file()and path.suffix in type_file:
            print(f"Rename {path.stem}" )
            date = generate_created_date(path)
            new_path = Path(image_folder + date + path.stem + path.suffix)
            path.rename(new_path)


#call function 

# ('images')

# GUI
form_rows = [ 
    [sg.Text('Rename Image from repository')],
    [sg.Text('Image path:', size=(10,1)),sg.Input(key='path'),sg.FolderBrowse()],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Rename Img'), sg.Cancel(), sg.Button('Exit')],
    
]

window = sg.Window('Rename Image from repository', form_rows)
while True:
    event , value = window.read()
    if event == 'Rename Img':
        link = value['path']
        window['-OUTPUT-'].update(rename_image(link),text_color='yellow')
    
    if event == 'Cancel':
        window['-OUTPUT-'].update("")
 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()