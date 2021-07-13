import os
import shutil

path = "C:/Users/cyberxploit/Desktop/Test/"
names = os.listdir(path)
folder_name = ["image", "video", "music", "text", "python", "random"]

for x in range(0, 6):
    if not os.path.exists(path + folder_name[x]):
        os.makedirs(path + folder_name[x])
for files in names:
    if ".png" in  files and not os.path.exists(path + "images/" + files):
        shutil.move(path + files, path + "image/" + files)
    elif ".mp3" in files and not os.path.exists(path + "music/" + files):
        shutil.move(path + files, path + "music/" + files)
    elif ".mp4" in files and not os.path.exists(path + "video/" + files):
        shutil.move(path + files, path + "video/" + files)
    elif ".txt" in files and not os.path.exists(path + "text/" + files):
        shutil.move(path + files, path + "text/" + files)
    elif ".py" in files and not os.path.exists(path + "python/" + files):
        shutil.move(path + files, path + "python/" + files)
    else:
        shutil.move(path + files, path + "random/" + files)

print("Job done. You have successfully moved your files into respective created folder")
