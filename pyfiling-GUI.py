#If on Windows to avoid fullscreen, use the following two lines of code
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader

from os import listdir, path, makedirs, rename

Builder.load_string('''
<FileOrganizer>:
    
    TextInput:
        id: direct
        pos: 0,root.top-50
        size: root.width-200,50
        hint_text: 'Enter Folder Location'
    Button:
        text: 'Organize'
        size: 200,50
        background_color: 0,.5,1,1
        pos: root.width-200, root.top-50
        on_press:
            status.text = "Attempting To Organize Folder..."
            status.color = (1, .5, 0, 1)
        on_release: root.organize()

    Label:
        id: status
        text: "Ready To Organize..."
        center: root.center
            

''')

class FileOrganizer(Widget):

    def organize(self):

        directory = self.ids.direct.text #Directory entered by the user
        
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
                    
        self.ids.status.text = "Folder has been organized"
        self.ids.status.color = (0, 1, 0, 1)
    
class FilingApp(App):
    
    def build(self):
        return FileOrganizer()
        
    def on_pause(self):
        return True
        
    def on_resume(self):
        pass
        
if __name__ == "__main__":
    FilingApp().run()
