from commands.commands_class import Commands
import os
import time


class OrganiseFilesWithLastModified():
    def __init__(self):
        self.last_modified_chart = ["seconds_ago", "minutes_ago", "hours_ago", "days_ago", "weeks_ago", "months_ago"]

    def lastModifiedSort(self, path):
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
                if file not in self.last_modified_chart:
                    new_path = path + '\\' + file
                    self.lastModifiedSort(new_path)
                else:
                    continue

    def assignDestination(self, path, source):
        current_time = int(time.time())
        last_modified_time = int(os.stat(source).st_mtime)
        difference = current_time - last_modified_time
        
        print(current_time, last_modified_time, difference)        
        
        if difference < 60:
            return path + "\\" + self.last_modified_chart[0]

        elif difference < 3600:
            return path + "\\" + self.last_modified_chart[1]
        
        elif difference < 86400:
            return path + "\\" + self.last_modified_chart[2]
        
        elif difference < 604800:
            return path + "\\" + self.last_modified_chart[3]

        elif difference < 2628000:
            return path + "\\" + self.last_modified_chart[4]

        else:
            return path + "\\" + self.last_modified_chart[5]