from commands.commands_class import Commands
import os


class OrganiseFilesWithSize():
    def __init__(self):
        self.size_chart = ["Bytes", "KiloBytes", "Megabytes", "GigaBytes"] 


    def sizeSort(self, path):
        files = os.listdir(path)
        for file in files:
            try:
                extension = file.split('.')[1]
                if extension:
                    source = path + "\\" + file
                    destination = self.assignDestination(path, source)
                    duplicate = destination + "\\" + file

                    deploy = Commands(source, destination, duplicate)
                    deploy.checkAndMove()    

            except:
                if file not in self.size_chart:
                    new_path = path + '\\' + file
                    self.sizeSort(new_path)
                
                else:
                    continue


    def assignDestination(self, path, source):
        size = os.stat(source).st_size

        if size < 1024:
            return path + "\\" + self.size_chart[0] 

        elif size >= 1024 and size < 1048576:
            return path + "\\" + self.size_chart[1] 

        elif size >= 1048576 and size < 1073741824:
            return path + "\\" + self.size_chart[2] 

        else:
            return path + "\\" + self.size_chart[3] 