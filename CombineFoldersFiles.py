''' 
Summer Guler
NOTE: Review the pdf document first, HowToOrganizeTranscriptFiles.pdf
- Move files in different subfolders into one folder.
- Combine files with the same format into one file.
- Organize the file by eliminating unnecessary space and other characters. '''

import os
import shutil

def combineFolders():
  ''' Combine subfolders into one folder (for Mac users) '''

  # Don't forget to change the paths
  source = '/Users/summerguler/Downloads/SED/'
  dest = '/Users/summerguler/Downloads/CombinedFolder/'

  # Move the renamed folders (as 1000, 1100, 1200, 1300...)
  for item in range(1000, 2800, 100):
    files = os.listdir(source+str(item))
    for f in files:
      print(f)
      shutil.move(source+str(item)+"/"+f, dest)


def combineFiles():
  ''' Combine files into one file '''

  # Folder that has the files to combine
  folder_path = '/Users/summerguler/Downloads/CombinedFolder/'
  myList = os.listdir(folder_path)

  # Creates and opens a file to append
  with open('/Users/summerguler/Downloads/combinedSEDNotes.srt', 'a+') as zh:

    for i in sorted(myList):
      with open(folder_path+i, encoding="utf8", errors='ignore') as xh:
        print(xh)   # To see whether file names are in order
        contents = xh.read()
        zh.write(contents)


def organizeCombinedFile():
  ''' Organize the combined file by removing unnecessary space and other
   characters '''

  # Specifies the eliminated and replaced characters
  eliminateItem = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
  replaceItem = ('>', '&gt;') # To get rid of unnecessary characters

  with open('/Users/summerguler/Downloads/combinedSEDNotes.srt', 'r') as ih:
    with open('/Users/summerguler/Downloads/myOutput.srt', 'a+') as oh:

      for line in ih:
        line = line.replace('\n', ' ')
        for item in replaceItem:
          line = line.replace(item, '')
        if line.lstrip().startswith('1 '):
          oh.write('\n\n***\n')
        elif not line.lstrip().startswith(eliminateItem):
          oh.write(line)


# Main to run the functions
if __name__ == "__main__":

  # Call the function you want to use, for instance;
  combineFiles()
  organizeCombinedFile()
