from importlib import import_module

def create_block(string):
    file_name, class_name, *parameters = string.split()

    imported_module = import_module(file_name)
    class_type = getattr(imported_module, class_name)

    if parameters:
        return class_type(*parameters)
    return class_type()
