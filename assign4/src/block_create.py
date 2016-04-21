from importlib import import_module

def block_create(string):
     if string.count(' ') == 2:
         file_name, class_name, parameters = string.split()
     elif string.count(' ') == 1:
         file_name, class_name = string.split()

    imported_module = import_module(file_name)
    class_type = getattr(imported_module, class_name)

    if parameters:
        return class_type(*parameters)
    return class_type()
