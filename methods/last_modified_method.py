from commands.commands_class import Commands
import os
import time


class OrganiseFilesWithLastModified():
    def __init__(self):
        self.last_modified_chart = list()

    def lastModifiedSort(self, path):
        files = os.listdir(path)
        for file in files:
            try:
                extension = file.split('.')[1]
                if extension:
                    source = os.path.join(path, file)
                    destination = self.assignDestination(path, source)
                    duplicate = os.path.join(destination, file)

                    deploy = Commands(source, destination, duplicate)
                    deploy.checkAndMove()
                    
            except:
                if file not in self.last_modified_chart:
                    new_path = os.path.join(path, file)
                    self.lastModifiedSort(new_path)
                else:
                    continue

    def assignDestination(self, path, source):
        current_time = os.path.getmtime(os.path.join(source))
        last_modified_time = time.ctime(current_time)
        mm_yy = last_modified_time[4:7] + "-" + last_modified_time[20:24]    
        
        if mm_yy not in self.last_modified_chart:
            self.last_modified_chart.append(mm_yy)
        
        return os.path.join(path, mm_yy)