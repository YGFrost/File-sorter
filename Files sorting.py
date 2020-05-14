import os
import shutil


path ="C:/Users/YGFrost123/Downloads/"
names = os.listdir(path)
folder_name = ['image' , 'text' , 'gif' , 'rar' , 'zip' , 'exe' , 'mp4' , 'mov']
for x in range(0,7):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])


for files in names:
    if ".png" in files and not os.path.exists(path+'image'+files):
        shutil.move(path+files, path+'image/'+files)

    elif ".jpg" in files and not os.path.exists(path+'image'+files):
        shutil.move(path+files, path+'image/'+files)

    if ".txt" in files and not os.path.exists(path + 'text'+ files):
        shutil.move(path + files, path + 'text/' + files)

    if ".gif" in files and not os.path.exists(path + 'gif' + files):
        shutil.move(path + files, path + 'gif/' + files)

    if ".rar" in files and not os.path.exists(path + 'rar' + files):
        shutil.move(path + files, path + 'rar/' + files)

    elif ".zip" in files and not os.path.exists(path + 'zip' + files):
        shutil.move(path + files, path + 'zip/' + files)

    elif ".exe" in files and not os.path.exists(path + 'exe' + files):
        shutil.move(path + files, path + 'exe/' + files)

    elif ".mp4" in files and not os.path.exists(path + 'mp4' + files):
        shutil.move(path + files, path + 'mp4/' + files)




