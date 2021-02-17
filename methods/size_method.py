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
                    source = os.path.join(path, file)
                    destination = self.assignDestination(path, source)
                    duplicate = os.path.join(destination, file)

                    deploy = Commands(source, destination, duplicate)
                    deploy.checkAndMove()

            except IndexError:
                if file not in self.size_chart:
                    new_path = os.path.join(path, file)
                    self.sizeSort(new_path)
                else:
                    continue

    def assignDestination(self, path, source):
        size = os.stat(source).st_size

        if size < 1024:
            return os.path.join(path, self.size_chart[0])

        elif size >= 1024 and size < 1048576:
            return os.path.join(path, self.size_chart[1])

        elif size >= 1048576 and size < 1073741824:
            return os.path.join(path, self.size_chart[2])

        else:
            return os.path.join(path, self.size_chart[3])
