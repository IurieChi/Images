import os
import PySimpleGUI as sg
import rename_img_createdday as re

# GUI
sg.theme('DarkTeal2')

form_rows = [ 
    [sg.Text('Add created date to image from repository.')],
    [sg.Text('Image path:', size=(10,1)),sg.Input(key='path'),sg.FolderBrowse()], 
    [sg.Text('Select image type:')],
    [sg.Checkbox('Select All:', key= 'all')],
    [sg.Checkbox('JPG',key='.jpg'),sg.Checkbox('PNG',key='.png'),sg.Checkbox('GIF',key='.gif'),sg.Checkbox('RAV',key='.rav'),sg.Checkbox('SVG',key='.svg'),sg.Checkbox('Bitmap', key='.bmp'),sg.Checkbox('HEIC',key='.HEIC')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Rename Img'), sg.Button('Exit')], 
]

window = sg.Window('Rename Image from repository', form_rows)
while True:
    event , value = window.read()
    
    folder_path = value['path'] #save path to variable
    file_type = [] #create ampty aray for file types

    if event == 'Rename Img':
        if folder_path == '':
            window['-OUTPUT-'].update("Select folder",text_color='yellow')
        elif value['all']:
            file_type = ['.jpg','.png','.gif','.bmp','.rav','.svg','.HEIC']
            re.rename_image(folder_path,file_type)
            window['-OUTPUT-'].update("Succes",text_color='green')
        else:
            if value['.jpg'] !=True and value['.png'] !=True and value['.gif']!=True and value['.bmp']!=True and value['.rav'] !=True and value['.HEIC'] !=True and value['.svg'] !=True:
                window['-OUTPUT-'].update('Select image type to be renamed',text_color = 'white')
            else:
                window['-OUTPUT-'].update("")
                for checkbox_key in ['.jpg','.png','.gif','.bmp','.rav','.svg','.HEIC']:
                        if value [checkbox_key]:
                            file_type.append(checkbox_key)

                re.rename_image(folder_path,file_type)
                window['-OUTPUT-'].update("Succes",text_color='white')
                # window['-OUTPUT-'].update(file_type,text_color='yellow')
 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()