from commands.commands_class import Commands
import os

class OrganiseFilesWithExtension():
    def __init__(self):
        self.list_of_extensions = ["html5","html", "htm", "xhtml", "jpeg", "jpg",
                                    "tiff", "gif", "bmp", "png", "bpg", "svg", 
                                    "heif", "psd", "avi", "flv", "wmv", "mov", 
                                    "mp4", "webm", "vob", "mng", "qt", "mpg", 
                                    "mpeg", "3gp", "oxps", "epub", "pages", 
                                    "docx", "doc", "fdf", "ods", "odt", "pwi", 
                                    "xsn", "xps", "dotx", "docm", "dox", "rvg", 
                                    "rtf", "rtfd", "wpd", "xls", "xlsx", "ppt", 
                                    "pptx", "a", "ar", "cpio", "iso", "tar", "gz", 
                                    "rz", "7z", "dmg", "rar", "xar", "zip", "aac", 
                                    "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3",
                                    "msv", "ogg", "oga", "raw", "vox", "wav", "wma", 
                                    "txt", "in", "out", "pdf", "py", "xml", "exe", "sh"
                                    ]

    def organise(self, path):
        files = os.listdir(path)
        for file in files:
            try:
                extension = file.split('.')[1]

                if extension not in self.list_of_extensions:
                    self.list_of_extensions.append(extension)

                source = path + "\\" + file
                destination = path + "\\" + extension 
                duplicate = destination + "\\" + file
                
                deploy = Commands(source, destination, duplicate)
                deploy.checkAndMove()
                
            except:
                if file not in self.list_of_extensions:
                    new_path = path + '\\' + file
                    self.organise(new_path)
                
                else:
                    continue