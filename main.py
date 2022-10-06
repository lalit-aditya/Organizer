import os
import getpass
import shutil

username = getpass.getuser();
downloads = 'C:/Users/' + username + '/downloads'
destination = downloads+ "/" + 'Your Files'
folders = ['Images','Installers','Documents']



def createFolder():
    if os.path.exists(destination) == False:
        os.chdir(downloads)
        os.mkdir('Your Files')
        os.chdir('Your Files')
    else:
        print("Your Files : Folder Already Exists")
        print("")
        print("Creating Sub Folders...")
    for paths in folders:
        if os.path.exists(paths) == True:
           global lists
           lists = os.listdir()
           print("Sub Folders Already Exists") 
           break
        else:
          os.mkdir(paths)
          lists = os.listdir()
          

def process():
    folderDocuments = downloads+"/Your Files/Documents"
    folderInstaller = downloads+"/Your Files/Installers"
    folderImage = downloads+"/Your Files/Images"
    os.chdir(downloads)
    for files in os.listdir(downloads):
        if files.endswith((".png",".jpg",".jfif")):
            shutil.move(files, folderImage)
            os.chdir(downloads)
        if files.endswith((".pdf",".txt")):
            shutil.move(files, folderDocuments)

            os.chdir(downloads)
        if files.endswith((".exe",".msi")):
            shutil.move(files, folderInstaller)
            os.chdir(downloads)
    pcx = "Process Completed"
    return pcx

createFolder()
process()




