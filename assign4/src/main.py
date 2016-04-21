from processing_unit import ProcessingUnit
from block_create import block_create
import sys


def get_blocks(file_path):
    with open(file_path) as file:
        input_string = file.read().splitlines()

    return list(map(block_create, input_string))

def get_input(file_path):
    with open(file_path) as file:
        input_string = file.read()
    return input_string


def main():
    file_name = 'user_blocks.txt'
    blocks = get_blocks(sys.path[0] + '/' + file_name)

    print('Block sequence loaded from {}'.format(file_name))
    process_unit = ProcessingUnit(blocks)

    file_name = 'user_input.txt'
    input_string = get_input(sys.path[0] + '/' + file_name)
    print('Input sequence loaded from {}'.format(file_name))
    print('input string: {}'.format(input_string))
    print('processed string: {}'.format(process_unit.process(input_string)))

if __name__ == '__main__':
    main()
