#Look on directory check metata data and rename photo with created day

from datetime import datetime
from pathlib import Path
import os
import PySimpleGUI as sg

def generate_created_date(path):
    stat_result = path.stat()
    creation_day = stat_result.st_birthtime
    # Windows --> stat_result.st_ctime
	# Other Unix --> stat_result.st_ctime (last modification date)
	# Other Linux --> stat_result.st_mtime (last modification date)
    timestamp = datetime.utcfromtimestamp(creation_day)
    return timestamp.strftime('%m_%y_')

def rename_image(image_folder, type_file):
    os.chdir(image_folder)
    # type_file = ['png']
    for path in Path(image_folder).iterdir():
        if path.is_file()and path.suffix in type_file:
            # print(f"Rename {path.stem}" )
            date = generate_created_date(path)
            new_name = Path(date + path.stem + path.suffix)
            path.rename(new_name)
            

# ('images')    

# GUI
sg.theme('DarkTeal2')

form_rows = [ 
    [sg.Text('Add created date to image from repository.')],
    [sg.Text('Image path:', size=(10,1)),sg.Input(key='path'),sg.FolderBrowse()], 
    [sg.Text('Select image type:')],
    [sg.Checkbox('Select All:', key= 'all')],
    [sg.Checkbox('JPG',key='.jpg'),sg.Checkbox('PNG',key='.png'),sg.Checkbox('RAV',key='.rav'),sg.Checkbox('HEIC',key='.HEIC'),sg.Checkbox('SVG',key='.svg')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Rename Img'), sg.Button('Exit')], 
]

window = sg.Window('Rename Image from repository', form_rows)
while True:
    event , value = window.read()
    
    f_path = value['path'] #save path to variable
    file_type = [] #create ampty aray for file types

    if event == 'Rename Img':
        if f_path == '':
            window['-OUTPUT-'].update("Select folder",text_color='yellow')
        elif value['all']:
            file_type = ['.jpg','.png','.rav','.HEIC','.svg']
            rename_image(f_path,file_type)
            window['-OUTPUT-'].update("Succes",text_color='green')
        else:
            if value['.jpg'] !=True and value['.png'] !=True and value['.rav'] !=True and value['.HEIC'] !=True and value['.svg'] !=True:
                window['-OUTPUT-'].update('Select image type to be renamed',text_color = 'white')
            else:
                window['-OUTPUT-'].update("")
                for checkbox_key in ['.jpg','.png','.rav','.HEIC','.svg']:
                        if value [checkbox_key]:
                            file_type.append(checkbox_key)

                rename_image(f_path,file_type)
                window['-OUTPUT-'].update("Succes",text_color='green')
                # window['-OUTPUT-'].update(file_type,text_color='yellow')
 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()