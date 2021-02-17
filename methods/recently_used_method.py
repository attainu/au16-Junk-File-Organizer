from commands.commands_class import Commands
import os
import time


class OrganiseFilesWithRecentlyUsed():
    def __init__(self):
        self.recently_used_chart = ["last_week", "last_month", "6_months_ago", "years_ago"]

    def recentlyUsedSort(self, path):
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
                if file not in self.recently_used_chart:
                    new_path = os.path.join(path, file)
                    self.recentlyUsedSort(new_path)
                else:
                    continue

    def assignDestination(self, path, source):
        current_time = int(os.stat(os.path.join(source)).st_atime)
        recently_used_time = int(time.time()) 
        recently_used_time = (recently_used_time - current_time) // 3600

        if recently_used_time <= 168:
            return os.path.join(path, self.recently_used_chart[0])

        elif recently_used_time <= 5040:
           return os.path.join(path, self.recently_used_chart[1])

        elif recently_used_time <= 30240:
            return os.path.join(path, self.recently_used_chart[2])

        else:
           return os.path.join(path, self.recently_used_chart[3])
        