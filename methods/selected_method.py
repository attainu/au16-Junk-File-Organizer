from methods.extension_method import OrganiseFilesWithExtension


class OrganiseMethod():
    def __init__(self, path, method):
        self.path = path
        self.method = method
        
        self.selection(self.method)

    def selection(self, method):
        if method == 'extension':
            call_method = OrganiseFilesWithExtension()
            call_method.organise(self.path)   
        
        elif method == 'size':
            pass
        
        elif method == 'last_used':
            pass
        
        else:
            pass