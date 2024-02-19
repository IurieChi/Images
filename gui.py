
import PySimpleGUI as sg
import rename_img_createdday as re
import os.path


# GUI
sg.theme('DarkTeal2')

first_column = [ 
    [sg.Text('Add created date to image from repository.')],
    [sg.Text('Image path:', size=(10,1)),sg.Input(key='path'),sg.FolderBrowse()], 
    [sg.Text('Select required format to be added to image: date, month, year:')],
    [sg.Checkbox('Day',key='d'),sg.Checkbox('Month',key='m'),sg.Checkbox('Year',key='y')],
    [sg.Text('Select image type:')],
    [sg.Checkbox('Select All:', key= 'all')],
    [sg.Checkbox('JPG',key='.jpg'),sg.Checkbox('PNG',key='.png'),sg.Checkbox('GIF',key='.gif'),sg.Checkbox('RAV',key='.rav'),sg.Checkbox('SVG',key='.svg'),sg.Checkbox('Bitmap', key='.bmp'),sg.Checkbox('HEIC',key='.HEIC')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Rename Img'), sg.Button('Exit')], 
    ]

second_column = [
    [sg.Text('Image viewer:',text_color=('yellow'))],
    [sg.Text('Image folder:',size=(10,1)) ,sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),sg.FolderBrowse()],
    [sg.Listbox(values=[], enable_events=True, size=(60,5), key='file_list')],
    # [sg.Text(size=(40,1),key='-tout-')],
    [sg.Image(key='image')]
    ]

#create window layout and separate first colum from second
layout = [
    [   sg.Column(first_column),
        sg.VSeparator(),
        sg.Column(second_column)
    ]
    ]

window = sg.Window('Rename Image from repository', layout)
while True:
    event , value = window.read()
    
    folder_path = value['path'] #save path to variable
    file_type = [] #create empty aray for file types
    date_format = '' #format date 
    image_name = []
    # logic for rename images
    if event == 'Rename Img':
        if folder_path == '':
            window['-OUTPUT-'].update('Select folder! ',text_color='yellow')
        elif value ['d'] != True and value['m']!= True and value['y']!=True:
            window['-OUTPUT-'].update('Please choose date format!',text_color = 'orange')
        else:
            for checkbox_key_date in ['d','m','y']:
                if value[checkbox_key_date]:
                    date_format += '%'+ checkbox_key_date + '_'
            if value['all']:
                file_type = ['.jpg','.png','.gif','.bmp','.rav','.svg','.HEIC']
                re.rename_image(folder_path,file_type,date_format)
                window['-OUTPUT-'].update("Succes",text_color='green')
            else:
                if value['.jpg'] !=True and value['.png'] !=True and value['.gif']!=True and value['.bmp']!=True and value['.rav'] !=True and value['.HEIC'] !=True and value['.svg'] !=True:
                    window['-OUTPUT-'].update('Select image type to be renamed',text_color = 'white')
                else:
                    window['-OUTPUT-'].update("")
                    for checkbox_key in ['.jpg','.png','.gif','.bmp','.rav','.svg','.HEIC']:
                            if value [checkbox_key]:
                                file_type.append(checkbox_key)

                    re.rename_image(folder_path,file_type,date_format)
                    window['-OUTPUT-'].update("Succes",text_color='white')
                    # window['-OUTPUT-'].update(file_type,text_color='yellow')
 
    # Logic for viewer image
    if event == '-FOLDER-':
        # Folder name was filled in, make a list of files in the folder
        folder  = value['-FOLDER-']  
    
        try:
            #get values from folder to a list 
            file_list = os.listdir(folder)
            
        except:
            file_list = []
        image_name = [image for image in file_list if os.path.isfile(os.path.join(folder, image)) and image.lower().endswith((".png",".gif"))]
        window['file_list'].update(image_name)

    elif event == "file_list":  # A file was chosen from the listbox
        try:
            filename = os.path.join(value["-FOLDER-"], value["file_list"][0])
            window["image"].update(filename=filename)
        except:
            pass
        
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()