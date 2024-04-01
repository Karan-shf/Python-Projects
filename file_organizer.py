import os
import shutil

path = os.path.dirname(__file__)

files_modes = {
    'jpg' : 'images',
    'png' : 'images',
    'jpeg' : 'images',
    'webp' : 'images',
    'gif' : 'videos',
    'mp4' : 'videos',
    'mov' : 'videos',
    'mkv' : 'videos',
    'mp3' : 'audios',
    'ogg' : 'audios',
    'heic' : 'images',
    'pdf' : 'documents',
    'docx' : 'documents',
    'srt' : 'subtitles',
    'ass' : 'subtitles',
}

files_names = os.listdir(path)

formated_names = []

for name in files_names:
    formated_names.append(name.split('.'))

for mode in formated_names:
    mode[1] = mode[1].lower()

new_directory = []

for file in formated_names:
    try:
        if files_modes[file[1]] not in new_directory:
            new_directory.append(files_modes[file[1]])
    except:
        if 'others' not in new_directory:
            new_directory.append('others')

path += '/'

for fold in new_directory:
    os.mkdir(path+fold)

for i in range(len(files_names)):
    try:
        shutil.move(path+files_names[i], path+files_modes[formated_names[i][1]]+'/'+files_names[i])
    except Exception as e:
        shutil.move(path+files_names[i], path+'others/'+files_names[i])
