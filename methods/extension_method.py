from commands.commands_class import Commands
import os


class OrganiseFilesWithExtension():
    def __init__(self):
        self.list_of_extensions = ["html5", "html", "htm", "xhtml", "jpeg",
                                   "jpg", "gif", "bmp", "png", "7z", "rar",
                                   "heif", "3gp", "avi", "flv", "wmv", "mov",
                                   "mp4", "webm", "epub", "mpeg", "iso", "mp3",
                                   "docx", "doc", "xps", "xls", "xlsx", "ppt",
                                   "pptx", "zip", "aac", "m4a", "txt", "pdf",
                                   "raw", "wav", "wma", "py", "xml", "exe"]

    def extensionSort(self, path):
        files = os.listdir(path)
        for file in files:
            try:
                split_list = file.split('.')
                extension = split_list[-1]
                if len(split_list) <= 1:
                    raise Exception

                source = os.path.join(path, file)
                destination = self.assignDestination(path, extension)
                duplicate = os.path.join(destination, file)

                deploy = Commands(source, destination, duplicate)
                deploy.checkAndMove()

            except Exception:
                if file not in self.list_of_extensions:
                    new_path = os.path.join(path, file)
                    self.extensionSort(new_path)
                else:
                    continue

    def assignDestination(self, path, extension):
        if extension not in self.list_of_extensions:
            self.list_of_extensions.append(extension)

        return os.path.join(path, extension)
