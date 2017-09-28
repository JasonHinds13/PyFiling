from os import listdir, path, makedirs, rename, environ, path, name
from datetime import datetime
import getpass

#Directory to sort
if name == 'nt':
    # requests user input of relative file path from users profile folder (Windows)
    relative_directory = raw_input("Enter Reletive Folder Path from {0}: ".format(getpass.getuser()))
    directory =  path.join(environ['USERPROFILE'], relative_directory)
else:
    # requests user input of relative file path from users profile folder (Unix)
    relative_directory = raw_input("Enter Reletive Folder Path from {0}: ".format(getpass.getuser()))
    directory =  path.join(environ['HOME'], relative_directory)

#To make sure that the directory ends with a '/'
if not directory.endswith('/'):
    directory += '/'

#General File Type Extentions
exts = {
"Applications": ['.exe', '.bat', '.msi', '.deb'],
"Code": ['.py','.java','.c','.cpp','.rb','.asm','.php','.html','.css','.js','.lua','.jar','.o','.obj'],
"Music": ['.mp3','.ogg','.wav'],
"Videos": ['.mp4','.3gp','.avi'],
"Pictures": ['.jpg','.jpeg','.png','.bmp','.gif'],
"Archives": ['.zip','.rar','.7zip','.tar','.iso', '.gz', '.xz', '.bz2'],
"Documents": ['.docx','.doc','.pdf','.txt','.ppt','.pptx','.ppsx','.pptm',
             '.docm','.dotx','.dotm','.docb','.xlsx','.xlsm','.xltx',
             '.xltm','.xlsb','.xla','.xlam','.xll','.xlw',
             '.ACCDB','.ACCDE','.ACCDT','.ACCDR','.pub',
             '.potx','.potm','.ppam','.ppsm','.sldx','.sldm', '.accdb']
}

#Check each file in the directory
for fil in listdir(directory):
    for typ,lis in exts.iteritems():
        for ex in lis:
            if fil.endswith(ex) or fil.endswith(ex.upper()):
                if not path.exists(directory+typ+'/'):
                    makedirs(directory+typ+'/')
                current_date_time = ".{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(datetime.now().day, datetime.now().month,
                                                                          datetime.now().year, datetime.now().hour,
                                                                          datetime.now().minute, datetime.now().second,
                                                                          datetime.now().microsecond)
                rename(directory+fil, directory+typ+'/'+fil.rsplit(ex)[0]+current_date_time+ex)
                print fil + " : " + typ

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
raw_input('Hit enter to exit')
