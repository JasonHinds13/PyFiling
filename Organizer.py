from os import listdir, path, makedirs, rename

#Directory to sort
directory = raw_input("Enter Folder : ")

#To make sure that the directory ends with a '/'
if not directory.endswith('/'):
    directory += '/'

#General File Type Extentions
code      = ['.py','.java','.c','.cpp','.rb','.asm','.php','.html',
             '.css','.js','.lua']

music     = ['.mp3','.ogg','.wav']
videos    = ['.mp4','.3gp','.avi']
pictures  = ['.jpg','.jpeg','.png','.bmp','.gif']
archives  = ['.zip','.rar','.7zip','.tar','.iso']

documents = ['.docx','.doc','.pdf','.txt','.ppt','.pptx','.ppsx','.pptm',
             '.docm','.dotx','.dotm','.docb','.xlsx','.xlsm','.xltx',
             '.xltm','.xlsb','.xla','.xlam','.xll','.xlw',
             '.ACCDB','.ACCDE','.ACCDT','.ACCDR','.pub',
             '.potx','.potm','.ppam','.ppsm','.sldx','.sldm']

#Hold files of the same type
cod = [] #holds files of type code
mus = [] #holds files of type music
vid = [] #holds files of type video
pic = [] #holds files of type picture
arc = [] #holds files of type archives
doc = [] #holds files of type document

#allTypes = [cod, mus, vid, pic, arc, doc]

#Check each file in the directory
for fil in listdir(directory):

    for x in code:
        if fil.endswith(x) or fil.endswith(x.upper()):
            cod.append(fil)
            if not path.exists(directory+'Code/'):
                makedirs(directory+'Code/')
            rename(directory+fil, directory+'Code/'+fil)
       
    for x in music:
        if fil.endswith(x) or fil.endswith(x.upper()):
            mus.append(fil)
            if not path.exists(directory+'Music/'):
                makedirs(directory+'Music/')
            rename(directory+fil, directory+'Music/'+fil)

    for x in videos:
        if fil.endswith(x) or fil.endswith(x.upper()):
            vid.append(fil)
            if not path.exists(directory+'Videos/'):
                makedirs(directory+'Videos/')
            rename(directory+fil, directory+'Videos/'+fil)
            
    for x in pictures:
        if fil.endswith(x) or fil.endswith(x.upper()):
            pic.append(fil)
            if not path.exists(directory+'Pictures/'):
                makedirs(directory+'Pictures/')
            rename(directory+fil, directory+'Pictures/'+fil)

    for x in archives:
        if fil.endswith(x) or fil.endswith(x.upper()):
            arc.append(fil)
            if not path.exists(directory+'Archives/'):
                makedirs(directory+'Archives/')
            rename(directory+fil, directory+'Archives/'+fil)

    for x in documents:
        if fil.endswith(x) or fil.endswith(x.upper()):
            doc.append(fil)
            if not path.exists(directory+'Documents/'):
                makedirs(directory+'Documents/')
            rename(directory+fil, directory+'Documents/'+fil)
