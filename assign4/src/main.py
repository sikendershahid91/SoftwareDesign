from processing_unit import ProcessingUnit
from create_block import create_block
import sys


#Venkat: This file should only contain one small main function. Everything else in other files, well tested.

def get_blocks(file_path):
    with open(file_path) as file:
        input_string = file.read().splitlines()

    return list(map(block_create, input_string))


def main():
    file_name = 'user_blocks.txt'
    blocks = get_blocks(sys.path[0] + '/' + file_name)

    print('Block sequence loaded from {}'.format(file_name))
    process_unit = ProcessingUnit(blocks)

    while True:
        print("String for process :: ", end = '')
        print(process_unit.process(input()))


if __name__ == '__main__':
    main()
