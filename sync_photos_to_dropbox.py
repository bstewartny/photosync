import os
from shutil import copy2
import datetime

# where to get masters from
MASTERS_DIR='/Users/bstewart/Pictures/Photos Library.photoslibrary/Masters'

# where to copy masters to
DROPBOX_DIR='/Users/bstewart/Dropbox/Pictures'

def sync():
    print 'Syncing '+MASTERS_DIR +' to '+DROPBOX_DIR+'...'
    for dirName,subDirList,fileList in os.walk(MASTERS_DIR):
        print 'Syncing masters from '+dirName+'...'
        for filePart in fileList:
            filename=dirName+'/'+filePart
            modified_time=os.path.getmtime(filename)
            d=datetime.datetime.fromtimestamp(modified_time)
            folder_path=str(d.year)+'/'+pad(d.month)
            sync_file(filename,filePart,DROPBOX_DIR+'/'+folder_path)

def pad(n):
    if n<10:
        return '0'+str(n)
    else:
        return str(n)

def sync_file(filename,filePart,dest_folder):
    # create destination folder if not already exists
    if not os.path.isdir(dest_folder):
        print 'Creating folder: '+dest_folder
        os.makedirs(dest_folder)
    # copy file retaining create/modified dates if not already exists
    if not os.path.isfile(dest_folder+'/'+filePart):
        print 'Copy '+filename +" to "+dest_folder+'...'
        copy2(filename,dest_folder+'/'+filePart)

if __name__=='__main__':
    sync()
