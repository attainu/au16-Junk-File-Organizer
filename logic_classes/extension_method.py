import os, shutil

class OrganiseFilesWithExtension():
    def __init__(self):
        self.source = None
        self.destination = None
        self.duplicate = None
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
                print(file)
                extension = file.split('.')[1]

                if extension not in self.list_of_extensions:
                    self.list_of_extensions.append(extension)

                self.source = path + "\\" + file
                self.destination = path + "\\" + extension 
                self.duplicate = self.destination + "\\" + file
                
                self.checkForDuplicates()
                
            except:
                if file not in self.list_of_extensions:
                    new_path = path + '\\' + file
                    self.organise(new_path)
                else:
                    continue

    def checkForDuplicates(self):
        if os.path.exists(self.destination):   
            if os.path.exists(self.duplicate):
                os.remove(self.source)
            else:
                shutil.move(self.source, self.destination) 
        else:
            os.mkdir(self.destination)
            shutil.move(self.source, self.destination)