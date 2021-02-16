import os, shutil

class Commands:
    def __init__(self, source, destination, duplicate):
        self.source = source
        self.destination = destination
        self.duplicate = duplicate

    def checkAndMove(self):
        if os.path.exists(self.destination):   
            self.check()               
        
        else:
            self.create()
            self.move()
    
    
    def check(self):
        if os.path.exists(self.duplicate):
            self.delete()

        else:
            self.move()
    

    def move(self):
        shutil.move(self.source, self.destination)


    def delete(self):
        os.remove(self.source)


    def create(self):
        os.mkdir(self.destination)