from os import listdir, path, makedirs, rename

#Directory to sort
directory = raw_input("Enter Folder : ")

#To make sure that the directory ends with a '/'
if not directory.endswith('/'):
    directory += '/'

#General File Type Extentions
apps      = ("Applications", ['.exe'])
code      = ("Code", ['.py','.java','.c','.cpp','.rb','.asm','.php','.html',
             '.css','.js','.lua','.jar','.o','.obj'])

music     = ("Music", ['.mp3','.ogg','.wav'])
videos    = ("Videos", ['.mp4','.3gp','.avi'])
pictures  = ("Pictures", ['.jpg','.jpeg','.png','.bmp','.gif'])
archives  = ("Archives", ['.zip','.rar','.7zip','.tar','.iso'])

documents = ("Documents", ['.docx','.doc','.pdf','.txt','.ppt','.pptx','.ppsx','.pptm',
             '.docm','.dotx','.dotm','.docb','.xlsx','.xlsm','.xltx',
             '.xltm','.xlsb','.xla','.xlam','.xll','.xlw',
             '.ACCDB','.ACCDE','.ACCDT','.ACCDR','.pub',
             '.potx','.potm','.ppam','.ppsm','.sldx','.sldm'])

allTypes = [apps, code, music, videos, pictures, archives, documents]

#Check each file in the directory

for fil in listdir(directory):
    for typ in allTypes:
        for x in typ[1]:
            if fil.endswith(x) or fil.endswith(x.upper()):
                if not path.exists(directory+typ[0]+'/'):
                    makedirs(directory+typ[0]+'/')
                rename(directory+fil, directory+typ[0]+'/'+fil)

print ""
print "How to Find What We Organised:"
print "Code Folder         - Contains Code, Object Files and jar Files."
print "Music Folder        - Contains Audio Files."
print "Videos Folder       - Contains Video Files."
print "Pictures Folder     - Contains Image Files."
print "Archives Folder     - Contains rar/zip Files and Other Archives."
print "Documents Folder    - Contains Powerpoint and Documents from MS Office."
print "Applications Folder - Contains applications and executable programs."
print "Other Folder        - Contains files that were not sorted into a folder."
