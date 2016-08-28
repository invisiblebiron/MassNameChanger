'''
Created on 2016/08/24

@author: Brian
'''
import os
import re

#Check to see if the file ends in .xml and split it into file name and extension.
nameRegEx = re.compile(r'(.*)(\.xml)')


if __name__ == '__main__':
    pass

#Select target folder for all languages.
basePath = 'D:\\AGM\\Stardew Valley\\Files Translated'

#Get list for all language folders.
rootFolderList = os.listdir(basePath)

#Iterate through the list, set path to each language folder, and rename each file based on current language folder.
for rootFolder in rootFolderList:
    folderPath = basePath + '\\' + rootFolder
    for root, subfolders, filenames in os.walk(folderPath):
        for filename in filenames:
            mo = nameRegEx.search(filename)
            newName = mo.group(1) + '.' + rootFolder + mo.group(2)
            print('Renaming ' + filename + ' to ' + newName + '...')
            os.rename(os.path.join(root,filename), os.path.join(root, newName))

print('Finished!')
        
