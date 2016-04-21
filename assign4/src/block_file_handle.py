from create_block import create_block


def block_file_handle(file_path):
    with open(file_path) as file:
        input_string = file.read().splitlines()

    return list(map(create_block, input_string))
