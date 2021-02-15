from logic_classes.extension_method import OrganiseFilesWithExtension


class OrganiseMethod:
    def __init__(self, path, method) -> None:
        self.path = path
        self.method = method
        
        self.check(self.method)

    def check(self, method):
        if method == 'extension':
            extension_method = OrganiseFilesWithExtension()
            extension_method.organise(self.path)   
        
        elif method == 'size':
            pass
        
        elif method == 'last_used':
            pass
        
        else:
            pass